# def process_line(line, current_extensible):
#     stripped = line.strip()
#
#     if stripped.startswith("- ["):
#         # 去掉前缀 "- [" 和结尾 "]"
#         content = stripped[len("- ["):-1]
#
#         # 手动解析列表项，避免 split(",") 错误分割带逗号的字符串
#         parts = []
#         current_part = []
#         in_quotes = False
#         for char in content:
#             if char == '"':
#                 in_quotes = not in_quotes
#             if char == ',' and not in_quotes:
#                 parts.append(''.join(current_part).strip())
#                 current_part = []
#             else:
#                 current_part.append(char)
#         if current_part:  # 添加最后一个部分
#             parts.append(''.join(current_part).strip())
#
#         if len(parts) >= 3:
#             if current_extensible == "sourceModel":
#                 parts[-3] = '""'
#                 parts[-2] = '"local"'
#             elif current_extensible == "sinkModel":
#                 parts[-3] = '""'
#                 parts[-2] = '"remote-sink"'
#             elif current_extensible == "summaryModel":
#                 if len(parts) >= 4:
#                     parts[-2] = '"taint"'
#                     parts[-3] = '""'
#                     parts[-4] = '""'
#                 elif len(parts) >= 3:
#                     parts[-2] = '""'
#                     parts[-3] = '""'
#
#             # 处理 Argument[...] 的情况（即使引号不完整）
#             for i in range(len(parts)):
#                 if 'Argument[' in parts[i]:
#                     parts[i] = '""'
#
#             return "      - [" + ", ".join(parts) + "]\n"
#
#     return line
def process_line(line, current_extensible):
    """
    根据当前 extensible 类型处理数据行：
    - sourceModel: 将倒数第二项替换为 "remote"
    - sinkModel: 将倒数第二项替换为 "remote-sink"
    - summaryModel: 将倒数第三项替换为 "ReturnValue"
    """
    stripped = line.strip()

    if stripped.startswith("- ["):
        # 去掉前缀 "- [" 和结尾 "]"
        content = stripped[len("- ["):-1]
        parts = [p.strip() for p in content.split(",")]

        if len(parts) >= 3:
            if current_extensible == "sourceModel":
                # parts[-3] = '""'
                if parts[-2].strip('"') == "local":
                    parts[-2] = '"remote"'
            # elif current_extensible == "sinkModel":
            #     parts[-3] = '""'
            #     # if parts[-2].strip('"') == "taint":
            #     #     parts[-2] = '"remote-sink"'
            # elif current_extensible == "summaryModel":
            #     parts[-2] = '""'
            #     parts[-3] = '""'
            #     parts[-4] = '""'

            return "      - [" + ", ".join(parts) + "]\n"

    return line


def main():
    input_file = "config/models/imagemagick_source.yml"
    output_file = "config/models/imagemagick_source.modified.yml"

    current_extensible = None

    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        for line in f_in:
            stripped = line.strip()

            if stripped.startswith("extensible:"):
                if "sourceModel" in stripped:
                    current_extensible = "sourceModel"
                elif "sinkModel" in stripped:
                    current_extensible = "sinkModel"
                elif "summaryModel" in stripped:
                    current_extensible = "summaryModel"
                else:
                    current_extensible = None

            modified_line = process_line(line, current_extensible)
            f_out.write(modified_line)

    print(f"✅ 修改完成，输出文件：{output_file}")


if __name__ == "__main__":
    main()
