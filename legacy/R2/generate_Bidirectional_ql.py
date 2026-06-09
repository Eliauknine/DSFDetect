# generate_Bidirectional_ql.py
import os
import csv
from codeql_queries import SOURCE_SINK_SEARCH, SOURCE_ONLY, SINK_ONLY

def read_function_names_and_roles(csv_path):
    """Read function names and taint roles from a CSV file"""
    functions = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            functions.append({
                'name': row['function_name'],
                'role': row['taint_role']
            })
    return functions

def generate_ql_files(functions, output_dir):
    """Generate QL files for each function based on its taint role"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for func in functions:
        if func['role'] == 'Source':
            ql_content = SOURCE_ONLY.replace('{function_name}', func['name'])
            file_name = f"{func['name']}_find_sink.ql"
        if func['role'] == 'Sink':
            ql_content = SINK_ONLY.replace('{function_name}', func['name'])
            file_name = f"{func['name']}_find_source.ql"
        if func['role'] == 'Inter_procedural_API':  # Inter_procedural_API or others
            ql_content = SOURCE_SINK_SEARCH.replace('{function_name}', func['name'])
            file_name = f"{func['name']}_find_source_sink.ql"

        output_path = os.path.join(output_dir, file_name)

        with open(output_path, 'w') as f:
            f.write(ql_content)

        print(f"Generated QL file: {output_path}")


'''
data/results/stage1/filtered/libraw_taint_functions.csv
data/results/stage1/filtered/libtiff_taint_functions.csv
data/results/stage1/filtered/wolfssl_taint_functions.csv
R2/myquery/ql_source_sink_extract/libraw
R2/myquery/ql_source_sink_extract/libtiff
R2/myquery/ql_source_sink_extract/wolfssl
'''
if __name__ == "__main__":
    input_file = "data/results/stage1/filtered/wolfssl_taint_functions.csv"
    output_dir = "R2/myquery/ql_source_sink_extract/wolfssl"

    functions = read_function_names_and_roles(input_file)
    generate_ql_files(functions, output_dir)

    print(f"\nSuccessfully generated {len(functions)} QL files in {output_dir}")