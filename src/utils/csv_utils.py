"""
CSV processing utilities: deduplication, filtering, merging, statistics.
"""
import pandas as pd


def deduplicate_and_filter(input_csv, output_csv, groundtruth_csv, subset=None):
    """Deduplicate a CSV and filter rows to only those present in groundtruth.

    Args:
        input_csv: Path to input CSV
        output_csv: Path for filtered output
        groundtruth_csv: CSV with groundtruth function names
        subset: Columns to use for dedup (default: ['function_name', 'taint_role'])

    Returns:
        Tuple of (original_count, deduped_count, filtered_count)
    """
    if subset is None:
        subset = ['function_name', 'taint_role']

    df = pd.read_csv(input_csv)
    df_dedup = df.drop_duplicates(subset=subset, keep='first')

    try:
        df_gt = pd.read_csv(groundtruth_csv)
        gt_functions = set(df_gt['function_name'].unique())
    except Exception as e:
        print(f"Error reading groundtruth: {e}")
        return 0, 0, 0

    df_filtered = df_dedup[df_dedup['function_name'].isin(gt_functions)]
    df_filtered.to_csv(output_csv, index=False)

    print(f"Original: {len(df)}, Deduped: {len(df_dedup)}, Filtered: {len(df_filtered)}")
    return len(df), len(df_dedup), len(df_filtered)


def merge_csvs(file1, file2, output, drop_duplicates=True):
    """Merge two CSV files by concatenation."""
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    merged = pd.concat([df1, df2], ignore_index=True)
    if drop_duplicates:
        merged = merged.drop_duplicates()
    merged.to_csv(output, index=False)
    print(f"Merged {len(df1)} + {len(df2)} -> {len(merged)} rows -> {output}")
    return merged


def count_csv_files(directory):
    """Count CSV files recursively in a directory."""
    import os
    count = 0
    for root, _, files in os.walk(directory):
        count += sum(1 for f in files if f.lower().endswith('.csv'))
    return count


def compute_is_present_sum(csv_path, column='is_present'):
    """Sum the values in a specific column of a CSV."""
    df = pd.read_csv(csv_path)
    total = df[column].sum()
    print(f"Sum of '{column}' in {csv_path}: {total}")
    return total
