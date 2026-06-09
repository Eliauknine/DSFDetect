"""
Stage 1: Sensitive Function Extraction

Uses GPT to analyze documentation and extract potentially vulnerable functions,
classifying them as Source, Sink, or Inter_procedural_API.
"""
import json
import logging
import pandas as pd
from pathlib import Path
from tqdm import tqdm

from src.llm.client import chat
from src.llm.prompts import STAGE1_EXTRACT_FUNCTIONS

logging.basicConfig(level=logging.INFO)

TAINT_ROLE_SOURCE = "Source"
TAINT_ROLE_SINK = "Sink"
TAINT_ROLE_INTER = "Inter_procedural_API"


def extract_functions_from_docs(input_csv, output_dir, model="gpt-3.5-turbo"):
    """Main entry point for Stage 1.

    Reads document snippets from input_csv, sends each to GPT, and saves
    extracted sensitive function names with taint roles.

    Args:
        input_csv: Path to CSV with a 'content' column (document snippets)
        output_dir: Directory to save results
        model: GPT model to use

    Returns:
        Path to the summary CSV file.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_csv)
    all_results = []

    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Extracting functions"):
        content = row.get('content', '')
        if not isinstance(content, str) or len(content) < 10:
            continue

        response = _query_gpt(content, idx, output_dir, model)
        if not response:
            continue

        functions = _parse_response(response)
        for func in functions:
            result = {
                "doc_index": idx,
                "function_name": "",
                "taint_role": TAINT_ROLE_INTER,
                "reason": "Unknown",
                "source_text": content[:200] + "..."
            }

            if isinstance(func, dict):
                result["function_name"] = func.get("function_name", "")
                result["taint_role"] = func.get("taint_role", TAINT_ROLE_INTER).capitalize()
                if result["taint_role"] not in [TAINT_ROLE_SOURCE, TAINT_ROLE_SINK, TAINT_ROLE_INTER]:
                    result["taint_role"] = TAINT_ROLE_INTER
                result["reason"] = func.get("reason", "No reason provided")
            elif isinstance(func, str):
                result["function_name"] = func.strip()
                result["reason"] = "Parsed from string response"

            if result["function_name"]:
                all_results.append(result)

    summary_path = output_dir / "vulnerable_functions_summary.csv"
    pd.DataFrame(all_results).to_csv(summary_path, index=False)

    if all_results:
        role_counts = pd.DataFrame(all_results)["taint_role"].value_counts()
        logging.info(f"Stage 1 complete: {len(all_results)} functions found")
        logging.info(f"Taint role distribution:\n{role_counts}")
    else:
        logging.warning("Stage 1 complete but no functions found.")

    return summary_path


def _query_gpt(content, index, output_dir, model):
    """Send a document snippet to GPT and save raw response."""
    prompt = STAGE1_EXTRACT_FUNCTIONS.format(content=content[:6000])
    response = chat(
        messages=[
            {"role": "system", "content": "You must strictly follow the required JSON output format. Only return valid JSON."},
            {"role": "user", "content": prompt}
        ],
        model=model,
        temperature=0.1,
        response_format={"type": "json_object"}
    )

    if response:
        raw_file = output_dir / f"llm_response_{index}.txt"
        with open(raw_file, 'w', encoding='utf-8') as f:
            f.write(response)

    return response


def _parse_response(response_text):
    """Robust JSON parsing of GPT response."""
    try:
        cleaned = response_text.strip()
        if not cleaned.startswith("{"):
            cleaned = "{" + cleaned
        if not cleaned.endswith("}"):
            cleaned = cleaned + "}"

        data = json.loads(cleaned)

        if isinstance(data, dict) and "functions" in data:
            functions = data.get("functions", [])
            if not isinstance(functions, list):
                return []

            validated = []
            for func in functions:
                if isinstance(func, dict) and "function_name" in func:
                    validated.append({
                        "function_name": func["function_name"],
                        "taint_role": func.get("taint_role", TAINT_ROLE_INTER),
                        "reason": func.get("reason", "No reason provided")
                    })
                elif isinstance(func, str):
                    validated.append({
                        "function_name": func,
                        "taint_role": TAINT_ROLE_INTER,
                        "reason": "Parsed from string response"
                    })
            return validated
        else:
            logging.warning(f"Unexpected format: {response_text[:200]}...")
            return []
    except json.JSONDecodeError as e:
        logging.error(f"JSON parse failed: {e}")
        return []
