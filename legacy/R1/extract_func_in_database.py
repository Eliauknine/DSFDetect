import pandas as pd


def remove_duplicates_and_filter(input_file, output_file, groundtruth_file):
    # 1. 读取原始CSV文件并去重
    df = pd.read_csv(input_file)
    df_deduplicated = df.drop_duplicates(subset=['function_name', 'taint_role'], keep='first')

    # 2. 读取groundtruth文件
    try:
        df_gt = pd.read_csv(groundtruth_file)
        gt_functions = set(df_gt['function_name'].unique())
    except Exception as e:
        print(f"读取groundtruth文件失败: {e}")
        return

    # 3. 过滤数据，只保留在groundtruth中存在的function_name
    df_filtered = df_deduplicated[df_deduplicated['function_name'].isin(gt_functions)]

    # 4. 保存结果
    df_filtered.to_csv(output_file, index=False)
    print(f"处理完成，结果已保存到 {output_file}")
    print(f"原始记录数: {len(df)}, 去重后: {len(df_deduplicated)}, 过滤后: {len(df_filtered)}")


# 使用示例
'''
data/results/stage1/libraw
data/results/stage1/libtiff
data/results/stage1/wolfssl
'''
input_csv = "data/results/stage1/wolfssl/vulnerable_functions_summary.csv"
output_csv = "data/results/stage1/filtered/wolfssl_taint_functions.csv"
groundtruth_file = "data/groundtruths/wolfssl_functions_gt_all.csv"

remove_duplicates_and_filter(input_csv, output_csv, groundtruth_file)