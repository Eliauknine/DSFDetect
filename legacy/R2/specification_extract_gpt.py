'''对only source/sink.csv文件进行处理'''
import os
import json
import pandas as pd
from pathlib import Path
from datetime import datetime
import openai
from tenacity import retry, stop_after_attempt, wait_exponential
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# OpenAI 配置
openai.api_key = os.environ.get("OPENAI_API_KEY", "")  # 从环境变量获取
openai.base_url = 'https://chatapi.onechats.top/v1/'

def ensure_directory_exists(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def generate_gpt_prompt(content):
    return f"""
You are analyzing taint flow traces for C/C++ programs. The input trace shows how data flows from a source to a sink. Your task is to extract both source and sink function information in JSON format.

✅ Instructions:
- Extract both **Source** and **Sink** from the trace.
- The source is the function where the data originates.
- The sink is the function where tainted data flows into (as one of its arguments).
- Output a **list** of two dictionaries, one for source and one for sink.

Your output must be a JSON list like below. You need to return information about both the source and sink. :

{{
    functions":[
      {{
        "Source": "<source_function_name>",
        "source_args": ["<arg_index>" or "func_call"],
        "type": "source"
      }},
      {{
        "Sink": "<sink_function_name>",
        "sink_args": ["<arg_index>" or "func_call"],  // e.g. "0", "1"
        "type": "sink"
      }}
    ]
}}

⚠️ Rules:
- Only output a JSON list, nothing else.
- If nothing can be extracted, output `[]`.

Input trace:
{content[:4000]}
"""



@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def query_gpt_api(content):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Only return JSON array in correct format."},
                {"role": "user", "content": generate_gpt_prompt(content)}
            ],
            temperature=0.1,
            response_format={"type": "json_object"},
            max_tokens=1000
        )
        raw_response = response.choices[0].message.content
        print(f"Raw GPT output: {raw_response}")
        return json.loads(raw_response)
    except json.JSONDecodeError:
        logging.warning("Invalid JSON returned, retrying...")
        raise
    except Exception as e:
        logging.error(f"GPT error: {e}")
        raise


def process_content(content):
    try:
        response = query_gpt_api(content)
        # response 应该是 dict，含 "functions" 键
        if isinstance(response, dict) and "functions" in response:
            funcs = response["functions"]
            processed = []
            for item in funcs:
                if isinstance(item, dict):
                    # 统一提取函数名、角色、参数位置等
                    func_name = item.get("Source") or item.get("Sink", "")
                    taint_role = item.get("type", "").capitalize()
                    arg_pos = item.get("source_args") or item.get("sink_args", [])
                    processed.append({
                        "function_name": func_name,
                        "taint_role": taint_role,
                        "arg_pos": arg_pos,
                        "source_text": content[:200] + "..."
                    })
            return processed
        else:
            return []
    except Exception as e:
        logging.error(f"Failed to process content: {e}")
        return []





def save_file_results(file_results, output_dir, base_name):
    json_path = os.path.join(output_dir, f"{base_name}.json")
    csv_path = os.path.join(output_dir, f"{base_name}.csv")

    with open(json_path, 'w') as f:
        json.dump(file_results, f, indent=2)

    if file_results:
        pd.json_normalize(file_results).to_csv(csv_path, index=False)


def process_csv_files(input_dir, output_dir):
    processed_files = []
    error_files = []

    for filename in os.listdir(input_dir):
        # if not (filename.endswith('_find_source.csv') or filename.endswith('_find_sink.csv')):
        if not (filename.endswith('_find_source_sink.csv')):
            continue

        file_path = os.path.join(input_dir, filename)
        base_name = Path(filename).stem

        try:
            df = pd.read_csv(file_path)
            if 'col2' not in df.columns:
                logging.warning(f"{filename} missing 'col2' column, skipping.")
                continue

            file_results = []
            for idx, row in df.iterrows():
                content = str(row['col2'])
                if not content.strip() or content.strip().lower() == "nan":
                    continue

                results = process_content(content)
                file_results.extend(results)

            if file_results:
                save_file_results(file_results, output_dir, base_name)
                processed_files.append(filename)
                logging.info(f"Processed and saved results for: {filename}")
            else:
                logging.info(f"No results extracted from: {filename}")
        except Exception as e:
            logging.error(f"Error processing file {filename}: {e}")
            error_files.append(filename)

    return processed_files, error_files

'''
R2/myquery/ql_source_sink_extract/result/libraw
R2/myquery/ql_source_sink_extract/result/libtiff
R2/myquery/ql_source_sink_extract/result/wolfssl"
'''
def main():
    input_dir = "R2/myquery/ql_source_sink_extract/result/libtiff"
    output_dir = "R2/myquery/ql_source_sink_extract/result/result_specification_extract_gpt/libtiff"

    ensure_directory_exists(output_dir)

    processed_files, error_files = process_csv_files(input_dir, output_dir)

    logging.info("\n=== Processing Summary ===")
    logging.info(f"Processed files: {len(processed_files)}")
    logging.info(f"Error files: {len(error_files)}")
    if error_files:
        logging.info(f"Files with errors: {error_files}")


if __name__ == "__main__":
    main()
    # test_input = "Upstream flow from source to GetPreviousImageInList Source: Function call: ReadOnePNGImage Source Signature: ReadOnePNGImage(MngInfo * mng_info, const ImageInfo * image_info, ExceptionInfo * exception) Sink: Argument of GetPreviousImageInList Sink Signature: GetPreviousImageInList(const Image * (unnamed parameter 0))"
    # print(query_gpt_api(test_input))

