import json
import os

def remove_duplicates_and_modify_json(file_name):
    # 获取文件路径
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    
    try:
        # 读取JSON文件
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 使用字典进行去重，键为function_name和data的组合
        unique_data = {}
        for item in data:
            if 'function_name' in item and 'data' in item:
                # 将data转换为元组，因为列表不能作为字典的键
                key = (item['function_name'], tuple(item['data']))
                unique_data[key] = item
        
        # 转换回列表
        deduplicated_data = list(unique_data.values())
        
        # 修改第8个值为taint
        for item in deduplicated_data:
            if len(item['data']) > 8:
                item['data'][7] = "taint"
        
        # 将去重和修改后的数据写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(deduplicated_data, f, ensure_ascii=False, indent=2)
        
        original_count = len(data)
        new_count = len(deduplicated_data)
        removed_count = original_count - new_count
        print(f"处理文件 {file_name}:")
        print(f"  - 原始数据条数: {original_count}")
        print(f"  - 去重后条数: {new_count}")
        print(f"  - 删除重复条数: {removed_count}")
        
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
    except json.JSONDecodeError:
        print(f"错误：文件 {file_name} 的JSON格式不正确")
    except Exception as e:
        print(f"处理文件 {file_name} 时发生错误：{str(e)}")

def process_all_files():
    files_to_process = [
        'sink_model_info_extract_gpt.json',
        'source_model_info_extract_gpt.json',
        'summary_model_info_extract_gpt.json'
    ]
    
    print("开始处理文件...")
    for file_name in files_to_process:
        remove_duplicates_and_modify_json(file_name)
    print("所有文件处理完成！")

if __name__ == "__main__":
    process_all_files() 