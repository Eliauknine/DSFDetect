# import os
# import openai
# import json
# from pathlib import Path
# from collections import defaultdict
# from tqdm import tqdm
# import time
#
# # 配置 OpenAI API
# openai.api_key = ""  # 注意：实际使用中应从环境变量获取
# openai.base_url = 'https://chatapi.onechats.top/v1/'
# # 并发缺陷类型列表
# CONCURRENCY_TYPES = [
#     "order violation", "data race", "atomicity violation", "deadlock"
# ]
#
#
# def get_gpt_classification(content):
#     """调用 GPT API 判断并发缺陷类型"""
#     prompt = f"""
#     你是一个专业的并发缺陷分析专家。请分析以下代码变更（diff），判断它属于哪种并发缺陷类型：
#
#     **可选类型**:
#     {", ".join(CONCURRENCY_TYPES)}
#
#     **代码变更**:
#     ```diff
#     {content[:6000]}  # 限制长度防止 token 超限
#     ```
#
#     **要求**:
#     1. 只返回最匹配的 **1个类型**（如 `deadlock`）。
#     2. 所需判断的类型一定在提供的类型之中，。
#     3. 直接返回类型名称，不要额外解释。
#
#     **示例输出**:
#     ```
#     data race
#     ```
#     """
#
#     try:
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "你是一个专业的并发缺陷分析助手。"},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.2,  # 降低随机性
#             max_tokens=50,
#         )
#         result = response.choices[0].message.content.strip().lower()
#         return result if result in CONCURRENCY_TYPES else "unknown"
#     except Exception as e:
#         print(f"GPT API 调用失败: {e}")
#         return "unknown"
#
#
# def analyze_diff_file(file_path):
#     """分析单个 diff 文件，调用 GPT 进行分类"""
#     with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
#         content = f.read()
#
#     # 调用 GPT API
#     classification = get_gpt_classification(content)
#     return classification
#
#
# def process_diff_entries(diff_entries_dir):
#     """处理单个 DiffEntries 目录"""
#     type_counts = defaultdict(int)
#     file_results = {}
#
#     diff_files = [f for f in Path(diff_entries_dir).glob("*.txt") if f.is_file()]
#
#     for file_path in tqdm(diff_files, desc=f"Analyzing {Path(diff_entries_dir).parent.name}"):
#         classification = analyze_diff_file(file_path)
#         file_results[file_path.name] = classification
#         type_counts[classification] += 1
#         time.sleep(1)  # 避免 API 限速
#
#     return file_results, type_counts
#
#
# def find_all_diff_entries_dirs(root_dir):
#     """递归查找所有 DiffEntries 目录"""
#     diff_entries_dirs = []
#     for root, dirs, files in os.walk(root_dir):
#         if "DiffEntries" in dirs:
#             diff_entries_dirs.append(os.path.join(root, "DiffEntries"))
#     return diff_entries_dirs
#
#
# def save_results(file_results, type_counts, output_dir, project_name):
#     """保存分析结果到指定目录"""
#     os.makedirs(output_dir, exist_ok=True)
#     output_file = os.path.join(output_dir, f"{project_name}_results.txt")
#
#     with open(output_file, "w", encoding="utf-8") as f:
#         f.write(f"Project: {project_name}\n")
#         f.write("File Classification Results:\n")
#         f.write("===========================\n")
#         for filename, category in file_results.items():
#             f.write(f"{filename}: {category}\n")
#
#         f.write("\nConcurrency Defect Type Statistics:\n")
#         f.write("===================================\n")
#         for t, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
#             f.write(f"{t}: {count}\n")
#
#
# def main():
#     # 配置根目录和输出目录
#     ROOT_DIR = "/Users/mycp/Files/TemCon/数据集"
#     OUTPUT_DIR = os.path.join(ROOT_DIR, "Concurrency_Results")
#     os.makedirs(OUTPUT_DIR, exist_ok=True)
#
#     # 查找所有 DiffEntries 目录
#     diff_entries_dirs = find_all_diff_entries_dirs(ROOT_DIR)
#     print(f"Found {len(diff_entries_dirs)} DiffEntries directories to process.")
#
#     # 处理每个 DiffEntries 目录
#     for diff_entries_dir in diff_entries_dirs:
#         project_name = Path(diff_entries_dir).parent.name
#         print(f"\nProcessing project: {project_name}")
#
#         file_results, type_counts = process_diff_entries(diff_entries_dir)
#         save_results(file_results, type_counts, OUTPUT_DIR, project_name)
#
#         # 打印当前项目的统计结果
#         print("\nConcurrency Defect Type Statistics:")
#         print("===================================")
#         for t, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
#             print(f"{t}: {count}")
#         print(f"Results saved to: {os.path.join(OUTPUT_DIR, f'{project_name}_types.txt')}")
#
#
# if __name__ == "__main__":
#     main()
#     # commons - configuration

# import os
# import openai
# from pathlib import Path
# from collections import defaultdict
# from tqdm import tqdm
# import time
#
# # 配置 OpenAI API
# openai.api_key = "sk-d683P1LhEiVOs15PlxZiuM1u6ChBoTS1PgqOCklyDcB36fAM"  # 注意：实际使用中应从环境变量获取
# openai.base_url = 'https://chatapi.onechats.top/v1/'
# # 并发缺陷类型列表
# CONCURRENCY_TYPES = [
#     "order violation", "data race", "atomicity violation", "deadlock"
# ]
#
#
# def get_gpt_classification(content):
#     """调用 GPT API 判断并发缺陷类型"""
#     prompt = f"""
#     你是一个专业的并发缺陷分析专家。请分析以下代码变更（diff），判断它属于哪种并发缺陷类型：
#
#     **可选类型**:
#     {", ".join(CONCURRENCY_TYPES)}
#
#     **代码变更**:
#     ```diff
#     {content[:6000]}  # 限制长度防止 token 超限
#     ```
#
#     **要求**:
#     1. 只返回最匹配的 **1个类型**（如 `deadlock`）。
#     2. 所需判断的类型一定在提供的四种类型中："order violation", "data race", "atomicity violation", "deadlock"。
#     3. 直接返回类型名称，不要额外解释。
#
#     **示例输出**:
#     ```
#     data race
#     ```
#     """
#
#     try:
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "你是一个专业的并发缺陷分析助手。"},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.2,  # 降低随机性
#             max_tokens=50,
#         )
#         result = response.choices[0].message.content.strip().lower()
#         return result if result in CONCURRENCY_TYPES else "unknown"
#     except Exception as e:
#         print(f"GPT API 调用失败: {e}")
#         return "unknown"
#
#
# def analyze_single_file(file_path):
#     """分析单个 diff 文件并打印结果"""
#     with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
#         content = f.read()
#
#     print(f"\nAnalyzing file: {file_path}")
#     print("=" * 50)
#
#     # 调用 GPT API
#     classification = get_gpt_classification(content)
#
#     print(f"\nAnalysis Result:")
#     print(f"Concurrency Defect Type: {classification}")
#     print("=" * 50)
#
#
# if __name__ == "__main__":
#     # 指定要分析的单个文件路径
#     SINGLE_FILE_PATH = '/Users/mycp/Files/TemCon/数据集/spring-framework/DiffEntries/329fbf_d73c2e_spring-messaging#src#main#java#org#springframework#messaging#simp#SimpMessagingTemplate.java.txt'
#
#     # 检查文件是否存在
#     if not Path(SINGLE_FILE_PATH).exists():
#         print(f"Error: File not found at {SINGLE_FILE_PATH}")
#     else:
#         analyze_single_file(SINGLE_FILE_PATH)



# import csv
# import openai
# from pathlib import Path
# import time
# import os
#
# # 配置 OpenAI API
# openai.api_key = "sk-d683P1LhEiVOs15PlxZiuM1u6ChBoTS1PgqOCklyDcB36fAM"  # 推荐从环境变量获取
# openai.base_url = 'https://chatapi.onechats.top/v1/'
#
# # 读取 CSV
# CSV_PATH = "data/groundtruths/imagemagick_functions_gt_all.csv"
# if not Path(CSV_PATH).exists():
#     raise FileNotFoundError(f"CSV 文件不存在: {CSV_PATH}")
# with open(CSV_PATH, "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     # 取前 20 行用于调试
#     functions = [(row["file_name"], row["function_name"]) for i, row in enumerate(reader) if i < 20]
#
# # with open(CSV_PATH, "r", encoding="utf-8") as f:
# #     reader = csv.DictReader(f)
# #     functions = [(row["file_name"], row["function_name"]) for row in reader]
#
# # Prompt 模板，要求 GPT 自动补齐数据流参数
# prompt_template = """
# 下面给出的是 ImageMagick 项目中的一个函数及其所在的文件位置：
# 文件路径: {file}
# 函数名: {func}
#
# 请你基于你数据库中的知识和对 ImageMagick 的理解，判断该函数更适合建模为以下哪几类（可能有多个），并且补齐替换其中的数据流参数部分的内容：
#
# 1. **sourceModel**
#    表示函数是数据来源（如从外部输入、文件、网络、用户输入读取数据）。
#    数据流参数填写函数的输入参数，例如 Argument[*1]。
#    输出格式：- ["", "", false, "{func}", "", "", "数据流参数", "local", "manual"]
#
# 2. **sinkModel**
#    表示函数是数据出口或敏感操作（如写入文件、网络发送、调用危险 API）。
#    数据流参数填写函数的敏感输入或输出参数，例如 Argument[*1]。
#    输出格式：- ["", "", false, "{func}", "", "", "数据流参数", "remote-sink", "manual"]
#
# 3. **summaryModel**
#    表示函数在输入参数和返回值之间传递或传播数据（即数据流建模）。
#    数据流参数填写函数的输入和返回值：
#    - 倒数第四个位置：输入参数，例如 Argument[*1]
#    - 倒数第三个位置：输出或返回值，例如 ReturnValue
#    输出格式：- ["", "", false, "{func}", "", "输入参数", "返回值", "", "taint", "manual"]
#
# 注意事项：
# - 如果一个函数可能属于多种模型，请分别输出对应的多条结果。
# - 请直接输出 YAML data 部分，每条独立一行，不要输出任何解释或多余文字。
# """
#
#
# # 存储结果
# results_source = []
# results_sink = []
# results_summary = []
#
# def get_gpt_classification(prompt: str) -> str:
#     """调用 GPT API 获取分类和数据流参数 YAML 输出"""
#     try:
#         response = openai.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": "你是一个 CodeQL 建模助手。"},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.2,
#             max_tokens=1000,
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         print(f"[Warning] GPT API 调用失败: {e}")
#         return ""
#
# def extract_yaml_lines(output: str):
#     """从 GPT 输出中提取每一条 YAML 行（以 - [ 开头）"""
#     lines = []
#     for line in output.splitlines():
#         line = line.strip()
#         if line.startswith("- ["):
#             lines.append(line)
#     return lines
#
# def write_yml(filename: str, extensible: str, data_lines: list):
#     """统一写 yml 文件"""
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write("extensions:\n")
#         f.write("  - addsTo:\n")
#         f.write("      pack: codeql/cpp-all\n")
#         f.write(f"      extensible: {extensible}\n")
#         f.write("    data:\n")
#         for line in data_lines:
#             f.write(f"      {line}\n")
#
# # 遍历函数列表
# for file_name, func_name in functions:
#     prompt = prompt_template.format(file=file_name, func=func_name)
#     output = get_gpt_classification(prompt)
#     if not output:
#         time.sleep(2)
#         continue
#
#     yaml_lines = extract_yaml_lines(output)
#
#     # 分类保存
#     for line in yaml_lines:
#         if '"local"' in line:
#             results_source.append(line)
#         if '"remote-sink"' in line:
#             results_sink.append(line)
#         if '"taint"' in line:
#             results_summary.append(line)
#
# # 写入三个 YAML 文件
# write_yml("config/models/imagemagick_source.yml", "sourceModel", results_source)
# write_yml("config/models/imagemagick_sink.yml", "sinkModel", results_sink)
# write_yml("config/models/imagemagick_summary.yml", "summaryModel", results_summary)
#
# print("YAML 文件生成完成！")


import os
import csv
import openai
from pathlib import Path
from tqdm import tqdm
import time

# 配置 OpenAI API
openai.api_key = os.environ.get("OPENAI_API_KEY", "")  # 从环境变量获取
openai.base_url = 'https://chatapi.onechats.top/v1/'

# 读取 CSV，只取前 20 行用于调试
CSV_PATH = "data/groundtruths/imagemagick_functions_gt_all.csv"
if not Path(CSV_PATH).exists():
    raise FileNotFoundError(f"CSV 文件不存在: {CSV_PATH}")

# with open(CSV_PATH, "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     functions = [(row["file_name"], row["function_name"]) for i, row in enumerate(reader) if i < 20]

# functions = []
# seen_func_names = set()
#
# with open(CSV_PATH, "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for i, row in enumerate(reader):
#         if i >= 20:
#             break
#         func_name = row["function_name"]
#         if func_name not in seen_func_names:
#             seen_func_names.add(func_name)
#             functions.append((row["file_name"], func_name))

# with open(CSV_PATH, "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     functions = [(row["file_name"], row["function_name"]) for row in reader]

functions = []
seen_func_names = set()

with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        func_name = row["function_name"]
        if func_name not in seen_func_names:
            seen_func_names.add(func_name)
            functions.append((row["file_name"], func_name))


# 新 Prompt 模板，数据流参数说明和 summaryModel 修正
prompt_template = """
下面给出的是 ImageMagick 项目中的一个函数及其所在的文件位置：
文件路径: {file}
函数名: {func}

请你基于你数据库中的知识和对 ImageMagick 的理解以及你数据库中对ImageMagick中 {func} 的函数定义代码，判断该函数更适合建模为以下哪几类（可能有多个），并且补齐替换其中的数据流参数部分的内容：

1. **sourceModel**  
   表示函数是数据来源（如从外部输入、文件、网络、用户输入读取数据）。  
   数据流参数填写函数的输入参数，例如 Argument[*0] 或 Argument[*1] 或 Argument[*2] 或 ReturnValue等。  
   输出格式：- ["", "", false, "{func}", "", "", "数据流参数", "local", "manual"]

2. **sinkModel**  
   表示函数是数据出口或敏感操作（如写入文件、网络发送、调用危险 API）。  
   数据流参数填写函数的敏感输入或输出参数，例如 Argument[*0] 或 Argument[*1] 或 Argument[*2] 或 ReturnValue等。  
   输出格式：- ["", "", false, "{func}", "", "", "数据流参数", "remote-sink", "manual"]

3. **summaryModel**  
   表示函数在输入参数和返回值之间传递或传播数据（即数据流建模）。  
   数据流参数填写函数的输入和返回值：  
   - 倒数第四个位置：输入参数，例如 Argument[*0] 或 Argument[*1] 或 Argument[*2]  
   - 倒数第三个位置：输出或返回值，例如 Argument[*0] 或 Argument[*1] 或 Argument[*2] 或 ReturnValue  
   输出格式：- ["", "", false, "{func}", "", "", "输入参数", "返回值", "taint", "manual"]
   注意在输出中的{func}不要出现例如Magick::Image::gaussianBlurChannel( const ChannelType channel_ , const double width_ , const double sigma_)这种形式，只应保存函数名，即gaussianBlurChannel，其中的Magick::Image应该放在输出格式的第一个位置。["MagickWand", "", false, "MagickGetImageBluePrimary", "", "", "Argument[*0]", "local", "manual"]是一个正确的示例。

注意事项：
- 如果一个函数可能属于多种模型，请分别输出对应的多条结果。  
- 请直接输出 YAML data 部分，每条独立一行，不要输出任何解释或多余文字。
- 注意一定要区分开命名空间和函数名，请勿出现- ["", "", false, "Magick::ColorRGB::ColorRGB( double red_ , double green_ , double blue_)", "", "", "Argument[*0]", "ReturnValue", "taint", "manual"]这种命名空间、函数名、函数参数混淆在一起的形式
- 注意像Magick::Image::gaussianBlurChannel( const ChannelType channel_ , const double width_ , const double sigma_)这种形式的，其Magick::Image是命名空间，gaussianBlurChannel是函数名，后()中的参数不要，请不要出现例如["", "", false, "Magick::Image::gaussianBlurChannel( const ChannelType channel_ , const double width_ , const double sigma_)", "", "", "Argument[*0]", "local", "manual"]这样的错误，正确的格式应该类似于["Magick::Image", "", false, "floodFillOpacity", "", "", "Argument[*2]", "local", "manual"]
- ["Magick::Image", "", false, "Magick::Image::getPixels", "", "", "Argument[*0]", "local", "manual"]这里错误在于Magick::Image只需要出现在第一个位置
- ["Magick::Color", "", false, "Magick::Color::Color( Quantum red_ , Quantum green_ , Quantum blue_)", "", "", "Argument[*0]", "local", "manual"]这里的错误在于Magick::Color只需出现在第一个位置，同时不应保留( Quantum red_ , Quantum green_ , Quantum blue_)
"""

# 存储结果
results_source = []
results_sink = []
results_summary = []

def get_gpt_classification(prompt: str) -> str:
    """调用 GPT API 获取分类和数据流参数 YAML 输出"""
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini", #gpt-3.5-turbo gpt-4o-mini
            messages=[
                {"role": "system", "content": "你是一个 CodeQL 建模助手。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1000,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[Warning] GPT API 调用失败: {e}")
        return ""

def extract_yaml_lines(output: str):
    """从 GPT 输出中提取每一条 YAML 行（以 - [ 开头）"""
    lines = []
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("- ["):
            lines.append(line)
    return lines

def write_yml(filename: str, extensible: str, data_lines: list):
    """统一写 yml 文件"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("extensions:\n")
        f.write("  - addsTo:\n")
        f.write("      pack: codeql/cpp-all\n")
        f.write(f"      extensible: {extensible}\n")
        f.write("    data:\n")
        for line in data_lines:
            f.write(f"      {line}\n")

# 遍历函数列表，带进度条
for file_name, func_name in tqdm(functions, desc="Processing functions"):
    prompt = prompt_template.format(file=file_name, func=func_name)
    output = get_gpt_classification(prompt)
    if not output:
        time.sleep(2)
        continue

    yaml_lines = extract_yaml_lines(output)

    # 分类保存
    for line in yaml_lines:
        if '"local"' in line:
            results_source.append(line)
        if '"remote-sink"' in line:
            results_sink.append(line)
        if '"taint"' in line:
            results_summary.append(line)

# 写入三个 YAML 文件
write_yml("config/models/imagemagick_source.yml", "sourceModel", results_source)
write_yml("config/models/imagemagick_sink.yml", "sinkModel", results_sink)
write_yml("config/models/imagemagick_summary.yml", "summaryModel", results_summary)

print("YAML 文件生成完成！")
