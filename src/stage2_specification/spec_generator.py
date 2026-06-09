"""
Stage 2: Taint Specification Generation

Uses GPT to generate CodeQL data-flow model specifications (sourceModel, sinkModel,
summaryModel) for functions identified in Stage 1.
"""
import csv
import time
from pathlib import Path
from tqdm import tqdm

from src.llm.client import chat
from src.llm.prompts import STAGE2_TAINT_SPEC


def generate_specifications(csv_path, output_dir, project="ImageMagick", model="gpt-4o-mini"):
    """Generate taint specifications for functions listed in a CSV.

    Reads function names from csv_path, sends each to GPT, and writes
    three YAML files: source, sink, and summary models.

    Args:
        csv_path: CSV with 'function_name' and 'file_name' columns
        output_dir: Directory for output YAML files
        project: Project name for context in prompts
        model: GPT model to use

    Returns:
        Tuple of (source_yml_path, sink_yml_path, summary_yml_path)
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load functions (deduplicate by name)
    functions = []
    seen = set()
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            func_name = row.get("function_name", "")
            if func_name and func_name not in seen:
                seen.add(func_name)
                functions.append((row.get("file_name", ""), func_name))

    results_source = []
    results_sink = []
    results_summary = []

    for file_name, func_name in tqdm(functions, desc="Generating specs"):
        prompt = STAGE2_TAINT_SPEC.format(project=project, file=file_name, func=func_name)
        output = chat(
            messages=[
                {"role": "system", "content": "You are a CodeQL modeling assistant."},
                {"role": "user", "content": prompt}
            ],
            model=model,
            temperature=0.2,
            max_tokens=1000
        )

        if not output:
            time.sleep(2)
            continue

        yaml_lines = _extract_yaml_lines(output)

        for line in yaml_lines:
            if '"local"' in line:
                results_source.append(line)
            if '"remote-sink"' in line:
                results_sink.append(line)
            if '"taint"' in line:
                results_summary.append(line)

    source_path = output_dir / f"{project.lower()}_source.yml"
    sink_path = output_dir / f"{project.lower()}_sink.yml"
    summary_path = output_dir / f"{project.lower()}_summary.yml"

    _write_yml(source_path, "sourceModel", results_source)
    _write_yml(sink_path, "sinkModel", results_sink)
    _write_yml(summary_path, "summaryModel", results_summary)

    print(f"Specification generation complete for {project}")
    print(f"  Source: {len(results_source)} entries -> {source_path}")
    print(f"  Sink:   {len(results_sink)} entries -> {sink_path}")
    print(f"  Summary:{len(results_summary)} entries -> {summary_path}")

    return source_path, sink_path, summary_path


def _extract_yaml_lines(output):
    """Extract YAML data lines from GPT output."""
    lines = []
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("- ["):
            lines.append(line)
    return lines


def _write_yml(filename, extensible, data_lines):
    """Write a CodeQL model YAML file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("extensions:\n")
        f.write("  - addsTo:\n")
        f.write("      pack: codeql/cpp-all\n")
        f.write(f"      extensible: {extensible}\n")
        f.write("    data:\n")
        for line in data_lines:
            f.write(f"      {line}\n")
