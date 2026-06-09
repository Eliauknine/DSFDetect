import os
import subprocess
from pathlib import Path

class BatchCodeQLRunner:
    def __init__(self):
        # 基础路径配置
        self.codeql_cli = "/Users/mycp/CodeQL/codeql-cli/codeql/codeql"
        self.db_path = "/Users/mycp/CodeQL/databases/wolfssl-db"
        self.input_root = "/Users/mycp/CodeQL/result/Path/wolfssl"
        self.output_dir = "/Users/mycp/CodeQL/result/Path/wolfssl/result_of_json"

    def convert_bqrs_to_json(self):
        # 确保输出目录存在
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

        # 遍历 input_root 目录下的所有 .bqrs 文件
        for root, _, files in os.walk(self.input_root):
            for file in files:
                if file.endswith(".bqrs"):
                    bqrs_path = os.path.join(root, file)
                    # 生成对应的 JSON 文件名（保留原文件名，仅替换扩展名）
                    json_filename = os.path.splitext(file)[0] + ".json"
                    json_path = os.path.join(self.output_dir, json_filename)

                    # 执行 codeql bqrs decode 命令
                    cmd = [
                        self.codeql_cli,
                        "bqrs",
                        "decode",
                        "--format=json",
                        "--output=" + json_path,
                        bqrs_path
                    ]

                    print(f"Converting {bqrs_path} to {json_path}...")
                    try:
                        subprocess.run(cmd, check=True)
                        print(f"Successfully converted {file}")
                    except subprocess.CalledProcessError as e:
                        print(f"Failed to convert {file}: {e}")

if __name__ == "__main__":
    runner = BatchCodeQLRunner()
    runner.convert_bqrs_to_json()