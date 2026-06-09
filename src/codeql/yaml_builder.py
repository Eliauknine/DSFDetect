"""
YAML model file builder for CodeQL data-flow models.

Generates custom-models YAML files from CSV containing function names and taint roles.
Also supports modifying existing YAML files (e.g., changing "local" to "remote").
"""
import csv
import os

from src.codeql.queries import SourceModel, SinkModel, SummaryModel


def generate_yaml_from_csv(csv_path, output_path=None):
    """Generate a CodeQL model YAML file from a CSV with function_name and taint_role columns.

    Args:
        csv_path: Path to CSV file with columns 'function_name' and 'taint_role'
        output_path: Path for output YAML file (default: derived from csv_path)

    Returns:
        The YAML content as a string.
    """
    yaml_content = "extensions:\n"

    with open(csv_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if 'function_name' not in row or 'taint_role' not in row:
                print(f"Warning: Missing columns in row: {row}")
                continue

            function_name = row['function_name']
            taint_role = row['taint_role']

            if taint_role == "Source":
                yaml_content += SourceModel.format(function_name=function_name) + "\n"
            elif taint_role == "Sink":
                yaml_content += SinkModel.format(function_name=function_name) + "\n"
            elif taint_role == "Inter_procedural_API":
                yaml_content += SummaryModel.format(function_name=function_name) + "\n"

    if output_path:
        with open(output_path, 'w') as f:
            f.write(yaml_content)
        print(f"YAML file generated: {output_path}")

    return yaml_content


def modify_yaml_file(input_path, output_path, changes=None):
    """Modify a CodeQL model YAML file.

    Supported changes (dict):
      - 'sourceModel': change 'local' to 'remote'
      - 'sinkModel': keep as-is or modify
      - 'summaryModel': keep as-is or modify

    Args:
        input_path: Path to input YAML file
        output_path: Path for modified output
        changes: Dict of extensible_type -> modification to apply
    """
    if changes is None:
        changes = {}

    current_extensible = None

    with open(input_path, "r") as f_in, open(output_path, "w") as f_out:
        for line in f_in:
            stripped = line.strip()

            if stripped.startswith("extensible:"):
                if "sourceModel" in stripped:
                    current_extensible = "sourceModel"
                elif "sinkModel" in stripped:
                    current_extensible = "sinkModel"
                elif "summaryModel" in stripped:
                    current_extensible = "summaryModel"
                else:
                    current_extensible = None

            modified = _process_line(line, current_extensible, changes)
            f_out.write(modified)

    print(f"Modified YAML written to: {output_path}")


def _process_line(line, current_extensible, changes):
    """Process a single data line based on extensible type."""
    stripped = line.strip()

    if stripped.startswith("- ["):
        content = stripped[len("- ["):-1]
        parts = [p.strip() for p in content.split(",")]

        if current_extensible == "sourceModel" and "sourceModel" in changes:
            if len(parts) >= 3 and parts[-2].strip('"') == "local":
                parts[-2] = '"remote"'

        return "      - [" + ", ".join(parts) + "]\n"

    return line
