import json
import csv
import os
import glob

def load_function_names(csv_path):
    """加载CSV文件中的函数名和对应的行信息"""
    function_data = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 使用函数名和文件名的组合作为键
            key = (row['function_name'], row['file_name'])
            function_data[key] = row
    return function_data

def process_sarif_file(sarif_path, function_data):
    """处理单个sarif文件并返回匹配的函数信息"""
    matched_functions = []
    
    try:
        with open(sarif_path, 'r', encoding='utf-8') as f:
            sarif_content = json.load(f)
            
        # 检查sarif文件的结构
        if 'runs' in sarif_content:
            for run in sarif_content['runs']:
                if 'results' in run:
                    for result in run['results']:
                        # 获取结果中的所有文本内容
                        result_text = json.dumps(result)
                        
                        # 检查每个函数名和文件名组合
                        for (func_name, file_name), func_info in function_data.items():
                            # 只有当函数名和文件名都匹配时才添加到结果中
                            if func_name and file_name and func_name in result_text and file_name in result_text:
                                if func_info not in matched_functions:
                                    matched_functions.append(func_info)
                                    print(f"    匹配到: 函数 {func_name} 在文件 {file_name} 中")
    
    except Exception as e:
        print(f"处理文件 {sarif_path} 时发生错误: {str(e)}")
    
    return matched_functions

def main():
    # 设置路径
    csv_path = "/Users/mycp/PycharmProjects/pythonProject/DSFDetect/data/groundtruths/imagemagick_functions_gt.csv"
    sarif_dir = "/Users/mycp/CodeQL/7.13/imagemagic"  # sarif文件所在目录
    output_dir = os.path.join(os.path.dirname(__file__), "sarif_results")
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 加载函数名数据
    print("正在加载函数名数据...")
    function_data = load_function_names(csv_path)
    print(f"已加载 {len(function_data)} 个函数名和文件名组合")
    
    # 获取所有sarif文件
    sarif_files = glob.glob(os.path.join(sarif_dir, "*.sarif"))
    print(f"找到 {len(sarif_files)} 个sarif文件")
    
    # 处理每个sarif文件
    for sarif_path in sarif_files:
        print(f"\n处理文件: {os.path.basename(sarif_path)}")
        
        # 处理sarif文件
        matched_functions = process_sarif_file(sarif_path, function_data)
        
        # 生成输出文件名
        output_filename = os.path.splitext(os.path.basename(sarif_path))[0] + ".csv"
        output_path = os.path.join(output_dir, output_filename)
        
        # 写入结果
        if matched_functions:
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                if matched_functions:
                    writer = csv.DictWriter(f, fieldnames=matched_functions[0].keys())
                    writer.writeheader()
                    writer.writerows(matched_functions)
            print(f"找到 {len(matched_functions)} 个匹配的函数，结果已保存到: {output_filename}")
        else:
            print(f"未找到匹配的函数")

if __name__ == "__main__":
    main() 