'''敏感函数提取，进一步判断是source、sink还是Inter_procedural_API'''
import os
import json
import pandas as pd
import openai
from tqdm import tqdm
import logging
from pathlib import Path
import re

# 配置日志和API
logging.basicConfig(level=logging.INFO)
openai.api_key = ""  # 注意：实际使用中应从环境变量获取
openai.base_url = 'https://chatapi.onechats.top/v1/'

'''
data/input_docs/libtiff_doc_input.csv
data/results/stage1/libtiff
data/input_docs/wolfssl_doc_input.csv
data/results/stage1/wolfssl
'''
# 路径配置
INPUT_CSV = "data/input_docs/wolfssl_doc_input.csv"
OUTPUT_DIR = "data/results/stage1/wolfssl"
Path(OUTPUT_DIR).mkdir(exist_ok=True)

# 定义污点角色类型
TAINT_ROLE_SOURCE = "Source"
TAINT_ROLE_SINK = "Sink"
TAINT_ROLE_INTER = "Inter_procedural_API"


def generate_gpt_prompt(content):
    """生成标准化的GPT提示词，包含污点角色判断"""
    return f"""
    You are an expert in secure coding and C/C++ API development. Analyze the following document snippet to:
    1. Identify potentially vulnerable functions
    2. Determine their role in taint analysis (Source, Sink, or Inter_procedural_API)

    **Definitions**:
    - Source: Functions that introduce untrusted data into the program (e.g., reading user input, network data)
    - Sink: Functions that consume data in a security-sensitive way (e.g., system commands, file operations)
    - Inter_procedural_API: Functions that process data between sources and sinks

    **Required Output Format**:
    Return a SINGLE JSON array containing ALL vulnerable functions found, using this exact format:
    {{
        "functions": [
            {{
                "function_name": "LibRaw::dcraw_clear_mem",
                "taint_role": "Source",
                "reason": "Reads untrusted image data"
            }},
            {{
                "function_name": "bad_pixels",
                "taint_role": "Inter_procedural_API",
                "reason": "Processes image data between input and output"
            }}
        ]
    }}
    If no vulnerable functions are found, return: {{"functions": []}}

    **Document Content**:
    {content[:6000]}
    """


def query_gpt_for_vulnerable_functions(content, index):
    """查询GPT并保存原始响应"""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You must strictly follow the required JSON output format. Only return valid JSON."},
                {"role": "user", "content": generate_gpt_prompt(content)}
            ],
            temperature=0.1,  # 降低随机性
            response_format={"type": "json_object"},  # 强制JSON格式
            max_tokens=1000
        )

        raw_response = response.choices[0].message.content

        # 保存原始响应
        output_file = Path(OUTPUT_DIR) / f"wolfssl_llm_response_{index}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(raw_response)

        return raw_response
    except Exception as e:
        logging.error(f"Error processing item {index}: {str(e)}")
        return None


def parse_gpt_response(response_text):
    """更健壮的JSON解析方法"""
    try:
        # 预处理响应文本
        cleaned = response_text.strip()

        # 处理常见的格式问题
        if not cleaned.startswith("{"):
            cleaned = "{" + cleaned
        if not cleaned.endswith("}"):
            cleaned = cleaned + "}"

        # 尝试解析为JSON
        data = json.loads(cleaned)

        # 验证数据结构
        if isinstance(data, dict) and "functions" in data:
            # 确保functions是一个列表
            functions = data.get("functions", [])
            if not isinstance(functions, list):
                return []

            # 验证列表中的每个元素
            validated_functions = []
            for func in functions:
                if isinstance(func, dict):
                    # 确保至少包含function_name
                    if "function_name" in func:
                        validated_func = {
                            "function_name": func["function_name"],
                            "taint_role": func.get("taint_role", TAINT_ROLE_INTER),
                            "reason": func.get("reason", "No reason provided")
                        }
                        validated_functions.append(validated_func)
                elif isinstance(func, str):
                    validated_functions.append({
                        "function_name": func,
                        "taint_role": TAINT_ROLE_INTER,
                        "reason": "Parsed from string response"
                    })

            return validated_functions
        else:
            logging.warning(f"Unexpected response format: {response_text[:200]}...")
            return []
    except json.JSONDecodeError as e:
        logging.error(f"JSON解析失败: {str(e)}")
        logging.debug(f"Problematic response: {response_text[:200]}...")
        return []


def process_all_documents():
    """主处理流程"""
    df = pd.read_csv(INPUT_CSV)
    all_results = []

    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Processing Documents"):
        content = row['content']
        if not isinstance(content, str) or len(content) < 10:
            continue

        response = query_gpt_for_vulnerable_functions(content, idx)
        if not response:
            continue

        functions = parse_gpt_response(response)
        for func in functions:
            result = {
                "doc_index": idx,
                "function_name": "",
                "taint_role": TAINT_ROLE_INTER,  # 默认值
                "reason": "Unknown",
                "source_text": content[:200] + "..."
            }

            if isinstance(func, dict):
                result["function_name"] = func.get("function_name", "")
                result["taint_role"] = func.get("taint_role", TAINT_ROLE_INTER).capitalize()
                if result["taint_role"] not in [TAINT_ROLE_SOURCE, TAINT_ROLE_SINK, TAINT_ROLE_INTER]:
                    result["taint_role"] = TAINT_ROLE_INTER
                result["reason"] = func.get("reason", "No reason provided")
            elif isinstance(func, str):
                result["function_name"] = func.strip()
                result["reason"] = "Parsed from string response"

            if result["function_name"]:  # 只有函数名不为空才添加
                all_results.append(result)

    # 保存汇总结果
    summary_path = Path(OUTPUT_DIR) / "vulnerable_functions_summary.csv"
    pd.DataFrame(all_results).to_csv(summary_path, index=False)

    # 打印统计信息（仅在结果不为空时）
    if all_results:
        role_counts = pd.DataFrame(all_results)["taint_role"].value_counts()
        logging.info(f"Process completed! Found {len(all_results)} potential vulnerable functions.")
        logging.info("Taint role distribution:\n" + str(role_counts))
    else:
        logging.warning("Process completed but no results were found.")


if __name__ == "__main__":
    process_all_documents()


'''敏感函数判断'''
# import os
# import json
# import pandas as pd
# import openai
# from tqdm import tqdm
# import logging
# from pathlib import Path
# import re
#
# # 配置日志和API
# logging.basicConfig(level=logging.INFO)
# openai.api_key = "sk-d683P1LhEiVOs15PlxZiuM1u6ChBoTS1PgqOCklyDcB36fAM"  # 注意：实际使用中应从环境变量获取
# openai.base_url = 'https://chatapi.onechats.top/v1/'
#
# # 路径配置
# INPUT_CSV = "data/input_docs/libtiff_doc_input.csv"
# OUTPUT_DIR = "data/results/stage1/libraw"
# Path(OUTPUT_DIR).mkdir(exist_ok=True)
#
#
# def generate_gpt_prompt(content):
#     """生成标准化的GPT提示词"""
#     return f"""
#     You are an expert in secure coding and C/C++ API development. Analyze the following document snippet to see if it contains function names that could lead to vulnerabilities.
#
#     **Required Output Format**:
#     Return a SINGLE JSON array containing ALL vulnerable functions found, using this exact format:
#     {{
#         "functions": [
#             {{"function_name": "LibRaw::dcraw_clear_mem"}},
#             {{"function_name": "bad_pixels"}}
#         ]
#     }}
#     If no vulnerable functions are found, return: {{"functions": []}}
#
#     **Document Content**:
#     {content[:6000]}  <!-- 限制长度防止token超限 -->
#     """
#
#
# def query_gpt_for_vulnerable_functions(content, index):
#     """查询GPT并保存原始响应"""
#     try:
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system",
#                  "content": "You must strictly follow the required JSON output format. Only return valid JSON."},
#                 {"role": "user", "content": generate_gpt_prompt(content)}
#             ],
#             temperature=0.1,  # 降低随机性
#             response_format={"type": "json_object"},  # 强制JSON格式
#             max_tokens=1000
#         )
#
#         raw_response = response.choices[0].message.content
#
#         # 保存原始响应
#         output_file = Path(OUTPUT_DIR) / f"librawraw_llm_response_{index}.txt"
#         with open(output_file, 'w', encoding='utf-8') as f:
#             f.write(raw_response)
#
#         return raw_response
#     except Exception as e:
#         logging.error(f"Error processing item {index}: {str(e)}")
#         return None
#
#
# def parse_gpt_response(response_text):
#     """更健壮的JSON解析方法"""
#     try:
#         # 预处理响应文本
#         cleaned = response_text.strip()
#
#         # 处理常见的格式问题
#         if not cleaned.startswith("{"):
#             cleaned = "{" + cleaned
#         if not cleaned.endswith("}"):
#             cleaned = cleaned + "}"
#
#         # 尝试解析为JSON
#         data = json.loads(cleaned)
#
#         # 验证数据结构
#         if isinstance(data, dict) and "functions" in data:
#             return data["functions"]
#         elif isinstance(data, list):
#             return data
#         else:
#             logging.warning(f"Unexpected response format: {response_text[:200]}...")
#             return []
#     except json.JSONDecodeError as e:
#         logging.error(f"JSON解析失败: {str(e)}")
#         logging.debug(f"Problematic response: {response_text[:200]}...")
#         return []
#
#
# def process_all_documents():
#     """主处理流程"""
#     df = pd.read_csv(INPUT_CSV)
#     all_results = []
#
#     for idx, row in tqdm(df.iterrows(), total=len(df), desc="Processing Documents"):
#         content = row['content']
#         if not isinstance(content, str) or len(content) < 10:
#             continue
#
#         response = query_gpt_for_vulnerable_functions(content, idx)
#         if not response:
#             continue
#
#         functions = parse_gpt_response(response)
#         for func in functions:
#             if isinstance(func, dict) and "function_name" in func:
#                 all_results.append({
#                     "doc_index": idx,
#                     "function_name": func["function_name"],
#                     "source_text": content[:200] + "..."
#                 })
#             elif isinstance(func, str):  # 处理GPT偶尔直接返回函数名的情况
#                 all_results.append({
#                     "doc_index": idx,
#                     "function_name": func.strip(),
#                     "source_text": content[:200] + "..."
#                 })
#
#     # 保存汇总结果
#     summary_path = Path(OUTPUT_DIR) / "vulnerable_functions_summary.csv"
#     pd.DataFrame(all_results).to_csv(summary_path, index=False)
#     logging.info(f"Process completed! Found {len(all_results)} potential vulnerable functions.")
#
#
# if __name__ == "__main__":
#     process_all_documents()


''' '''
# import os
# import re
# import csv
# import pandas as pd
# import openai
# from tqdm import tqdm
# import sys
# import logging
#
#
# # 设置CSV字段大小限制
# csv.field_size_limit(sys.maxsize)
#
# # 设置 GPT API 密钥
# openai.api_key = "sk-d683P1LhEiVOs15PlxZiuM1u6ChBoTS1PgqOCklyDcB36fAM"
# openai.base_url = 'https://chatapi.onechats.top/v1/'
#
#
#
# def is_sensitive_function(function_name, definition, deve_doc):
#     """
#     使用 GPT 判断给定函数是否为敏感函数，添加 Linux kernel 文档片段支持。
#     """
#     prompt = f"""
# #     You are an expert in secure coding and C/C++ API development. Analyze the following document snippet to see if it contains a function name that could lead to a vulnerability from a security perspective.
# #
# #     Sensitive functions in the Linux kernel are characterized by any of the following types:
#     1. **Alloc / Free**: Functions that allocate or release system resources (e.g., memory, I/O regions).
#     2. **Lock / Unlock**: Functions that manage locks or synchronization primitives to ensure thread or process safety.
#     3. **Start / End**: Functions that initialize or terminate critical system processes or components.
#     4. **Enable / Disable**: Functions that enable or disable hardware, interrupts, or critical features.
#     5. **Register / Unregister**: Functions that register or deregister system components (e.g., device drivers, callbacks).
#     6. **Map / Unmap**: Functions that manage mappings between virtual and physical memory or I/O regions.
#
#     **Vulnerable functions** usually have the following characteristics, which can lead to security risks such as memory corruption, information disclosure, privilege escalation, etc.
#
#     Please review the provided information:
#     C/C++ API development documentation: {deve_doc}
#
#     **Your task**:
#     1. Extract the function names from the document snippet that could lead to the vulnerability.
#     2. Return the result in json format if a potentially vulnerable function name is found, or multiple JSONs if there are multiple potentially vulnerable function names in the document fragment.
#     """
#     try:
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are an expert in secure coding and C/C++ API development."},
#                 {"role": "user", "content": prompt},
#             ],
#             max_tokens=10,  # 限制返回的字符数，只需“Yes”或“No”
#             temperature=0.0
#         )
#         reply = response.choices[0].message.content.strip().lower()
#         return 1 if reply.startswith("yes") else 0
#     except Exception as e:
#         logging.error(f"Error querying GPT for function '{function_name}': {e}")
#         return None  # 若出错，返回 None 以供后续处理
#
#
# def find_section_by_function_name(fragments_path, function_name):
#     """
#     在CSV文件中查找包含function_name的条目，并返回对应的SectionTitle和Content合并后的内容。
#     如果没有找到，返回'No relevant documentation found.'。
#     """
#     try:
#         df = pd.read_csv(fragments_path)
#         relevant_rows = df[df['Content'].str.contains(function_name, case=False, na=False)]
#
#         if not relevant_rows.empty:
#             section_title = relevant_rows.iloc[0]['SectionTitle']
#             content = relevant_rows.iloc[0]['Content']
#             return f"{section_title}\n{content}"
#         else:
#             return "No relevant documentation found."
#     except FileNotFoundError:
#         logging.error(f"文件 {fragments_path} 不存在！")
#         return "No relevant documentation found."
#
#
# def process_csv_row_by_row(file_path, fragments_path, Linux_file_path):
#     """
#     逐行处理主 CSV 文件，调用 GPT 判断敏感函数，并统计比例，支持 Linux kernel 文档片段。
#     """
#     # 初始化结果存储
#     results = []
#     sensitive_count = 0
#     total_calls = 0
#     no_rele_doc_entries = []
#
#     output_dir = "data_process"
#     os.makedirs(output_dir, exist_ok=True)
#
#     with open(file_path, 'r', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         for row in tqdm(reader, desc="Processing Functions"):
#             function_name = row.get("Function Name", "").strip()
#             definition = row.get("Function Code", "").strip()
#
#             if not function_name or not definition:
#                 continue  # 跳过不完整条目
#
#             deve_doc = find_section_by_function_name(fragments_path, function_name)
#
#
#
#             if deve_doc == "No relevant documentation found.":
#                 no_rele_doc_entries.append({
#                     "Function Name": function_name,
#                     "Function Code": definition,
#                     "success": 1
#                 })
#
#                 continue
#             print("----------------------\n")
#
#
#
#             sensitive = is_sensitive_function(function_name, definition, deve_doc)
#
#             if sensitive is not None:
#                 sensitive_count += sensitive
#                 total_calls += 1
#
#             results.append({
#                 "Function Name": function_name,
#                 "Sensitive": sensitive
#             })
#
#     sensitive_ratio = (sensitive_count / total_calls) if total_calls > 0 else 0
#     logging.info(f"Sensitive Ratio: {sensitive_ratio:.2%}")
#
#     output_file = file_path.replace(".csv", "_sensitive_analysis.csv")
#     pd.DataFrame(results).to_csv(output_file, index=False)
#     logging.info(f"Results saved to {output_file}")
#
#     # 保存无相关文档条目到文件
#     if no_rele_doc_entries:
#         no_rele_doc_file = os.path.join(output_dir, "no_rele_doc.csv")
#         pd.DataFrame(no_rele_doc_entries).to_csv(no_rele_doc_file, index=False)
#         logging.info(f"No relevant documentation entries saved to {no_rele_doc_file}")
#
#
# # 示例运行
# file_path = "result/have_func_code_only.csv"
# fragments_path = "database/linux_kernel_sections.csv"
# Linux_file_path = 'linux-4.19'
# process_csv_row_by_row(file_path, fragments_path, Linux_file_path)
#
