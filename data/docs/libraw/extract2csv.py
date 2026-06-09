import csv
import os
from doc_extract import extract_sections


def process_markdown_to_csv(input_md, output_csv):
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    # 提取目标层级内容
    sections = extract_sections(input_md, target_level=1)

    # 判断文件是否存在以决定写入模式
    file_exists = os.path.exists(output_csv)

    with open(output_csv, 'a', newline='', encoding='utf-8') as f:  # 使用'a'模式追加
        writer = csv.writer(f)

        # 如果文件不存在，写入标题行
        if not file_exists:
            writer.writerow(['content'])

        # 写入新内容
        for section in sections:
            escaped = section.replace('"', '""')
            writer.writerow([f'"{escaped}"'])

    print(f"内容已{'追加到' if file_exists else '保存到'}：{output_csv}")


if __name__ == '__main__':
    # 可替换的输入文件路径
    input_md = 'DSFDetectData/libraw_doc/API-overview-eng.md'  # 替换为您需要的md文件
    output_csv = 'data/input_docs/libraw_doc_input.csv'  # 固定输出路径

    process_markdown_to_csv(input_md, output_csv)