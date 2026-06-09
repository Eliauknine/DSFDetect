'''yml生成'''
import csv
from codeql_queries import SourceModel, SinkModel, SummaryModel

# 定义路径
csv_path = "/Users/mycp/PycharmProjects/pythonProject/DSFDetect/data/results/stage1/filtered/imagemagic_taint_functions.csv"
output_yml_path = "/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src/Mymodels/config/models/custom-models1.yml"


def generate_yaml_from_templates():
    yaml_content = "extensions:\n"

    with open(csv_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if 'function_name' not in row or 'taint_role' not in row:
                print(f"Warning: Missing required columns in CSV row: {row}")
                continue

            function_name = row['function_name']
            taint_role = row['taint_role']

            if taint_role == "Source":
                yaml_content += SourceModel.format(function_name=function_name) + "\n"
            elif taint_role == "Sink":
                yaml_content += SinkModel.format(function_name=function_name) + "\n"
            elif taint_role == "Inter_procedural_API":
                yaml_content += SummaryModel.format(function_name=function_name) + "\n"

    return yaml_content


def write_yaml_file(content, file_path):
    with open(file_path, 'w') as yml_file:
        yml_file.write(content)
    print(f"YAML文件已成功生成: {file_path}")


if __name__ == "__main__":
    # 注意：需要确保codeql_queries.py中的模板格式正确
    # 特别是SinkModel模板中的格式问题（pack: codeql / cpp - all 应该改为 pack: codeql/cpp-all）
    yaml_content = generate_yaml_from_templates()
    write_yaml_file(yaml_content, output_yml_path)