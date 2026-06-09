"""
CodeQL query runner — single query and batch modes.

Supports:
- Running a single .ql or .qls query against a CodeQL database
- Batch running all .ql files in a directory
- Running queries across multiple databases
- Output as SARIF, BQRS, or CSV
"""
import os
import subprocess
import time
from pathlib import Path
from tqdm import tqdm

from src.config import CODEQL_CLI, CODEQL_DB_DIR


class CodeQLRunner:
    """Run CodeQL queries against one or more databases."""

    def __init__(self, db_name="ImageMagick", db_path=None, output_root=None):
        self.codeql_cli = CODEQL_CLI
        self.db_path = db_path or os.path.join(CODEQL_DB_DIR, db_name)
        self.output_root = output_root
        if self.output_root:
            Path(self.output_root).mkdir(parents=True, exist_ok=True)

    def run_query_sarif(self, query_path, output_path, model_pack=None, additional_packs=None, rerun=True):
        """Run a query and output SARIF format."""
        cmd = [
            self.codeql_cli, "database", "analyze",
            "--format=sarif-latest",
            f"--output={output_path}",
        ]
        if additional_packs:
            cmd.append(f"--additional-packs={additional_packs}")
        if model_pack:
            cmd.append(f"--model-packs={model_pack}")
        if rerun:
            cmd.append("--rerun")
        cmd.extend([self.db_path, query_path])

        try:
            subprocess.run(cmd, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True, None
        except subprocess.CalledProcessError as e:
            return False, str(e)

    def run_query_bqrs(self, ql_path, bqrs_path):
        """Run a query and output BQRS intermediate format."""
        try:
            subprocess.run([
                self.codeql_cli, "query", "run",
                f"--database={self.db_path}",
                f"--output={bqrs_path}",
                ql_path
            ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True, None
        except subprocess.CalledProcessError as e:
            return False, str(e)

    def bqrs_to_csv(self, bqrs_path, csv_path):
        """Convert BQRS file to CSV."""
        subprocess.run([
            self.codeql_cli, "bqrs", "decode",
            bqrs_path,
            "--format=csv",
            f"--output={csv_path}"
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class BatchRunner(CodeQLRunner):
    """Batch run all .ql files in a directory."""

    def __init__(self, queries_root, db_name="ImageMagick", output_root=None):
        super().__init__(db_name=db_name, output_root=output_root)
        self.queries_root = queries_root

    def find_ql_files(self):
        """Recursively find all .ql files."""
        ql_files = []
        for root, _, files in os.walk(self.queries_root):
            for f in files:
                if f.endswith('.ql'):
                    ql_files.append(os.path.join(root, f))
        return ql_files

    def run_all(self, output_format="csv"):
        """Run all queries with a progress bar."""
        ql_files = self.find_ql_files()
        success = 0
        failed = []

        print(f"Found {len(ql_files)} query files. Starting...\n")

        for ql_path in tqdm(ql_files, desc="Running queries", unit="query"):
            name = Path(ql_path).stem
            bqrs_path = os.path.join(self.output_root, f"{name}.bqrs")
            csv_path = os.path.join(self.output_root, f"{name}.csv")

            ok, err = self.run_query_bqrs(ql_path, bqrs_path)
            if ok:
                if output_format == "csv":
                    self.bqrs_to_csv(bqrs_path, csv_path)
                success += 1
            else:
                failed.append((name, err))

        print(f"\nDone: {success}/{len(ql_files)} succeeded")
        if failed:
            print(f"Failed queries: {len(failed)}")
            for name, err in failed[:5]:
                print(f"  - {name}: {err[:100]}")


class MultiDBRunner:
    """Run the same queries across multiple CodeQL databases."""

    def __init__(self, databases_root=None, queries_root=None, output_root=None):
        self.databases_root = databases_root or CODEQL_DB_DIR
        self.queries_root = queries_root
        self.output_root = output_root
        if self.output_root:
            Path(self.output_root).mkdir(parents=True, exist_ok=True)

    def run_all_databases(self, db_names, ql_files):
        """Run all queries against all specified databases."""
        total_success = 0
        total_queries = len(ql_files) * len(db_names)

        print(f"Processing {len(db_names)} databases, {len(ql_files)} queries each\n")

        for db_name in db_names:
            db_path = os.path.join(self.databases_root, db_name)
            if not os.path.exists(db_path):
                print(f"  SKIP: database not found: {db_path}")
                continue

            runner = BatchRunner(
                queries_root=self.queries_root,
                db_name=db_name,
                output_root=os.path.join(self.output_root, db_name) if self.output_root else None
            )
            runner.db_path = db_path
            runner.run_all()

        print(f"\nAll databases processed.")
