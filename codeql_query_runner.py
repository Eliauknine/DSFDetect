# import os
# import subprocess
# from pathlib import Path
#
# class SimpleCodeQLRunner:
#     def __init__(self):
#         # 路径根据实际情况修改
#         self.codeql_cli = "/Users/mycp/CodeQL/codeql-cli/codeql/codeql"
#         self.db_path = "/Users/mycp/CodeQL/databases/ImageMagick"
#         self.query_path = "/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src/Security/CWE/AcquireQuantumMemory_source_sink_path.ql"
#
#         # 结果输出目录
#         self.output_dir = "/Users/mycp/CodeQL/result/test"
#         Path(self.output_dir).mkdir(parents=True, exist_ok=True)
#
#         # 结果文件路径
#         self.bqrs_path = os.path.join(self.output_dir, "results2.bqrs")
#         self.csv_path = os.path.join(self.output_dir, "results2.csv")
#         self.sarif_path = os.path.join(self.output_dir, "results2.sarif")
#
#     def run_query(self):
#         """执行查询并强制重新生成结果"""
#         try:
#             # 1. 强制生成SARIF（使用database analyze）
#             subprocess.run([
#                 self.codeql_cli, "database", "analyze",
#                 self.db_path,
#                 self.query_path,
#                 "--format=sarif-latest",
#                 f"--output={self.sarif_path}",
#                 "--rerun"  # 强制重新分析
#             ], check=True)
#
#             # 2. 强制生成BQRS（使用query run）
#             subprocess.run([
#                 self.codeql_cli, "query", "run",
#                 f"--database={self.db_path}",
#                 f"--output={self.bqrs_path}",
#                 "--no-precompiled-imports",
#                 "--rerun",
#                 self.query_path
#             ], check=True)
#
#             # 3. 转换BQRS为CSV
#             subprocess.run([
#                 self.codeql_cli, "bqrs", "decode",
#                 self.bqrs_path,
#                 "--format=csv",
#                 f"--output={self.csv_path}"
#             ], check=True)
#
#             print(f"结果已保存至:\nSARIF: {self.sarif_path}\nCSV: {self.csv_path}")
#             return True
#
#         except subprocess.CalledProcessError as e:
#             print(f"执行失败: {e}")
#             return False
#
# if __name__ == "__main__":
#     runner = SimpleCodeQLRunner()
#     success = runner.run_query()
#     if not success:
#         exit(1)


# import os
# import subprocess
# from pathlib import Path
#
#
# class SimpleCodeQLRunner:
#     def __init__(self):
#         # 硬编码路径（根据你的实际路径修改）
#         self.codeql_cli = "/Users/mycp/CodeQL/codeql-cli/codeql/codeql"
#         self.db_path = "/Users/mycp/CodeQL/databases/ImageMagick"
#         self.query_path = "/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src/codeql-suites/cpp-lgtm.qls"
#
#
#         # 结果输出目录
#         self.output_dir = "/Users/mycp/CodeQL/result/test"
#         Path(self.output_dir).mkdir(parents=True, exist_ok=True)
#
#         # 结果文件路径
#         self.bqrs_path = os.path.join(self.output_dir, "results2.bqrs")
#         self.csv_path = os.path.join(self.output_dir, "results2.csv")
#
#     def run_query(self):
#         """执行CodeQL查询并生成CSV结果"""
#         try:
#             # 先清理缓存并重新分析
#             # subprocess.run([
#             #     self.codeql_cli, "database", "cleanup",
#             #     "--mode=brutal",  # 强制清理所有缓存
#             #     self.db_path
#             # ], check=True)
#
#             # 1. 运行查询生成BQRS文件
#             subprocess.run([
#                 self.codeql_cli, "query", "run",
#                 f"--database={self.db_path}",
#                 f"--output={self.bqrs_path}",
#                 self.query_path
#             ], check=True)
#
#             # 2. 转换BQRS为CSV
#             subprocess.run([
#                 self.codeql_cli, "bqrs", "decode",
#                 self.bqrs_path,
#                 "--format=csv",
#                 f"--output={self.csv_path}"
#             ], check=True)
#
#             print(f"查询成功完成！结果已保存至: {self.csv_path}")
#             return True
#
#         except subprocess.CalledProcessError as e:
#             print(f"执行失败: {e}")
#             return False
#
#
# if __name__ == "__main__":
#     runner = SimpleCodeQLRunner()
#     success = runner.run_query()
#     if not success:
#         exit(1)

import os
import subprocess
from pathlib import Path


class SimpleCodeQLRunner:
    def __init__(self):
        # 硬编码路径（根据你的实际路径修改）
        self.codeql_cli = "/Users/mycp/CodeQL/codeql-cli/codeql/codeql"
        self.db_path = "/Users/mycp/CodeQL/databases/ImageMagick"
        self.query_path = "/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src/codeql-suites/cpp-lgtm.qls"

        # 结果输出目录
        self.output_dir = "/Users/mycp/CodeQL/result/test"
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

        # SARIF 结果文件路径
        self.sarif_path = os.path.join(self.output_dir, "results1.sarif")

    def run_query(self):
        """执行CodeQL查询并直接生成SARIF结果"""
        try:
            # 先安装关联 Pack 的依赖
            # subprocess.run([
            #     self.codeql_cli, "pack", "install",
            #     str(Path(self.db_path).parent)  # 假设 .qlpack.yml 在数据库同级目录中
            # ], check=True)

            # 直接运行查询并生成SARIF文件
            subprocess.run([
                self.codeql_cli, "database", "analyze",
                f"--format=sarif-latest",
                f"--additional-packs=/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src/Mymodels",
                f"--model-packs=my-models/my-cpp-model-pack",
                f"--output={self.sarif_path}",
                # f"--search-path=/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src",
                f"--rerun",  # 添加这个参数强制重新运行所有查询
                self.db_path,
                self.query_path
            ], check=True)

            print(f"查询成功完成！SARIF结果已保存至: {self.sarif_path}")
            return True

        except subprocess.CalledProcessError as e:
            print(f"执行失败: {e}")
            return False

    # def run_query(self):
    #     """执行CodeQL查询并直接生成SARIF结果（带详细日志检查）"""
    #     try:
    #         # 运行命令并捕获输出
    #         result = subprocess.run(
    #             [
    #                 self.codeql_cli, "database", "analyze",
    #                 "--format=sarif-latest",
    #                 "--external=model=/Users/mycp/.../config/models/custom-models1.yml",
    #                 f"--output={self.sarif_path}",
    #                 "--rerun",
    #                 "--verbose",  # 添加详细日志
    #                 self.db_path,
    #                 self.query_path
    #             ],
    #             check=True,
    #             stdout=subprocess.PIPE,  # 捕获标准输出
    #             stderr=subprocess.STDOUT,  # 将标准错误重定向到标准输出
    #             text=True  # 输出为文本格式
    #         )
    #
    #         # 检查是否加载了外部模型
    #         if "external model" in result.stdout.lower():
    #             print("✅ 外部模型加载成功！")
    #         else:
    #             print("⚠️  未检测到模型加载日志，请检查路径和文件格式")
    #
    #         print(f"查询成功完成！SARIF结果已保存至: {self.sarif_path}")
    #         return True
    #
    #     except subprocess.CalledProcessError as e:
    #         print(f"❌ CodeQL执行失败，错误输出:\n{e.stdout}")
    #         return False

if __name__ == "__main__":
    runner = SimpleCodeQLRunner()
    success = runner.run_query()
    if not success:
        exit(1)