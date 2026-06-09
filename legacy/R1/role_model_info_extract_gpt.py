import os
import json
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import openai
from tenacity import retry, stop_after_attempt, wait_exponential
import glob

# OpenAI 配置
openai.api_key = os.environ.get("OPENAI_API_KEY", "")  # 从环境变量获取
openai.base_url = 'https://chatapi.onechats.top/v1/'

MAX_SAMPLES = 10  # 设置最大处理条数

def ensure_directory_exists(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def generate_gpt_prompt(content):
    return f"""As a CodeQL expert, you need to analyze the following function information and generate a standard JSON array. This array must contain 10 elements.Pay special attention：
    ["", "", false, "", "", "", "", "", "taint", "manual"]

1. The seventh argument (index 6) must specify the input specification for the function, which must be one of the following：
   - "ReturnValue" - If it's a return value
   - "Argument[n]" - If it is the NTH argument (zero-based)
   - "Argument[n1,n2]" - If multiple parameters are involved
   - "Argument[*n]" - If is the pointer dereferencing of the NTH argument
   - "Argument[Qualifier]" - If it's a qualifier argument

2. The eighth argument (index 7) must specify the output specification of the function in one of the following formats：
   - "ReturnValue" - If the data flows to the return value
   - "Argument[n]" - If the data flows to the NTH argument
   - "Argument[n1,n2]" - If the data flows to multiple parameters
   - "Argument[*n]" - Dereferencing a pointer if data flows to the NTH argument
   - "Argument[Qualifier]" - If the data flows to the qualifier argument

3. The array format must be strictly followed:
   [
     "Namespaces",  // Fill in namespace information if present, otherwise empty string
     "",  // Type name, usually an empty string
     false,  // Must be lowercase false
     "Function name",  // The name of the function is required
     "",  // Function signature, usually an empty string
     "",  // Extended field, must be an empty string
     "Input specification",  // Must be filled in as above, specifying where the data is coming from
     "Output specification",  // Must be filled in the above format, specifying where the data flow
     "taint",  // Fixed value, indicating the taint propagation type
     "manual"   // Fixed value, indicating the origin
   ]

Examples：
- The right format：["boost::asio", "", false, "buffer", "", "", "Argument[*0]", "ReturnValue", "taint", "manual"]
- The right format：["", "", false, "memcpy", "", "", "Argument[1]", "Argument[0]", "taint", "manual"]
- The right format：["std", "", false, "copy", "", "", "Argument[0,1]", "Argument[2]", "taint", "manual"]

This example shows how the CPP query pack models flow through a function for a simple case:

boost::asio::write(socket, boost::asio::buffer(send_str), error);
We need to add tuples to the summaryModel(namespace, type, subtypes, name, signature, ext, input, output, kind, provenance) extensible predicate by updating a data extension file:

extensions:
  - addsTo:
      pack: codeql/cpp-all
      extensible: summaryModel
    data:
      - ["boost::asio", "", False, "buffer", "", "", "Argument[*0]", "ReturnValue", "taint", "manual"]

The seventh value is the input specification (where data flows from). Argument[*0] specifies the first indirection (or pointed-to value, *) of the first argument (Argument[0]) passed to the function.

The eighth value "ReturnValue" is the output specification (where data flows to), in this case the return value.

The ninth value "taint" is the kind of the flow. taint means that taint is propagated through the call.

The tenth value "manual" is the provenance of the summary.

Please fill in the following:
{content}

Just return a JSON array with the following format:["boost::asio", "", false, "buffer", "", "", "Argument[*0]", "ReturnValue", "taint", "manual"].
Note:
1. A valid JSON array must be returned
The array must contain exactly 10 elements
3. The seventh parameter (input specification) must be specified in the above format and cannot be empty
The eighth parameter (output specification) must be specified in the format above and cannot be null
All strings must use double quotes
Boolean values must be lowercase false
7. Don't return any additional text
"""

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def query_gpt_api(content):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a CodeQL expert. You must return a JSON array with exactly 10 elements, where the 7th element (index 6) must specify the input specification and the 8th element (index 7) must specify the output specification (ReturnValue, Argument[n], etc.)."},
                {"role": "user", "content": generate_gpt_prompt(content)}
            ],
            temperature=0.1,
            max_tokens=1000
        )
        raw_response = response.choices[0].message.content.strip()
        print(f"Raw GPT response: {raw_response}")  # 打印原始响应以便调试
        
        # 尝试清理响应文本，确保它是一个有效的JSON数组
        if not raw_response.startswith('['):
            raw_response = raw_response[raw_response.find('['):]
        if not raw_response.endswith(']'):
            raw_response = raw_response[:raw_response.rfind(']')+1]
            
        try:
            parsed_response = json.loads(raw_response)
            if isinstance(parsed_response, list) and len(parsed_response) == 10:  # 修改为10个元素
                # 确保false是小写的
                parsed_response[2] = False if isinstance(parsed_response[2], bool) else False
                # 验证第七个和第八个参数是否符合要求
                if not parsed_response[6] or not isinstance(parsed_response[6], str):
                    print("Error: 7th parameter (input specification) is empty or invalid")
                    return None
                if not parsed_response[7] or not isinstance(parsed_response[7], str):
                    print("Error: 8th parameter (output specification) is empty or invalid")
                    return None
                if not (parsed_response[6].startswith("ReturnValue") or 
                       parsed_response[6].startswith("Argument[") or 
                       parsed_response[6].startswith("Parameter[")):
                    print(f"Error: Invalid input specification format: {parsed_response[6]}")
                    return None
                if not (parsed_response[7].startswith("ReturnValue") or 
                       parsed_response[7].startswith("Argument[") or 
                       parsed_response[7].startswith("Parameter[")):
                    print(f"Error: Invalid output specification format: {parsed_response[7]}")
                    return None
                return parsed_response
            else:
                print(f"Invalid response format: expected list of 10 elements, got: {parsed_response}")
                return None
        except json.JSONDecodeError as je:
            print(f"JSON decode error: {je}")
            print(f"Problematic response: {raw_response}")
            return None
    except Exception as e:
        print(f"Error in GPT API call: {str(e)}")
        return None

def process_content(content):
    try:
        response = query_gpt_api(content)
        if response and isinstance(response, list) and len(response) == 10:  # 修改为10个元素
            return response
        return None
    except Exception as e:
        print(f"Error processing content: {str(e)}")
        return None

def save_results(results, output_path):
    # 自定义JSON编码器
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, list) and len(obj) == 10:  # 如果是data数组
                return json.dumps(obj)[1:-1]  # 移除最外层的方括号
            return json.JSONEncoder.default(self, obj)

    formatted_results = []
    for result in results:
        # 创建新的字典，保持function_name正常格式，但data数组会被特殊处理
        formatted_result = {
            "function_name": result["function_name"],
            "data": result["data"]
        }
        formatted_results.append(formatted_result)

    with open(output_path, 'w') as f:
        json.dump(formatted_results, f, indent=2, cls=CustomJSONEncoder)
        
    # 读取文件内容
    with open(output_path, 'r') as f:
        content = f.read()
    
    # 替换data数组的格式
    content = content.replace('"\\"', '[')
    content = content.replace('\\""', ']')
    content = content.replace('\\", \\"', ', ')
    
    # 重新写入文件
    with open(output_path, 'w') as f:
        f.write(content)

def process_csv_file(input_file, output_file, all_results):
    try:
        # 读取CSV文件
        df = pd.read_csv(input_file)
        
        # 检查必要的列是否存在
        if 'f' not in df.columns or 'col1' not in df.columns:
            print(f"Required columns 'f' and 'col1' not found in CSV file: {input_file}")
            return all_results
        
        # 过滤掉空值和NaN
        df = df.dropna(subset=['f', 'col1'])
        
        # 如果记录数超过MAX_SAMPLES，随机选择MAX_SAMPLES条记录
        if len(df) > MAX_SAMPLES:
            print(f"CSV {input_file} contains {len(df)} records, randomly selecting {MAX_SAMPLES} records")
            df = df.sample(n=MAX_SAMPLES, random_state=42)
        
        total_processed = 0
        
        for idx, row in df.iterrows():
            func_name = row['f']
            content = str(row['col1'])
            
            if not content.strip() or content.strip().lower() == "nan":
                continue
                
            result = process_content(content)
            if result:
                all_results.append({
                    "function_name": func_name,
                    "data": result
                })
                total_processed += 1
                print(f"Processed function {total_processed}/{len(df)}: {func_name} from {os.path.basename(input_file)}")
        
        print(f"Completed processing {input_file}. Total processed: {total_processed}")
        return all_results
        
    except Exception as e:
        print(f"Error processing file {input_file}: {str(e)}")
        return all_results

def main():
    input_dir = "/Users/mycp/CodeQL/7.12/imagemagic"
    output_file = "R1/summary_model_info_extract_gpt.json"
    
    # 获取所有以Inter_procedural_API_analysis.csv结尾的文件
    csv_files = glob.glob(os.path.join(input_dir, "*Inter_procedural_API_analysis.csv"))
    
    if not csv_files:
        print(f"No CSV files found in {input_dir}")
        return
        
    print(f"Found {len(csv_files)} CSV files to process")
    
    # 存储所有结果
    all_results = []
    
    # 处理每个CSV文件
    for csv_file in csv_files:
        print(f"\nProcessing {os.path.basename(csv_file)}...")
        all_results = process_csv_file(csv_file, output_file, all_results)
    
    # 保存所有结果到一个文件
    save_results(all_results, output_file)
    print(f"\nAll results saved to {output_file}. Total functions processed: {len(all_results)}")

if __name__ == "__main__":
    main()