'''处理_find_source_sink.csv结尾的CSV文件的source、sink信息'''
import os
import pandas as pd


def process_csv_files(directory):
    """
    处理指定目录下以_find_source_sink.csv结尾的CSV文件
    """
    # 遍历目录下的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('_find_source_sink.csv'):
                file_path = os.path.join(root, file)
                print(f"正在处理文件: {file_path}")

                try:
                    # 读取CSV文件
                    df = pd.read_csv(file_path)

                    # 原始行数
                    original_rows = len(df)

                    # 条件1: 删除source_text以Upstream开头且taint_role为Sink的行
                    condition1 = (df['source_text'].str.split().str[0] == 'Upstream') & (df['taint_role'] == 'Sink')

                    # 条件2: 删除source_text以Downstream开头且taint_role为Source的行
                    condition2 = (df['source_text'].str.split().str[0] == 'Downstream') & (df['taint_role'] == 'Source')

                    # 组合条件
                    combined_condition = condition1 | condition2

                    # 删除符合条件的行
                    df = df[~combined_condition]

                    # 保存处理后的文件（覆盖原文件）
                    df.to_csv(file_path, index=False)

                    # 打印处理结果
                    removed_rows = original_rows - len(df)
                    print(f"处理完成: 移除了 {removed_rows} 行，剩余 {len(df)} 行")

                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {str(e)}")


if __name__ == "__main__":
    target_directory = "R2/myquery/ql_source_sink_extract/result/result_specification_extract_gpt/imagemagic"

    if not os.path.exists(target_directory):
        print(f"错误: 目录 {target_directory} 不存在")
    else:
        process_csv_files(target_directory)
        print("所有文件处理完成")


'''对'function_name', 'taint_role', 'arg_pos'进行去重操作'''
import os
import pandas as pd


def deduplicate_csv_files(directory):
    """
    对指定目录下所有CSV文件按指定列进行去重
    """
    processed_files = 0
    total_duplicates_removed = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.csv'):
                file_path = os.path.join(root, file)
                print(f"正在处理文件: {file_path}")

                try:
                    # 读取CSV文件
                    df = pd.read_csv(file_path)

                    # 原始行数
                    original_rows = len(df)

                    # 检查是否包含所需的列
                    required_columns = ['function_name', 'taint_role', 'arg_pos']
                    if not all(col in df.columns for col in required_columns):
                        print(f"警告: 文件 {file} 缺少所需列，跳过处理")
                        continue

                    # 按指定列去重（保留第一个出现的记录）
                    df_dedup = df.drop_duplicates(subset=required_columns, keep='first')

                    # 计算移除的重复行数
                    duplicates_removed = original_rows - len(df_dedup)
                    total_duplicates_removed += duplicates_removed

                    # 保存处理后的文件（覆盖原文件）
                    df_dedup.to_csv(file_path, index=False)

                    # 打印处理结果
                    print(f"处理完成: 移除了 {duplicates_removed} 个重复行，剩余 {len(df_dedup)} 行")
                    processed_files += 1

                except Exception as e:
                    print(f"处理文件 {file} 时出错: {str(e)}")

    print(f"\n处理完成: 共处理 {processed_files} 个文件，移除了总计 {total_duplicates_removed} 个重复行")


if __name__ == "__main__":
    target_directory = "R2/myquery/ql_source_sink_extract/result/result_specification_extract_gpt/imagemagic"

    if not os.path.exists(target_directory):
        print(f"错误: 目录 {target_directory} 不存在")
    else:
        deduplicate_csv_files(target_directory)