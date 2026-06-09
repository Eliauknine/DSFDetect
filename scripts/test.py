# # import csv
# # import re
# #
# # csv_file = "data/groundtruths/wolfssl_functions_gt.csv"
# # function_names = []  # 临时存储所有名称（含重复）
# #
# #
# # def extract_function_name(raw_name):
# #     # 情况1：如果已经是纯函数名（无括号），直接返回
# #     if not re.search(r'\(', raw_name):
# #         yield raw_name
# #         return
# #
# #     # 情况2：如果包含括号，提取括号前的名称
# #     matches = re.finditer(r'(\b[a-zA-Z_]\w*)\s*\(', raw_name)
# #     for match in matches:
# #         func_name = match.group(1)
# #         # 过滤掉纯C关键字（如 `if`、`for`，但保留 `if_something`）
# #         if func_name.lower() in {"if", "for", "while", "return"} and not re.search(r'^\w+\s*\(', raw_name):
# #             continue
# #         yield func_name
# #
# #
# # with open(csv_file, mode='r', encoding='utf-8') as file:
# #     reader = csv.DictReader(file)
# #     for row in reader:
# #         if 'function_name' not in row or not row['function_name'].strip():
# #             continue
# #         raw_name = row['function_name'].strip()
# #         for func_name in extract_function_name(raw_name):
# #             function_names.append(func_name)
# #
# # # 去重并保持顺序（Python 3.7+ 字典有序）
# # unique_function_names = list(dict.fromkeys(function_names))
# #
# # # 生成 predicate_code
# # predicate_code = 'predicate targetFunctions(string funcName) {\n'
# # predicate_code += '    funcName = "' + '" or\n    funcName = "'.join(unique_function_names) + '"\n'
# # predicate_code += '    // 可以继续添加其他函数名\n'
# # predicate_code += '}'
# #
# # print(predicate_code)
# # print(f"\nTotal unique functions extracted: {len(unique_function_names)}")
#
# '''累加求和'''
# # import os
# # import pandas as pd
# # from pathlib import Path
# #
# # # 设置CSV文件目录路径
# # csv_dir = "R3/ql_path_search/result/ql_path_search_imagemagic"
# #
# # # 初始化一个空的DataFrame用于存储汇总结果
# # summary_df = None
# #
# # # 遍历目录中的所有CSV文件
# # for csv_file in Path(csv_dir).glob("*.csv"):
# #     # 读取CSV文件
# #     df = pd.read_csv(csv_file)
# #
# #     # 如果是第一个文件，直接作为初始汇总结果
# #     if summary_df is None:
# #         summary_df = df.copy()
# #     else:
# #         # 确保function_name列匹配
# #         if not all(summary_df["function_name"] == df["function_name"]):
# #             print(f"警告: {csv_file.name}的function_name顺序不匹配，已跳过")
# #             continue
# #
# #         # 累加is_present列
# #         summary_df["is_present"] += df["is_present"]
# #
# # # 按is_present降序排序
# # summary_df = summary_df.sort_values("is_present", ascending=False)
# #
# # # 保存汇总结果到新CSV文件
# # output_path = os.path.join(csv_dir, "summary_result.csv")
# # summary_df.to_csv(output_path, index=False)
# #
# # print(f"汇总完成，结果已保存到: {output_path}")
# # print("\n汇总结果预览:")
# # print(summary_df.head())
#
# '''warning次数'''
# # import csv
# # from collections import defaultdict
# #
# # # 文件路径
# # summary_path = 'R3/ql_path_search/result/ql_path_search_imagemagic/summary_result.csv'
# # gt_path = 'data/groundtruths/imagemagick_functions_gt.csv'
# #
# # # 1. 读取groundtruth文件并统计每个function_name的出现次数
# # function_counts = defaultdict(int)
# #
# # with open(gt_path, 'r') as gt_file:
# #     gt_reader = csv.DictReader(gt_file)
# #     for row in gt_reader:
# #         function_name = row['function_name']
# #         function_counts[function_name] += 1
# #
# # # 2. 读取summary文件并更新is_present值
# # updated_rows = []
# # with open(summary_path, 'r') as summary_file:
# #     summary_reader = csv.DictReader(summary_file)
# #     fieldnames = summary_reader.fieldnames
# #
# #     for row in summary_reader:
# #         function_name = row['function_name']
# #         count = function_counts.get(function_name, 0)
# #         row['is_present'] = str(float(row['is_present']) * count)
# #         updated_rows.append(row)
# #
# # # 3. 将更新后的数据写回summary文件
# # with open(summary_path, 'w', newline='') as summary_file:
# #     writer = csv.DictWriter(summary_file, fieldnames=fieldnames)
# #     writer.writeheader()
# #     writer.writerows(updated_rows)
# #
# # print(f"已更新 {len(updated_rows)} 行数据")
#
# '''result检索'''
# # import pandas as pd
# # import os
# #
# # # 定义文件路径
# # summary_path = 'R3/ql_path_search/result/ql_path_search_imagemagic/summary_result.csv'
# # groundtruth_path = 'data/groundtruths/imagemagick_functions_gt.csv'
# # output_dir = 'R3/detect'
# # output_path = os.path.join(output_dir, 'imagemagic_result.csv')
# #
# # # 确保输出目录存在
# # os.makedirs(output_dir, exist_ok=True)
# #
# # # 1. 读取summary_result.csv文件
# # summary_df = pd.read_csv(summary_path)
# #
# # # 2. 筛选is_present不为0的行
# # filtered_summary = summary_df[summary_df['is_present'] != 0]
# #
# # # 3. 读取groundtruth文件
# # groundtruth_df = pd.read_csv(groundtruth_path)
# #
# # # 4. 在groundtruth中检索包含function_name的行（部分匹配）
# # result_rows = []
# # for func_name in filtered_summary['function_name']:
# #     matched_rows = groundtruth_df[groundtruth_df['function_name'].str.contains(func_name, regex=False, na=False)]
# #     result_rows.append(matched_rows)
# #
# # # 5. 合并所有匹配的行
# # result_df = pd.concat(result_rows) if result_rows else pd.DataFrame()
# #
# # # 6. 保存结果到result.csv
# # result_df.to_csv(output_path, index=False)
# #
# # print(f"处理完成，结果已保存到 {output_path}")
# # print(f"共找到 {len(result_df)} 条匹配记录")
#
# '''累加求和is_present'''
#
# # import pandas as pd
# #
# # # 定义文件路径
# # summary_path = 'R3/ql_path_search/result/ql_path_search_imagemagic/summary_result.csv'
# #
# # # 1. 读取 summary_result.csv 文件
# # summary_df = pd.read_csv(summary_path)
# #
# # # 2. 计算 is_present 列的总和
# # total_sum = summary_df['is_present'].sum()
# #
# # # 3. 打印结果
# # print(f"is_present 列的总和: {total_sum}")
#
# '''统计每个 CVE 的出现次数'''
# # import pandas as pd
# #
# # # 定义文件路径
# # file_path = 'R3/detect/imagemagic_result.csv'
# #
# # # 1. 读取 CSV 文件
# # df = pd.read_csv(file_path)
# #
# # # 2. 获取 cve 列的唯一值（去重）
# # unique_cves = df['cve'].unique()
# #
# # # 3. 计算唯一 CVE 的数量
# # num_unique_cves = len(unique_cves)
# #
# # # 4. 打印结果
# # print(f"共有 {num_unique_cves} 种不同的 CVE")
# # print("唯一 CVE 列表：")
# # print(unique_cves)
# #
# # import pandas as pd
# #
# # file_path = '/Users/mycp/CodeQL/result/node/result/warning/wolfssl_result.csv'
# # df = pd.read_csv(file_path)
# #
# # # 统计每个 CVE 出现的次数
# # cve_counts = df['cve'].value_counts()
# #
# # print("CVE 统计结果：")
# # print(cve_counts)
#
# '''对commit sha值一样的提取'''
# # import pandas as pd
# # import os
# #
# # # 文件路径
# # imagemagick_file = '/Users/mycp/CodeQL/result/node/result/warning/wolfssl_result.csv'
# # metrics_file = '/Users/mycp/PycharmProjects/pythonProject/extract/12653656/1-5_7-9/7_analysis/prioritization_performance/analyzed-warning-severity-effort-metrics.csv'
# # output_dir = '/Users/mycp/CodeQL/result/node/result/warning/baseline'
# #
# # # 确保输出目录存在
# # os.makedirs(output_dir, exist_ok=True)
# #
# # # 读取CSV文件
# # imagemagick_df = pd.read_csv(imagemagick_file)
# # metrics_df = pd.read_csv(metrics_file)
# #
# # # 获取imagemagick文件中的commit_sha列表
# # target_shas = set(imagemagick_df['commit_sha'].dropna().unique())
# #
# # # 在metrics文件中筛选匹配的commit_sha
# # matched_df = metrics_df[metrics_df['commit_sha'].isin(target_shas)]
# #
# # # 保存结果到baseline目录
# # output_file = os.path.join(output_dir, 'wolfssl_matched_metrics.csv')
# # matched_df.to_csv(output_file, index=False)
# #
# # print(f"匹配完成，结果已保存到: {output_file}")
# # print(f"匹配到的记录数: {len(matched_df)}")
#
# '''汇总vulnerable_function的数量'''
# # import pandas as pd
# #
# # # 文件路径
# # input_file = '/Users/mycp/CodeQL/result/node/result/warning/baseline/wolfssl_matched_metrics.csv'
# #
# # # 读取CSV文件
# # df = pd.read_csv(input_file)
# #
# # # 筛选条件：tool = 'codeql' 且 is_successful_effort = True
# # filtered_df = df[(df['tool'] == 'codechecker') & (df['is_successful_effort'] == True)]
# #
# # # 计算符合条件的 vulnerable_function 总数
# # total_vulnerable_functions = filtered_df['vulnerable_functions'].sum()
# #
# # # 输出结果
# # print(f"符合条件的条目数: {len(filtered_df)}")
# # print(f"vulnerable_function 总数: {total_vulnerable_functions}")
#
# # 可选：保存筛选后的数据到新文件（如果需要）
# # output_file = '/Users/mycp/CodeQL/result/node/result/warning/baseline/codeql_successful_efforts.csv'
# # filtered_df.to_csv(output_file, index=False)
# # print(f"筛选后的数据已保存至: {output_file}")
#
#
# '''合并csv文件'''
# # import pandas as pd
# #
# #
# # def merge_csv_files(file1_path, file2_path, output_path):
# #     """
# #     合并两个CSV文件并保存到指定路径
# #
# #     参数:
# #         file1_path (str): 第一个CSV文件路径
# #         file2_path (str): 第二个CSV文件路径
# #         output_path (str): 合并后的输出路径
# #     """
# #     try:
# #         # 读取两个CSV文件
# #         df1 = pd.read_csv(file1_path)
# #         df2 = pd.read_csv(file2_path)
# #
# #         # 合并数据（假设需要简单拼接）
# #         merged_df = pd.concat([df1, df2], ignore_index=True)
# #
# #         # 去重（如果需要）
# #         merged_df = merged_df.drop_duplicates()
# #
# #         # 保存到目标路径
# #         merged_df.to_csv(output_path, index=False)
# #         print(f"成功合并文件并保存到: {output_path}")
# #
# #     except Exception as e:
# #         print(f"处理过程中发生错误: {str(e)}")
# #
# #
# # # 文件路径
# # file1 = "data/results/stage1/filtered/imagemagic_taint_functions1.csv"
# # file2 = "data/results/stage1/imagemagic/vulnerable_functions_summary.csv"
# # output = "data/results/stage1/imagemagic/vulnerable_functions_summary.csv"
# #
# # # 执行合并
# # merge_csv_files(file1, file2, output)
#
# '''查看R2/myquery/ql_source_sink_extract/result/imagemagic下有多少个csv文件'''
# # import os
# #
# # def count_csv_files(directory):
# #     """
# #     统计指定目录及其子目录下的CSV文件数量
# #     """
# #     csv_count = 0
# #
# #     for root, dirs, files in os.walk(directory):
# #         for file in files:
# #             if file.lower().endswith('.csv'):
# #                 csv_count += 1
# #
# #     return csv_count
# #
# #
# # if __name__ == "__main__":
# #     target_directory = "R2/myquery/ql_source_sink_extract/result/imagemagic"
# #
# #     try:
# #         count = count_csv_files(target_directory)
# #         print(f"在目录 {target_directory} 及其子目录下共找到 {count} 个CSV文件")
# #     except FileNotFoundError:
# #         print(f"错误：目录 {target_directory} 不存在")
# #     except Exception as e:
# #         print(f"发生错误: {str(e)}")
#
#
#
# '''检查目录下所有CSV文件中是否存在taint_role为Sink且arg_pos为func_call的行'''
#
# # import os
# # import pandas as pd
# #
# #
# # def check_sink_func_call(directory):
# #     """
# #     检查目录下所有CSV文件中是否存在taint_role为Sink且arg_pos为func_call的行
# #     """
# #     found_in_files = []
# #
# #     for root, dirs, files in os.walk(directory):
# #         for file in files:
# #             if file.lower().endswith('.csv'):
# #                 file_path = os.path.join(root, file)
# #
# #                 try:
# #                     # 读取CSV文件
# #                     df = pd.read_csv(file_path)
# #
# #                     # 检查是否包含所需的列
# #                     if 'taint_role' not in df.columns or 'arg_pos' not in df.columns:
# #                         continue
# #
# #                     # 检查条件
# #                     condition = (df['taint_role'] == 'Sink') & (df['arg_pos'] == 'func_call')
# #                     if condition.any():
# #                         found_in_files.append(file_path)
# #                         print(f"存在: {file_path} 中包含taint_role为Sink且arg_pos为func_call的行")
# #
# #                 except Exception as e:
# #                     print(f"处理文件 {file_path} 时出错: {str(e)}")
# #
# #     # 输出最终结果
# #     if found_in_files:
# #         print("\n总结: 以下文件包含符合条件的行:")
# #         for file in found_in_files:
# #             print(f"- {file}")
# #     else:
# #         print("\n总结: 没有找到任何文件包含taint_role为Sink且arg_pos为func_call的行")
# #
# #
# # if __name__ == "__main__":
# #     target_directory = "R2/myquery/ql_source_sink_extract/result/result_specification_extract_gpt/imagemagic"
# #
# #     if not os.path.exists(target_directory):
# #         print(f"错误: 目录 {target_directory} 不存在")
# #     else:
# #         check_sink_func_call(target_directory)
#
#
# '''检查所有文件的arg_pos列是否均为合法形式'''
# # import os
# # import pandas as pd
# #
# # # 目标目录路径
# # target_dir = "R2/myquery/ql_source_sink_extract/result/result_specification_extract_gpt/imagemagic"
# #
# # # 存储异常文件名
# # abnormal_files = []
# #
# #
# # # 暴力检查函数
# # def is_valid_arg_pos(value):
# #     value = str(value).strip()  # 转为字符串并去除首尾空格
# #
# #     # 检查是否为数字形式（如 ['0'] 或 ['0', '1']）
# #     if len(value) >= 3 and value[2].isdigit():  # 第3个字符是数字
# #         return True
# #
# #     # 检查是否为函数调用形式（如 ['func_call']）
# #     if len(value) >= 7 and value[2:7] == "func_":  # 第3-7个字符是 'func_'
# #         return True
# #
# #     # 其他情况非法
# #     return False
# #
# #
# # # 遍历目录下所有CSV文件
# # for filename in os.listdir(target_dir):
# #     if filename.endswith(".csv"):
# #         filepath = os.path.join(target_dir, filename)
# #         try:
# #             df = pd.read_csv(filepath)
# #
# #             if "arg_pos" in df.columns:
# #                 # 检查每个arg_pos值是否合法
# #                 for value in df["arg_pos"].astype(str).unique():
# #                     if not is_valid_arg_pos(value):
# #                         abnormal_files.append(filename)
# #                         print(f"异常文件: {filename}, 非法值: {value}")
# #                         break  # 发现一个非法值即可标记文件
# #
# #         except Exception as e:
# #             print(f"处理文件 {filename} 时出错: {e}")
# #
# # # 输出结果
# # if abnormal_files:
# #     print("\n存在非法arg_pos值的文件:")
# #     for file in set(abnormal_files):  # 去重
# #         print(file)
# # else:
# #     print("所有文件的arg_pos列均为合法形式。")
#
# '''并发缺陷'''
#
# # import os
# #
# # base_path = "/Users/mycp/Files/TemCon/数据集"
# # total_files = 0
# #
# # for root, dirs, files in os.walk(base_path):
# #     if "prevFiles" in dirs:
# #         diff_path = os.path.join(root, "prevFiles")
# #         count = len([f for f in os.listdir(diff_path) if os.path.isfile(os.path.join(diff_path, f))])
# #         total_files += count
# #
# # print(f"Total files in all DiffEntries folders: {total_files}")
# #
# # import os
# # from pathlib import Path
# # from collections import defaultdict
# #
# # # 配置结果目录路径
# # RESULTS_DIR = "/Users/mycp/Files/TemCon/Concurrency_Results"
# # # 关注的并发缺陷类型
# # CONCURRENCY_TYPES = ["atomicity violation", "data race", "order violation", "deadlock"]
# #
# #
# # def parse_result_file(file_path):
# #     """解析单个结果文件，提取并发缺陷统计"""
# #     type_counts = defaultdict(int)
# #
# #     with open(file_path, 'r', encoding='utf-8') as f:
# #         for line in f:
# #             line = line.strip()
# #             for concurrency_type in CONCURRENCY_TYPES:
# #                 if line.startswith(concurrency_type + ":"):
# #                     count = line.split(":")[1].strip()
# #                     try:
# #                         type_counts[concurrency_type] += int(count)
# #                     except ValueError:
# #                         continue
# #     return type_counts
# #
# #
# # def aggregate_results(directory):
# #     """汇总目录下所有结果文件的统计"""
# #     total_counts = defaultdict(int)
# #     processed_files = 0
# #
# #     # 遍历目录下所有txt文件
# #     for file_path in Path(directory).glob("*.txt"):
# #         if file_path.is_file():
# #             file_counts = parse_result_file(file_path)
# #             for concurrency_type, count in file_counts.items():
# #                 total_counts[concurrency_type] += count
# #             processed_files += 1
# #
# #     return total_counts, processed_files
# #
# #
# # def print_summary(total_counts, file_count):
# #     """打印汇总结果"""
# #     print("\nConcurrency Defect Summary Report")
# #     print("=" * 50)
# #     print(f"Analyzed {file_count} result files from: {RESULTS_DIR}\n")
# #
# #     # 按指定顺序打印每种类型的统计
# #     for concurrency_type in CONCURRENCY_TYPES:
# #         count = total_counts.get(concurrency_type, 0)
# #         print(f"{concurrency_type}: {count}")
# #
# #     # 计算并打印总计
# #     total = sum(total_counts.values())
# #     print("\n" + "=" * 50)
# #     print(f"TOTAL: {total}")
# #     print("=" * 50)
# #
# #
# # if __name__ == "__main__":
# #     # 汇总结果
# #     total_counts, file_count = aggregate_results(RESULTS_DIR)
# #
# #     # 打印汇总报告
# #     print_summary(total_counts, file_count)
#
#
# """
# 遍历目录中的.ql文件，检查是否包含'@kind path-problem'
# 不包含的则删除
# """
# # import os
# # import sys
# #
# #
# # def check_and_delete_ql_files(root_dir):
# #
# #     deleted_count = 0
# #     kept_count = 0
# #
# #     for root, _, files in os.walk(root_dir):
# #         for file in files:
# #             if file.endswith('.ql'):
# #                 file_path = os.path.join(root, file)
# #                 try:
# #                     with open(file_path, 'r', encoding='utf-8') as f:
# #                         content = f.read()
# #                         if '@kind path-problem' in content:
# #                             kept_count += 1
# #                             print(f'保留: {file_path}')
# #                         else:
# #                             os.remove(file_path)
# #                             deleted_count += 1
# #                             print(f'删除: {file_path}')
# #                 except UnicodeDecodeError:
# #                     try:
# #                         # 尝试其他编码
# #                         with open(file_path, 'r', encoding='latin-1') as f:
# #                             content = f.read()
# #                             if '@kind path-problem' in content:
# #                                 kept_count += 1
# #                                 print(f'保留: {file_path}')
# #                             else:
# #                                 os.remove(file_path)
# #                                 deleted_count += 1
# #                                 print(f'删除: {file_path}')
# #                     except Exception as e:
# #                         print(f'处理文件 {file_path} 时出错: {e}')
# #                 except Exception as e:
# #                     print(f'处理文件 {file_path} 时出错: {e}')
# #
# #     print(f'\n操作完成:')
# #     print(f'保留文件数: {kept_count}')
# #     print(f'删除文件数: {deleted_count}')
# #
# #
# # if __name__ == '__main__':
# #     target_dir = '/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src/Security/CWE-path-problem'
# #
# #     if not os.path.isdir(target_dir):
# #         print(f'错误: 目录 {target_dir} 不存在')
# #         sys.exit(1)
# #
# #     print(f'开始处理目录: {target_dir}')
# #     print('搜索包含"@kind path-problem"的.ql文件...')
# #
# #     check_and_delete_ql_files(target_dir)
#
#
# # import json
# # import csv
# # import os
# # from pathlib import Path
# # from collections import defaultdict
# #
# #
# # def count_functions_in_sarif(sarif_path, function_names):
# #     """统计sarif文件中每个function_name出现的次数"""
# #     counts = {name: 0 for name in function_names}
# #
# #     try:
# #         with open(sarif_path, 'r', encoding='utf-8') as f:
# #             data = json.load(f)
# #
# #         # 递归搜索JSON中的所有字符串
# #         def search_in_json(obj):
# #             if isinstance(obj, str):
# #                 for name in function_names:
# #                     if name in obj:
# #                         counts[name] += 1
# #             elif isinstance(obj, dict):
# #                 for value in obj.values():
# #                     search_in_json(value)
# #             elif isinstance(obj, list):
# #                 for item in obj:
# #                     search_in_json(item)
# #
# #         search_in_json(data)
# #     except Exception as e:
# #         print(f"Error processing {sarif_path}: {str(e)}")
# #
# #     return counts
# #
# #
# # def generate_summary_csv(directory, function_names, sort_by='function'):
# #     """
# #     生成汇总的summary.csv文件
# #     sort_by: 排序方式，可选 'function'(按函数名), 'total'(按总次数), 'max'(按最大次数)
# #     """
# #     summary_data = defaultdict(dict)
# #
# #     # 收集所有CSV文件的数据
# #     csv_dir = Path(directory)
# #     for csv_file in csv_dir.glob('*.csv'):
# #         # 跳过原始CSV和summary.csv
# #         if csv_file.name == "functions.csv" or csv_file.name == "summary.csv":
# #             continue
# #
# #         sarif_name = csv_file.stem  # 获取不带扩展名的文件名
# #         with open(csv_file, 'r', encoding='utf-8') as f:
# #             reader = csv.DictReader(f)
# #             for row in reader:
# #                 function_name = row['function_name']
# #                 count = int(row['is_present'])
# #                 summary_data[function_name][sarif_name] = count
# #
# #     # 确保所有函数在所有文件中都有记录
# #     for func in function_names:
# #         if func not in summary_data:
# #             summary_data[func] = {}
# #
# #     # 获取所有sarif文件名(作为列名)
# #     all_sarif_files = set()
# #     for func_data in summary_data.values():
# #         all_sarif_files.update(func_data.keys())
# #     all_sarif_files = sorted(all_sarif_files)
# #
# #     # 计算排序键
# #     sorted_functions = []
# #     if sort_by == 'function':
# #         sorted_functions = sorted(summary_data.keys())
# #     elif sort_by == 'total':
# #         # 按总出现次数排序
# #         sorted_functions = sorted(
# #             summary_data.keys(),
# #             key=lambda x: sum(summary_data[x].values()),
# #             reverse=True
# #         )
# #     elif sort_by == 'max':
# #         # 按最大出现次数排序
# #         sorted_functions = sorted(
# #             summary_data.keys(),
# #             key=lambda x: max(summary_data[x].values(), default=0),
# #             reverse=True
# #         )
# #     else:
# #         sorted_functions = sorted(summary_data.keys())
# #
# #     # 写入summary.csv
# #     summary_path = csv_dir / "summary.csv"
# #     with open(summary_path, 'w', encoding='utf-8', newline='') as f:
# #         writer = csv.writer(f)
# #         # 写入表头
# #         header = ['function_name'] + all_sarif_files + ['total', 'max']
# #         writer.writerow(header)
# #
# #         # 写入每行数据
# #         for func_name in sorted_functions:
# #             counts = summary_data[func_name]
# #             row = [func_name]
# #             total = 0
# #             max_count = 0
# #             for sarif_file in all_sarif_files:
# #                 count = counts.get(sarif_file, 0)
# #                 row.append(str(count))
# #                 total += count
# #                 if count > max_count:
# #                     max_count = count
# #             row.extend([str(total), str(max_count)])
# #             writer.writerow(row)
# #
# #     print(f"Summary file generated: {summary_path}")
# #     print(f"Sorted by: {sort_by}")
# #
# #
# # def process_sarif_files(directory, csv_path, sort_by='function'):
# #     """处理所有sarif文件"""
# #     # 读取原始CSV获取function_name列表
# #     function_names = []
# #     try:
# #         with open(csv_path, 'r', encoding='utf-8') as f:
# #             reader = csv.DictReader(f)
# #             for row in reader:
# #                 function_names.append(row['function_name'])
# #     except Exception as e:
# #         print(f"Error reading CSV file: {str(e)}")
# #         return
# #
# #     if not function_names:
# #         print("No function names found in CSV")
# #         return
# #
# #     # 遍历目录下的所有sarif文件
# #     sarif_dir = Path(directory)
# #     for sarif_file in sarif_dir.glob('*.sarif'):
# #         print(f"Processing {sarif_file.name}...")
# #         counts = count_functions_in_sarif(sarif_file, function_names)
# #
# #         # 生成对应的CSV文件
# #         output_csv = sarif_dir / f"{sarif_file.stem}.csv"
# #         with open(output_csv, 'w', encoding='utf-8', newline='') as f:
# #             writer = csv.writer(f)
# #             writer.writerow(['function_name', 'is_present'])
# #             for name, count in counts.items():
# #                 writer.writerow([name, count])
# #
# #         print(f"Generated {output_csv.name}")
# #
# #     # 生成汇总文件
# #     generate_summary_csv(directory, function_names, sort_by)
# #
# #
# # if __name__ == "__main__":
# #     directory = "/Users/mycp/CodeQL/7.13/imagemagick"
# #     csv_path = os.path.join(directory, "imagemagick.csv")  # 假设原始CSV名为functions.csv
# #
# #     # 可以选择排序方式: 'function'(默认), 'total', 'max'
# #     sort_method = 'total'  # 更改为你需要的排序方式
# #
# #     process_sarif_files(directory, csv_path, sort_method)
# #     print("All files processed.")
#
#
# import csv
#
#
# def print_qlpack_entries(csv_file_path):
#     """
#     从CSV文件中读取函数名，并直接打印QL pack格式的条目
#     """
#
#     # 读取CSV文件中的函数名
#     function_names = []
#     try:
#         with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
#             reader = csv.DictReader(csvfile)
#             if 'function_name' not in reader.fieldnames:
#                 print("错误：CSV文件中没有 'function_name' 列")
#                 return
#
#             for row in reader:
#                 if row['function_name'] and row['function_name'].strip():
#                     function_names.append(row['function_name'].strip())
#     except FileNotFoundError:
#         print(f"错误：找不到文件 {csv_file_path}")
#         return
#     except Exception as e:
#         print(f"读取CSV文件时出错: {e}")
#         return
#
#     if not function_names:
#         print("警告：没有找到任何函数名")
#         return
#
#     # 打印QL pack格式的内容
#     print("extensions:")
#     print("  - addsTo:")
#     print("      pack: codeql/cpp-all")
#     print("      extensible: summaryModel")
#     print("    data:")
#
#     for function_name in function_names:
#         print(f'      - ["", "", false, "{function_name}", "", "", "", "", "taint", "manual"]')
#
#
# # 使用示例
# if __name__ == "__main__":
#     csv_file = "data/groundtruths/imagemagick_functions_gt_all.csv"
#     print_qlpack_entries(csv_file)

from staticfg import CFGBuilder

# 构建 CFG
cfg = CFGBuilder().build_from_src('example.py', """
def foo(x):
    if x > 0:
        y = x * 2
        return y
    return 0
""")

# 生成 PDF 格式的 CFG 图
cfg.build_visual('exampleCFG', 'pdf')