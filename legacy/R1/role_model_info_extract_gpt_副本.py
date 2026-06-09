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
openai.api_key = "sk-d683P1LhEiVOs15PlxZiuM1u6ChBoTS1PgqOCklyDcB36fAM"  # 注意：实际使用中应从环境变量获取
openai.base_url = 'https://chatapi.onechats.top/v1/'

MAX_SAMPLES = 10  # 设置最大处理条数

def ensure_directory_exists(path):
    Path(path).mkdir(parents=True, exist_ok=True)
'''source process'''
# def generate_gpt_prompt(content):
#     return f"""作为CodeQL专家，你需要分析以下函数信息并生成一个标准的JSON数组。这个数组必须包含9个元素，特别注意：
#     ["", "", False, "", "", "", "", "", "manual"]
# 1. 第七个参数（索引6）必须指定函数的输出规范，格式必须是以下之一：
#    - "ReturnValue" - 如果是返回值
#    - "Argument[n]" - 如果是第n个参数（从0开始计数）
#    - "Argument[n1,n2]" - 如果涉及多个参数
#    - "Argument[*n]" - 如果是第n个参数的指针解引用
#    - "Argument[Qualifier]" - 如果是限定符参数
#
# 2. 数组格式必须严格遵循：
#    [
#      "命名空间",  // 如果有命名空间信息请填写，否则空字符串
#      "",  // 类型名称，通常为空字符串
#      false,  // 必须是小写的false
#      "函数名",  // 必须填写函数名
#      "",  // 函数签名，通常为空字符串
#      "",  // 扩展字段，必须为空字符串
#      "输出规范",  // 必须按上述格式填写，不能为空
#      "remote",  // 固定值
#      "manual"   // 固定值
#    ]
#
# 示例：
# - 正确格式：["boost::asio", "", false, "read_until", "", "", "Argument[*1]", "remote", "manual"]
# - 正确格式：["", "", false, "malloc", "", "", "ReturnValue", "remote", "manual"]
# - 正确格式：["std", "", false, "memcpy", "", "", "Argument[0,1]", "remote", "manual"]
#
# extensions:
#   - addsTo:
#       pack: codeql/cpp-all
#       extensible: sourceModel
#     data:
#       - ["boost::asio", "", False, "read_until", "", "", "Argument[*1]", "remote", "manual"]
# Since we are adding a new source, we need to add a tuple to the sourceModel extensible predicate. The first five values identify the callable (in this case a free function) to be modeled as a source.
#
# The first value "boost::asio" is the namespace name.
#
# The second value "" is the name of the type (class) that contains the method. Because we're modelling a free function, the type is left blank.
#
# The third value False is a flag that indicates whether or not the sink also applies to all overrides of the method. For a free function, this should be False.
#
# The fourth value "read_until" is the function name.
#
# The fifth value is the function input type signature, which can be used to narrow down between functions that have the same name. In this case, we want the model to include all functions in boost::asio called read_until.
#
# The sixth value should be left empty and is out of scope for this documentation. The remaining values are used to define the output specification, the kind, and the provenance (origin) of the source.
#
# The seventh value "Argument[*1]" is the output specification, which means in this case that the sink is the first indirection (or pointed-to value, *) of the second argument (Argument[1]) passed to the function.
#
# The eighth value "remote" is the kind of the source. The source kind is used to define the threat model where the source is in scope. remote applies to many of the security related queries as it means a remote source of untrusted data. For more information, see "Threat models."
#
# The ninth value "manual" is the provenance of the source, which is used to identify the origin of the source model.
#
# 请你根据下面的内容进行补全：
# {content}
# 请只返回一个JSON数组，格式如：["boost::asio", "", false, "read_until", "", "", "Argument[*1]", "remote", "manual"]。
# 注意：
# 1. 必须返回一个合法的JSON数组
# 2. 数组必须包含恰好9个元素
# 3. 第七个参数（输出规范）必须按照上述格式指定，不能为空
# 4. 所有字符串必须使用双引号
# 5. 布尔值必须是小写的false
# 6. 不要返回任何额外的文字说明
# """

'''sink process'''
def generate_gpt_prompt(content):
    return f"""作为CodeQL专家，你需要分析以下函数信息并生成一个标准的JSON数组。这个数组必须包含9个元素，特别注意：
    ["", "", False, "", "", "", "", "taint", "manual"]
1. 第七个参数（索引6）必须指定函数的输出规范，格式必须是以下之一：
   - "ReturnValue" - 如果是返回值
   - "Argument[n]" - 如果是第n个参数（从0开始计数）
   - "Argument[n1,n2]" - 如果涉及多个参数
   - "Argument[*n]" - 如果是第n个参数的指针解引用
   - "Argument[Qualifier]" - 如果是限定符参数

2. 数组格式必须严格遵循：
   [
     "命名空间",  // 如果有命名空间信息请填写，否则空字符串
     "",  // 类型名称，通常为空字符串
     false,  // 必须是小写的false
     "函数名",  // 必须填写函数名
     "",  // 函数签名，通常为空字符串
     "",  // 扩展字段，必须为空字符串
     "输出规范",  // 必须按上述格式填写，不能为空
     "remote",  // 固定值
     "manual"   // 固定值
   ]

示例：
- 正确格式：["boost::asio", "", false, "read_until", "", "", "Argument[*1]", "taint", "manual"]
- 正确格式：["", "", false, "malloc", "", "", "ReturnValue", "taint", "manual"]
- 正确格式：["std", "", false, "memcpy", "", "", "Argument[0,1]", "taint", "manual"]

extensions:
  - addsTo:
      pack: codeql/cpp-all
      extensible: sourceModel
    data:
      - ["boost::asio", "", False, "read_until", "", "", "Argument[*1]", "remote", "manual"]
Since we are adding a new source, we need to add a tuple to the sourceModel extensible predicate. The first five values identify the callable (in this case a free function) to be modeled as a source.

The first value "boost::asio" is the namespace name.

The second value "" is the name of the type (class) that contains the method. Because we're modelling a free function, the type is left blank.

The third value False is a flag that indicates whether or not the sink also applies to all overrides of the method. For a free function, this should be False.

The fourth value "read_until" is the function name.

The fifth value is the function input type signature, which can be used to narrow down between functions that have the same name. In this case, we want the model to include all functions in boost::asio called read_until.

The sixth value should be left empty and is out of scope for this documentation. The remaining values are used to define the output specification, the kind, and the provenance (origin) of the source.

The seventh value "Argument[*1]" is the output specification, which means in this case that the sink is the first indirection (or pointed-to value, *) of the second argument (Argument[1]) passed to the function.

The eighth value "remote" is the kind of the source. The source kind is used to define the threat model where the source is in scope. remote applies to many of the security related queries as it means a remote source of untrusted data. For more information, see "Threat models."

The ninth value "manual" is the provenance of the source, which is used to identify the origin of the source model.

请你根据下面的内容进行补全：
{content}
请只返回一个JSON数组，格式如：["boost::asio", "", false, "read_until", "", "", "Argument[*1]", "remote", "manual"]。
注意：
1. 必须返回一个合法的JSON数组
2. 数组必须包含恰好9个元素
3. 第七个参数（输出规范）必须按照上述格式指定，不能为空
4. 所有字符串必须使用双引号
5. 布尔值必须是小写的false
6. 不要返回任何额外的文字说明
"""
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def query_gpt_api(content):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a CodeQL expert. You must return a JSON array with exactly 9 elements, where the 7th element (index 6) must specify the output specification (ReturnValue, Argument[n], etc.)."},
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
            if isinstance(parsed_response, list) and len(parsed_response) == 9:
                # 确保false是小写的
                parsed_response[2] = False if isinstance(parsed_response[2], bool) else False
                # 验证第七个参数（索引6）是否符合要求
                if not parsed_response[6] or not isinstance(parsed_response[6], str):
                    print("Error: 7th parameter (output specification) is empty or invalid")
                    return None
                if not (parsed_response[6].startswith("ReturnValue") or 
                       parsed_response[6].startswith("Argument[") or 
                       parsed_response[6].startswith("Parameter[")):
                    print(f"Error: Invalid output specification format: {parsed_response[6]}")
                    return None
                return parsed_response
            else:
                print(f"Invalid response format: expected list of 9 elements, got: {parsed_response}")
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
        if response and isinstance(response, list) and len(response) == 9:
            return response
        return None
    except Exception as e:
        print(f"Error processing content: {str(e)}")
        return None

def save_results(results, output_path):
    # 自定义JSON编码器
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, list) and len(obj) == 9:  # 如果是data数组
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
    # output_file = "R1/source_model_info_extract_gpt.json"
    output_file = "R1/sink_model_info_extract_gpt.json"
    # output_file = "R1/summary_model_info_extract_gpt.json"
    
    # 获取所有以Source_analysis.csv结尾的文件
    # csv_files = glob.glob(os.path.join(input_dir, "*Source_analysis.csv"))
    csv_files = glob.glob(os.path.join(input_dir, "*Sink_analysis.csv"))
    # csv_files = glob.glob(os.path.join(input_dir, "*Inter_procedural_API_analysis.csv"))

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