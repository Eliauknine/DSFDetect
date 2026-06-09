import os
import csv
from codeql_templates import (
    SOURCE_TEMPLATE,
    SINK_TEMPLATE,
    Inter_procedural_TEMPLATE
)

def ensure_directory_exists(directory):
    """确保目录存在，如果不存在则创建"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_template_by_role(function_name, taint_role):
    """根据taint_role选择合适的模板"""
    template_map = {
        'Source': SOURCE_TEMPLATE,
        'Sink': SINK_TEMPLATE,
        'Inter_procedural_API': Inter_procedural_TEMPLATE
    }
    
    # 获取对应的模板
    if taint_role not in template_map:
        raise ValueError(f"Unsupported taint role: {taint_role}. Must be one of: Source, Sink, Inter_procedural_API")
    
    return template_map[taint_role].format(function_name=function_name)

def generate_query_file(function_name, taint_role, output_dir):
    """根据函数名和taint角色生成查询文件"""
    # 获取对应的查询内容
    query_content = get_template_by_role(function_name, taint_role)
    
    # 生成文件名
    filename = f"{function_name}_{taint_role}_analysis.ql"
    file_path = os.path.join(output_dir, filename)
    
    # 写入文件
    with open(file_path, 'w') as f:
        f.write(query_content)
    
    return file_path

def main():
    # 设置输入和输出路径
    csv_path = "data/results/stage1/filtered/imagemagic_taint_functions.csv"
    output_dir = "data/results/stage1/filtered/generated_queries"
    
    # 确保输出目录存在
    ensure_directory_exists(output_dir)
    
    # 读取CSV文件并生成查询
    generated_files = []
    
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            function_name = row['function_name']
            taint_role = row['taint_role']  # 保持原始大小写
            
            try:
                file_path = generate_query_file(function_name, taint_role, output_dir)
                generated_files.append(file_path)
                print(f"Generated query file for {function_name} with role {taint_role}:")
                print(f"  - {file_path}")
            except ValueError as e:
                print(f"Error processing {function_name}: {str(e)}")
                continue
    
    print(f"\nTotal generated files: {len(generated_files)}")

if __name__ == "__main__":
    main()