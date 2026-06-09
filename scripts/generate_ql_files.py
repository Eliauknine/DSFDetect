# generate_ql_files.py
import os
from codeql_queries import SOURCE_SINK_SEARCH


def read_function_names(file_path):
    """Read function names from a text file"""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def generate_ql_files(function_names, output_dir):
    """Generate QL files for each function name"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for function_name in function_names:
        ql_content = SOURCE_SINK_SEARCH.replace('{function_name}', function_name)
        file_name = f"{function_name}_source_sink.ql"
        output_path = os.path.join(output_dir, file_name)

        with open(output_path, 'w') as f:
            f.write(ql_content)

        print(f"Generated QL file: {output_path}")


if __name__ == "__main__":
    input_file = "data/function_names/wolfssl_func_name_final.txt"
    output_dir = "myquery/wolfssl/wolfssl_source_sink_extract"

    function_names = read_function_names(input_file)
    generate_ql_files(function_names, output_dir)

    print(f"\nSuccessfully generated {len(function_names)} QL files in {output_dir}")