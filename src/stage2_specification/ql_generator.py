"""
Generate CodeQL query (.ql) files from function name lists.

Reads function names from text files and creates individual .ql query files
using the SOURCE_SINK_SEARCH template.
"""
import os
from src.codeql.queries import SOURCE_SINK_SEARCH


def read_function_names(file_path):
    """Read function names from a text file (one per line)."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def generate_ql_files(function_names, output_dir, template=None):
    """Generate a .ql file for each function name.

    Args:
        function_names: List of function name strings
        output_dir: Directory to write .ql files into
        template: QL template to use (default: SOURCE_SINK_SEARCH)
    """
    if template is None:
        template = SOURCE_SINK_SEARCH

    os.makedirs(output_dir, exist_ok=True)

    for func_name in function_names:
        ql_content = template.replace('{function_name}', func_name)
        file_name = f"{func_name}_source_sink.ql"
        output_path = os.path.join(output_dir, file_name)

        with open(output_path, 'w') as f:
            f.write(ql_content)

        print(f"Generated: {output_path}")

    print(f"\nGenerated {len(function_names)} QL files in {output_dir}")


def generate_from_file(input_file, output_dir, template=None):
    """Convenience: read function names from file and generate QL files."""
    names = read_function_names(input_file)
    generate_ql_files(names, output_dir, template)
