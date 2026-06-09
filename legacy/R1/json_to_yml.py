import json
import yaml
import os

def load_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"读取文件 {file_path} 时发生错误：{str(e)}")
        return []

def create_yaml_structure():
    return {
        'extensions': [
            {
                'addsTo': {
                    'pack': 'codeql/cpp-all',
                    'extensible': 'sourceModel'
                },
                'data': []
            },
            {
                'addsTo': {
                    'pack': 'codeql/cpp-all',
                    'extensible': 'sinkModel'
                },
                'data': []
            },
            {
                'addsTo': {
                    'pack': 'codeql/cpp-all',
                    'extensible': 'summaryModel'
                },
                'data': []
            }
        ]
    }

def format_data_as_string(data):
    # 确保所有元素都是字符串形式
    formatted_items = []
    for item in data:
        if isinstance(item, bool):
            formatted_items.append(str(item).lower())
        else:
            formatted_items.append(f'"{str(item)}"' if str(item) != "false" else "false")
    return f'[{", ".join(formatted_items)}]'

def process_json_files():
    # 文件映射关系
    file_mapping = {
        'source_model_info_extract_gpt.json': 'sourceModel',
        'sink_model_info_extract_gpt.json': 'sinkModel',
        'summary_model_info_extract_gpt.json': 'summaryModel'
    }
    
    # 创建YAML结构
    yaml_data = create_yaml_structure()
    
    # 处理每个JSON文件
    for json_file, model_type in file_mapping.items():
        file_path = os.path.join(os.path.dirname(__file__), json_file)
        json_data = load_json_file(file_path)
        
        # 找到对应的YAML部分
        yaml_section = next(
            ext for ext in yaml_data['extensions'] 
            if ext['addsTo']['extensible'] == model_type
        )
        
        # 提取并格式化数据
        formatted_data = []
        for item in json_data:
            if 'data' in item:
                formatted_data.append(format_data_as_string(item['data']))
        
        # 直接写入格式化的字符串
        yaml_section['data'] = formatted_data
        
        print(f"处理文件 {json_file}:")
        print(f"  - 添加了 {len(json_data)} 条数据到 {model_type}")
    
    # 生成YAML内容
    yaml_content = "extensions:\n"
    for ext in yaml_data['extensions']:
        yaml_content += "  - addsTo:\n"
        yaml_content += f"      pack: {ext['addsTo']['pack']}\n"
        yaml_content += f"      extensible: {ext['addsTo']['extensible']}\n"
        yaml_content += "    data:\n"
        for data_item in ext['data']:
            yaml_content += f"      - {data_item}\n"
    
    # 写入YAML文件
    output_file = os.path.join(os.path.dirname(__file__), 'custom-models.yml')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(yaml_content)
    
    print("\n生成的YAML文件已保存为 custom-models.yml")

if __name__ == "__main__":
    process_json_files() 