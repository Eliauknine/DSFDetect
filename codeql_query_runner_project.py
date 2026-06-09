import os
import subprocess
from pathlib import Path
from tqdm import tqdm

'''
/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src/Security/CWE/myquery/ql_source_sink_extract/libtiff
/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src/Security/CWE/myquery/ql_source_sink_extract/wolfssl
'''
class BatchCodeQLRunner:
    def __init__(self):
        # 基础路径配置
        self.codeql_cli = "/Users/mycp/CodeQL/codeql-cli/codeql/codeql"
        self.db_path = "/Users/mycp/CodeQL/databases/ImageMagick"
        self.queries_root = "/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src/Security/CWE-path-problem"
        self.output_root = "/Users/mycp/CodeQL/7.13/imagemagic_bqrs_csv"

        # 创建输出目录
        Path(self.output_root).mkdir(parents=True, exist_ok=True)

    def find_ql_files(self):
        """递归查找所有.ql查询文件"""
        ql_files = []
        for root, _, files in os.walk(self.queries_root):
            for file in files:
                if file.endswith('.ql'):
                    ql_files.append(os.path.join(root, file))
        return ql_files


    def generate_output_names(self, ql_path):
        """根据ql文件名生成输出文件名"""
        # 获取查询文件名（不带扩展名）
        query_name = Path(ql_path).stem

        return (
            os.path.join(self.output_root, f"{query_name}.bqrs"),
            os.path.join(self.output_root, f"{query_name}.csv")
        )

    def run_query(self, ql_path, bqrs_path, csv_path):
        """执行单个查询"""
        try:
            # 运行查询生成BQRS文件
            subprocess.run([
                self.codeql_cli, "query", "run",
                f"--database={self.db_path}",
                f"--output={bqrs_path}",
                ql_path
            ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # 转换BQRS为CSV
            subprocess.run([
                self.codeql_cli, "bqrs", "decode",
                bqrs_path,
                "--format=csv",
                f"--output={csv_path}"
            ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            return True, None

        except subprocess.CalledProcessError as e:
            error_msg = f"{Path(ql_path).name} - {e.stderr.decode().strip() if e.stderr else str(e)}"
            return False, error_msg

    def run_all_queries(self):
        """批量执行所有查询"""
        ql_files = self.find_ql_files()
        total = len(ql_files)
        success = 0
        failed_queries = []

        print(f"找到 {total} 个查询文件，开始执行...\n")

        # 使用tqdm创建进度条
        progress_bar = tqdm(ql_files, desc="执行进度", unit="query", dynamic_ncols=True)

        for ql_path in progress_bar:
            # 在进度条中显示当前处理的文件名
            progress_bar.set_postfix(file=Path(ql_path).name[:20] + "...")

            bqrs_path, csv_path = self.generate_output_names(ql_path)
            is_success, error_msg = self.run_query(ql_path, bqrs_path, csv_path)

            if is_success:
                success += 1
            else:
                failed_queries.append((Path(ql_path).name, error_msg))

        # 打印总结报告
        print("\n执行完成:")
        print(f"✓ 成功: {success}/{total}")
        print(f"✗ 失败: {len(failed_queries)}/{total}")

        if failed_queries:
            print("\n失败的查询:")
            for query, error in failed_queries:
                print(f"- {query}: {error}")


if __name__ == "__main__":
    runner = BatchCodeQLRunner()
    runner.run_all_queries()



# import os
# import subprocess
# from pathlib import Path
# from tqdm import tqdm
#
#
# class BatchCodeQLRunner:
#     def __init__(self):
#         # 基础路径配置
#         self.codeql_cli = "/Users/mycp/CodeQL/codeql-cli/codeql/codeql"
#         self.db_path = "/Users/mycp/CodeQL/databases/ImageMagick"
#         self.queries_root = "/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src/Security/CWE-path-problem"
#         self.output_root = "/Users/mycp/CodeQL/7.13/imagemagic"
#
#         # 创建输出目录
#         Path(self.output_root).mkdir(parents=True, exist_ok=True)
#
#     def find_ql_files(self):
#         """递归查找所有.ql查询文件"""
#         ql_files = []
#         for root, _, files in os.walk(self.queries_root):
#             for file in files:
#                 if file.endswith('.ql'):
#                     ql_files.append(os.path.join(root, file))
#         return ql_files
#
#     def generate_output_name(self, ql_path):
#         """根据ql文件名生成输出文件名，前缀加上所在目录名"""
#         ql_path_obj = Path(ql_path)
#         query_name = ql_path_obj.stem
#         parent_dir = ql_path_obj.parent.name  # 获取 .ql 所在的目录名
#         final_name = f"{parent_dir}__{query_name}.sarif"
#         return os.path.join(self.output_root, final_name)
#
#     def run_query(self, ql_path, sarif_path):
#         """执行单个查询并生成SARIF文件"""
#         try:
#             # 运行查询并直接生成SARIF文件
#             subprocess.run([
#                 self.codeql_cli, "database", "analyze",
#                 f"--format=sarif-latest",
#                 f"--output={sarif_path}",
#                 self.db_path,
#                 ql_path
#             ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
#             return True, None
#
#         except subprocess.CalledProcessError as e:
#             error_msg = f"{Path(ql_path).name} - {e.stderr.decode().strip() if e.stderr else str(e)}"
#             return False, error_msg
#
#     def run_all_queries(self):
#         """批量执行所有查询"""
#         ql_files = self.find_ql_files()
#         total = len(ql_files)
#         success = 0
#         failed_queries = []
#
#         print(f"找到 {total} 个查询文件，开始执行...\n")
#
#         # 使用tqdm创建进度条
#         progress_bar = tqdm(ql_files, desc="执行进度", unit="query", dynamic_ncols=True)
#
#         for ql_path in progress_bar:
#             # 在进度条中显示当前处理的文件名
#             progress_bar.set_postfix(file=Path(ql_path).name[:20] + "...")
#
#             sarif_path = self.generate_output_name(ql_path)
#             is_success, error_msg = self.run_query(ql_path, sarif_path)
#
#             if is_success:
#                 success += 1
#             else:
#                 failed_queries.append((Path(ql_path).name, error_msg))
#
#         # 打印总结报告
#         print("\n执行完成:")
#         print(f"✓ 成功: {success}/{total}")
#         print(f"✗ 失败: {len(failed_queries)}/{total}")
#
#         if failed_queries:
#             print("\n失败的查询:")
#             for query, error in failed_queries:
#                 print(f"- {query}: {error}")
#
#
# if __name__ == "__main__":
#     runner = BatchCodeQLRunner()
#     runner.run_all_queries()