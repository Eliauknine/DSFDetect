"""
SARIF file processing utilities.

Functions for parsing SARIF results, extracting matched function names,
and generating summary CSVs.
"""
import json
import csv
import os
import glob
from collections import defaultdict


def load_function_names(csv_path):
    """Load function names from a CSV into a dict keyed by function_name."""
    function_data = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            function_data[row['function_name']] = row
    return function_data


def process_sarif_file(sarif_path, function_data):
    """Process a single SARIF file and return matched function rows."""
    matched = []

    try:
        with open(sarif_path, 'r', encoding='utf-8') as f:
            sarif_content = json.load(f)

        if 'runs' in sarif_content:
            for run in sarif_content['runs']:
                if 'results' in run:
                    for result in run['results']:
                        result_text = json.dumps(result)
                        for func_name, func_info in function_data.items():
                            if func_name in result_text:
                                if func_info not in matched:
                                    matched.append(func_info)
    except Exception as e:
        print(f"Error processing {sarif_path}: {e}")

    return matched


def batch_process_sarif(sarif_dir, function_csv, output_dir):
    """Process all SARIF files in a directory and output CSV results."""
    os.makedirs(output_dir, exist_ok=True)

    function_data = load_function_names(function_csv)
    print(f"Loaded {len(function_data)} function names")

    sarif_files = glob.glob(os.path.join(sarif_dir, "*.sarif"))
    print(f"Found {len(sarif_files)} SARIF files")

    for sarif_path in sarif_files:
        print(f"Processing: {os.path.basename(sarif_path)}")
        matched = process_sarif_file(sarif_path, function_data)

        output_name = os.path.splitext(os.path.basename(sarif_path))[0] + ".csv"
        output_path = os.path.join(output_dir, output_name)

        if matched:
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=matched[0].keys())
                writer.writeheader()
                writer.writerows(matched)
            print(f"  Found {len(matched)} matches -> {output_name}")
        else:
            print(f"  No matches found")


def generate_summary_csv(result_dir, output_path, sort_by='total'):
    """Aggregate multiple SARIF result CSVs into a summary CSV."""
    all_data = defaultdict(dict)

    for csv_file in glob.glob(os.path.join(result_dir, "*.csv")):
        name = os.path.splitext(os.path.basename(csv_file))[0]
        if name in ("summary", "functions"):
            continue

        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                func_name = row['function_name']
                all_data[func_name][name] = int(row.get('is_present', 0))

    # Sort functions
    if sort_by == 'total':
        sorted_funcs = sorted(all_data.keys(),
                              key=lambda x: sum(all_data[x].values()), reverse=True)
    elif sort_by == 'max':
        sorted_funcs = sorted(all_data.keys(),
                              key=lambda x: max(all_data[x].values(), default=0), reverse=True)
    else:
        sorted_funcs = sorted(all_data.keys())

    all_files = sorted(set(f for d in all_data.values() for f in d))

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['function_name'] + all_files + ['total', 'max'])

        for func in sorted_funcs:
            counts = all_data[func]
            row = [func]
            total = 0
            max_count = 0
            for sf in all_files:
                c = counts.get(sf, 0)
                row.append(str(c))
                total += c
                max_count = max(max_count, c)
            row.extend([str(total), str(max_count)])
            writer.writerow(row)

    print(f"Summary written to: {output_path}")
