import csv
import os

# 输入文件路径
input_csv = '/Users/mycp/PycharmProjects/pythonProject/DSFDetect/data/results/stage1/log/wolfssl/vulnerable_functions_summary.csv'
# 输出文件路径
output_txt = '/Users/mycp/PycharmProjects/pythonProject/DSFDetect/data/function_names/wolfssl_func_name.txt'

# 确保输出目录存在
os.makedirs(os.path.dirname(output_txt), exist_ok=True)

try:
    # 读取CSV文件
    with open(input_csv, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # 提取所有function_name
        function_names = [row['function_name'] for row in csv_reader if 'function_name' in row]

    # 写入文本文件（追加模式 'a'）
    with open(output_txt, mode='a', encoding='utf-8') as txt_file:
        txt_file.write('\n'.join(function_names) + '\n')  # 加换行符避免粘连

    print(f"成功追加 {len(function_names)} 个函数名到 {output_txt}")

except FileNotFoundError:
    print(f"错误：文件 {input_csv} 未找到")
except Exception as e:
    print(f"发生错误: {str(e)}")

'''去重'''
# 输入/输出文件路径（相同文件）
file_path = '/Users/mycp/PycharmProjects/pythonProject/DSFDetect/data/function_names/wolfssl_func_name.txt'

try:
    # 1. 读取所有函数名
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()  # 按行读取，去除末尾换行符

    # 2. 去重（使用 set 自动去重）
    unique_lines = sorted(set(lines))  # 去重并排序（可选）

    # 3. 重新写入文件（覆盖模式 'w'）
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(unique_lines) + '\n')  # 换行符保证格式

    print(f"去重完成！原 {len(lines)} 行 → 去重后 {len(unique_lines)} 行")

except FileNotFoundError:
    print(f"错误：文件 {file_path} 不存在！")
except Exception as e:
    print(f"发生错误: {str(e)}")

import pandas as pd


def find_matching_functions():
    # 文件路径
    txt_path = 'data/function_names/wolfssl_func_name.txt'
    csv_path = 'data/groundtruths/wolfssl_functions_gt_all.csv'
    output_path = 'data/function_names/wolfssl_func_name_final.txt'

    try:
        # 1. 读取txt文件中的函数名
        with open(txt_path, 'r', encoding='utf-8') as f:
            txt_functions = set(line.strip() for line in f if line.strip())

        print(f"从 {txt_path} 中读取到 {len(txt_functions)} 个函数名")

        # 2. 读取csv文件中的函数名
        df = pd.read_csv(csv_path)
        if 'function_name' not in df.columns:
            print(f"错误：{csv_path} 中没有 'function_name' 列")
            return

        csv_functions = set(df['function_name'].dropna().unique())
        print(f"从 {csv_path} 中读取到 {len(csv_functions)} 个唯一函数名")

        # 3. 查找匹配的函数名
        matched_functions = sorted(txt_functions & csv_functions)
        print(f"找到 {len(matched_functions)} 个匹配的函数名")

        # 4. 将匹配的函数名写入新文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(matched_functions) + '\n')

        print(f"匹配的函数名已保存到 {output_path}")

        # 5. 打印未找到的函数名（可选）
        unmatched = txt_functions - csv_functions
        if unmatched:
            print(f"\n未找到 {len(unmatched)} 个函数名:")
            for func in sorted(unmatched):
                print(f"- {func}")

    except FileNotFoundError as e:
        print(f"文件未找到: {str(e)}")
    except Exception as e:
        print(f"发生错误: {str(e)}")


if __name__ == '__main__':
    find_matching_functions()