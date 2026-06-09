import os
import csv
import re


def clean_text(text):
    """
    清理文本内容：
    1. 删除所有file://开头的文件路径
    2. 删除Source Comment:及其后内容
    3. 删除Source Location:及其后内容
    4. 清理多余空格
    """
    if not isinstance(text, str):
        return ""

    # 执行所有清理操作
    text = re.sub(r'file://[^\s]+', '', text)
    text = re.sub(r'Source Comment:[^\n]*', '', text)
    text = re.sub(r'Source Location:[^\n]*', '', text)
    text = re.sub(r'Sink Comment:[^\n]*', '', text)
    text = re.sub(r'Sink Location:[^\n]*', '', text)
    text = re.sub(r'\s+', ' ', text).strip()  # 合并多个空格

    return text


def process_csv_file(filepath):
    """
    处理单个CSV文件：
    1. 读取内容并清理col2列
    2. 删除空行和重复行
    3. 如果文件为空或只有表头则删除
    """
    try:
        # 读取CSV文件内容
        rows = []
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:  # 跳过空行
                    rows.append(row)

        # 检查文件是否有效
        if len(rows) <= 1:  # 只有表头或空文件
            os.remove(filepath)
            print(f"删除空文件: {os.path.basename(filepath)}")
            return False

        # 处理col2列（假设是第三列）
        cleaned_rows = []
        seen_texts = set()

        for row in rows:
            if len(row) >= 3:  # 确保有col2列
                cleaned_col2 = clean_text(row[2])
                if cleaned_col2 and cleaned_col2 not in seen_texts:  # 去重
                    seen_texts.add(cleaned_col2)
                    row[2] = cleaned_col2
                    cleaned_rows.append(row)

        # 检查处理后是否还有有效数据
        if len(cleaned_rows) <= 1:  # 只有表头或数据全被清理
            os.remove(filepath)
            print(f"删除无效数据文件: {os.path.basename(filepath)}")
            return False

        # 写回原文件
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(cleaned_rows)

        print(f"成功处理: {os.path.basename(filepath)}")
        return True

    except Exception as e:
        print(f"处理文件 {filepath} 时出错: {str(e)}")
        return False


def process_directory(directory):
    """
    处理目录下所有CSV文件
    """
    if not os.path.isdir(directory):
        print(f"目录不存在: {directory}")
        return

    processed_count = 0
    deleted_count = 0

    for filename in os.listdir(directory):
        if filename.lower().endswith('.csv'):
            filepath = os.path.join(directory, filename)
            if process_csv_file(filepath):
                processed_count += 1
            else:
                deleted_count += 1

    print(f"\n处理完成！共处理 {processed_count} 个文件，删除 {deleted_count} 个文件")


def check_file_content(filepath):
    """
    检查CSV文件是否同时包含Upstream和Downstream开头的行
    返回: True(保留) / False(删除)
    """
    has_upstream = False
    has_downstream = False

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 3:  # 确保有col2列
                    col2 = row[2]
                    if col2.startswith('Upstream'):
                        has_upstream = True
                    elif col2.startswith('Downstream'):
                        has_downstream = True

                    # 如果两者都已找到，提前终止检查
                    if has_upstream and has_downstream:
                        return True

        # 检查结果
        return has_upstream and has_downstream

    except Exception as e:
        print(f"检查文件 {os.path.basename(filepath)} 时出错: {str(e)}")
        return False


def process_directory2(directory):
    """
    处理目录下所有_find_source_sink.csv文件
    """
    if not os.path.isdir(directory):
        print(f"目录不存在: {directory}")
        return

    kept_count = 0
    deleted_count = 0

    for filename in os.listdir(directory):
        if filename.endswith('_find_source_sink.csv'):
            filepath = os.path.join(directory, filename)

            if check_file_content(filepath):
                kept_count += 1
                print(f"保留文件: {filename} (包含Upstream和Downstream)")
            else:
                os.remove(filepath)
                deleted_count += 1
                print(f"删除文件: {filename} (缺少Upstream或Downstream)")

    print(f"\n处理完成！共保留 {kept_count} 个文件，删除 {deleted_count} 个文件")

'''
R2/myquery/ql_source_sink_extract/result/libraw
R2/myquery/ql_source_sink_extract/result/libtiff
R2/myquery/ql_source_sink_extract/result/wolfssl
'''

if __name__ == '__main__':
    target_dir = 'R2/myquery/ql_source_sink_extract/result/wolfssl'
    process_directory(target_dir)
    process_directory2(target_dir)