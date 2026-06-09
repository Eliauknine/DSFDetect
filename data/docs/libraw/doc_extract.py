import re


def extract_sections(file_path, target_level):
    """
    提取Markdown文档中指定层级标题及其所有子级内容

    更新说明：
    现在会保留目标层级下的所有子级标题结构

    参数：
        file_path (str): Markdown文件路径
        target_level (int): 要提取的标题层级（1-6）

    返回：
        list: 包含完整子级结构的区块列表
    """
    sections = []
    current_section = []
    in_target_section = False  # 更明确的变量名

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            stripped_line = line.rstrip('\n')

            # 标题行检测
            if (match := re.match(r'^(#+)\s+', stripped_line)):
                current_level = len(match.group(1))

                if in_target_section:
                    if current_level <= target_level:
                        # 结束当前区块
                        sections.append('\n'.join(current_section))
                        current_section = []
                        in_target_section = False

                        # 处理新标题 (可能同级)
                        if current_level == target_level:
                            current_section.append(stripped_line)
                            in_target_section = True
                    else:
                        # 子级标题，保留完整结构
                        current_section.append(stripped_line)
                else:
                    if current_level == target_level:
                        current_section.append(stripped_line)
                        in_target_section = True
            else:
                if in_target_section:
                    current_section.append(stripped_line)

        # 处理文件末尾的最后一个区块
        if in_target_section:
            sections.append('\n'.join(current_section))

    return sections


if __name__ == '__main__':
    sections = extract_sections('DSFDetectData/libraw_doc/API-CXX-eng.md', 3)
    for i, sec in enumerate(sections, 1):
        print(f"完整区块 {i}:")
        print(sec)
        print('-' * 40)