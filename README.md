# DSFDetect

> **D**etection of **S**ensitive **F**unctions via LLM-Assisted **D**ata-Flow Analysis for C/C++ Libraries

A framework that combines Large Language Models (GPT) with CodeQL static analysis to automatically identify security-sensitive functions, construct taint analysis specifications, and detect vulnerabilities in C/C++ open-source libraries.

---

## Table of Contents

- [Overview](#overview)
- [Motivation & Background](#motivation--background)
- [System Architecture](#system-architecture)
  - [Stage 1: Sensitive Function Extraction](#stage-1-sensitive-function-extraction)
  - [Stage 2: Taint Specification Extraction](#stage-2-taint-specification-extraction)
  - [Stage 3: Vulnerability Detection](#stage-3-vulnerability-detection)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage Guide](#usage-guide)
  - [Quick Start: Running the Full Pipeline](#quick-start-running-the-full-pipeline)
  - [Stage-by-Stage Usage](#stage-by-stage-usage)
    - [Stage 1: Extract Sensitive Functions](#stage-1-extract-sensitive-functions)
    - [Stage 2: Generate Taint Specifications](#stage-2-generate-taint-specifications)
    - [Stage 3: Vulnerability Detection with CodeQL](#stage-3-vulnerability-detection-with-codeql)
  - [Utility Functions](#utility-functions)
- [Module Reference](#module-reference)
  - [`src/codeql/` — CodeQL Integration](#srccodeql----codeql-integration)
  - [`src/llm/` — LLM Integration](#srcllm----llm-integration)
  - [`src/stage1_extract/` — Function Extraction](#srcstage1_extract----function-extraction)
  - [`src/stage2_specification/` — Specification Generation](#srcstage2_specification----specification-generation)
  - [`src/utils/` — Shared Utilities](#srcutils----shared-utilities)
- [Data Formats](#data-formats)
- [Supported Target Projects](#supported-target-projects)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Overview

Traditional taint analysis faces two significant challenges:

1. **Sensitive functions are hard to identify** — manually labeling which functions act as data sources, sinks, or propagation points is labor-intensive and error-prone.
2. **LLM-generated specifications have accuracy gaps** — raw GPT outputs often contain formatting errors, hallucinated function names, and incorrect parameter mappings.

DSFDetect addresses both problems by integrating LLM-based semantic understanding with CodeQL's precise data-flow analysis. The system:

- Converts developer documentation into structured prompts for GPT
- Uses GPT to extract potentially vulnerable functions and classify their taint roles (Source / Sink / Inter_procedural_API)
- Generates CodeQL-compatible data-flow model specifications in YAML format
- Applies those models through CodeQL to perform taint tracking and vulnerability detection
- Validates results against groundtruth datasets

**Supported target libraries:** ImageMagick, LibRaw, LibTIFF, WolfSSL

---

## Motivation & Background

In CodeQL-based taint analysis, the precision of the analysis depends heavily on the quality of **data-flow models** — definitions that tell the engine which functions introduce untrusted data (sources), which functions consume data dangerously (sinks), and which functions propagate taint from input to output (summaries). Writing these models manually requires deep knowledge of each library's API, which does not scale.

DSFDetect automates model construction in three phases:

1. **Pre-processing**: Developer documentation is converted to Markdown and split into chunks optimized for GPT's context window. CodeQL databases are built from project source code, providing AST (Abstract Syntax Tree), CFG (Control-Flow Graph), and DFG (Data-Flow Graph) information. Redundant content is cleaned to ensure input quality.

2. **LLM-powered extraction**: Chunked documentation is fed into carefully designed prompts that instruct GPT to identify sensitive functions and determine their taint roles. This approach improves coverage compared to rule-based or manual annotation methods, and adapts better across different projects.

3. **Static analysis integration**: The extracted specifications are converted to CodeQL model packs, integrated into the taint analysis library, and evaluated using CodeQL test suites to assess detection capability.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATA FLOW                               │
│                                                                 │
│  Developer Docs ──→ Stage 1 ──→ Stage 2 ──→ Stage 3 ──→ Report │
│  (Markdown/CSV)     (GPT)       (GPT+QL)    (CodeQL)            │
│                                                                 │
│  CodeQL DB ────────────────────→ Stage 2 ──→ Stage 3           │
│  (AST/CFG/DFG)                    (Specs)     (Detection)        │
└─────────────────────────────────────────────────────────────────┘
```

### Stage 1: Sensitive Function Extraction

**Goal:** Automatically identify security-sensitive functions from developer documentation and classify them by taint role.

**Input:**
- CSV files containing document snippets (`content` column), one row per chunk of documentation

**Process:**
1. Each document snippet is embedded into a structured prompt template (`STAGE1_EXTRACT_FUNCTIONS`)
2. GPT is queried with JSON mode enabled, requesting a structured output listing all vulnerable functions
3. The raw GPT response is saved to disk for auditability and parsed for function names and taint roles
4. Results are aggregated into a summary CSV (`vulnerable_functions_summary.csv`)

**Roles assigned:**

| Role | Description | Example |
|------|-------------|---------|
| `Source` | Introduces untrusted data into the program | `recv()`, `fread()`, `scanf()` |
| `Sink` | Consumes data in a security-sensitive way | `system()`, `fwrite()`, `send()` |
| `Inter_procedural_API` | Processes data between sources and sinks | Transformation / processing functions |

**Output:** `vulnerable_functions_summary.csv` with columns: `doc_index`, `function_name`, `taint_role`, `reason`, `source_text`

**Key module:** [`src/stage1_extract/extractor.py`](src/stage1_extract/extractor.py)

---

### Stage 2: Taint Specification Extraction

**Goal:** Generate CodeQL-compatible data-flow model specifications (sourceModel, sinkModel, summaryModel) with accurate parameter mappings.

**Input:**
- CSV from Stage 1 containing function names and file locations
- CodeQL database information (AST, CFG, DFG) providing namespace, parameter behavior, call relationships, and return value semantics

**Process:**
1. Functions from Stage 1 are deduplicated by name
2. Each function is embedded into the `STAGE2_TAINT_SPEC` prompt, which instructs GPT to:
   - Classify the function as sourceModel, sinkModel, and/or summaryModel
   - Fill in precise data-flow parameter positions (e.g., `Argument[*0]`, `Argument[*1]`, `ReturnValue`)
   - Separate namespace from function name (e.g., `Magick::Image::gaussianBlurChannel` → namespace `Magick::Image`, function `gaussianBlurChannel`)
3. GPT outputs YAML data lines, which are classified by model type
4. Three YAML files are generated per project: `{project}_source.yml`, `{project}_sink.yml`, `{project}_summary.yml`

**Output:** Three YAML model files in CodeQL's custom-models format for direct integration into taint analysis.

**Key module:** [`src/stage2_specification/spec_generator.py`](src/stage2_specification/spec_generator.py)

---

### Stage 3: Vulnerability Detection

**Goal:** Apply generated taint specifications through CodeQL and evaluate detection capability.

**Input:**
- CodeQL model YAML files from Stage 2
- CodeQL databases for target projects
- Groundtruth datasets for validation

**Process:**
1. Generated YAML models are integrated into CodeQL's model packs
2. CodeQL queries (pre-built templates or generated queries) are executed against project databases
3. Results are collected as SARIF files
4. SARIF results are parsed to count function presence (`is_present`) and matched against groundtruth
5. Summary statistics are computed across all queries for ranking and evaluation

**Output:** SARIF result files, per-query CSVs, and aggregated function-level summary CSVs.

**Key modules:**
- [`src/codeql/runner.py`](src/codeql/runner.py) — CodeQL query execution
- [`src/utils/sarif_utils.py`](src/utils/sarif_utils.py) — SARIF parsing and result aggregation

---

## Project Structure

```
DSFDetect/
│
├── src/                                   # Core Python source code
│   ├── __init__.py                        # Package marker
│   ├── config.py                          # Centralized configuration management
│   │
│   ├── codeql/                            # CodeQL integration layer
│   │   ├── __init__.py
│   │   ├── queries.py                     # QL query templates + target function predicates
│   │   ├── runner.py                      # Query execution (single, batch, multi-DB)
│   │   └── yaml_builder.py                # YAML model file generation & modification
│   │
│   ├── llm/                               # Large Language Model integration
│   │   ├── __init__.py
│   │   ├── client.py                      # OpenAI API wrapper
│   │   └── prompts.py                     # All prompt templates (centralized)
│   │
│   ├── stage1_extract/                    # Stage 1: Sensitive Function Extraction
│   │   ├── __init__.py
│   │   └── extractor.py                   # GPT-based function extraction from docs
│   │
│   ├── stage2_specification/              # Stage 2: Taint Specification Generation
│   │   ├── __init__.py
│   │   ├── spec_generator.py              # GPT-based taint spec generation
│   │   └── ql_generator.py                # CodeQL query file generation
│   │
│   ├── stage3_detect/                     # Stage 3: Vulnerability Detection
│   │   └── __init__.py
│   │
│   └── utils/                             # Shared utility modules
│       ├── __init__.py
│       ├── csv_utils.py                   # CSV dedup, merge, filter, statistics
│       └── sarif_utils.py                 # SARIF parsing & result aggregation
│
├── config/                                # Configuration files
│   ├── models/                            # CodeQL data-flow model YAML files
│   │   ├── imagemagick_source.yml
│   │   ├── imagemagick_sink.yml
│   │   ├── imagemagick_summary.yml
│   │   ├── imagemagick_source.modified.yml
│   │   ├── custom-models1.yml
│   │   └── ...
│   │
│   └── templates/                         # QL template files
│       └── cpp-lgtm-ql.txt
│
├── data/                                  # Data files (read/write)
│   ├── function_names/                    # Function name lists per target library
│   │   ├── imagemagic_func_name.txt
│   │   ├── libraw_func_name.txt
│   │   ├── libtiff_func_name.txt
│   │   └── wolfssl_func_name.txt
│   │
│   ├── groundtruths/                      # Ground truth data for result validation
│   │   ├── imagemagick_functions_gt.csv
│   │   ├── libraw_functions_gt.csv
│   │   ├── libtiff_functions_gt.csv
│   │   ├── wolfssl_functions_gt.csv
│   │   └── *_gt_all.csv                   # Full groundtruth variants
│   │
│   ├── input_docs/                        # Input documentation (CSV with 'content' column)
│   │   └── *_doc_input.csv
│   │
│   ├── docs/                              # Reference documentation (per library)
│   │   ├── imageMagick/
│   │   ├── libraw/
│   │   └── libtiff/
│   │
│   └── results/                           # Pipeline results (organized by stage)
│       ├── stage1/                        # GPT raw responses + summary CSVs
│       │   └── <project>/                 # llm_response_*.txt, vulnerable_functions_summary.csv
│       ├── stage2/                        # SARIF results + extracted specifications
│       │   ├── sarif/
│       │   └── extracted/
│       └── stage3/                        # Path search + detection results
│           ├── path_search/
│           └── detect/
│
├── queries/                               # Generated CodeQL query (.ql) files
│   ├── imagemagick/
│   ├── libraw/
│   ├── libtiff/
│   ├── wolfssl/
│   ├── path_queries/                      # Path-problem query variants
│   ├── generated/                         # Auto-generated queries
│   └── ...
│
├── scripts/                               # Standalone utility scripts (legacy)
│   ├── sensitive_func_judge.py            # Original Stage 1 script
│   ├── judge.py                           # Original Stage 2 script
│   ├── generate_ql_files.py               # QL file generation utility
│   ├── ymlCreate.py                       # YAML creation utility
│   ├── modify_yaml.py                     # YAML modification utility
│   └── test.py                            # Miscellaneous data analysis snippets
│
├── legacy/                                # Original R1/R2/R3 iteration code (preserved)
│   ├── R1/                                # Iteration 1: Function extraction
│   ├── R2/                                # Iteration 2: Specification refinement
│   └── R3/                                # Iteration 3: Detection phase
│
├── third_party/                           # Third-party source code
│   └── ImageMagick-7.0.1-0/               # ImageMagick reference source
│
├── .env.example                           # Environment variable template
├── requirements.txt                       # Python dependencies
└── README.md                              # This file
```

---

## Installation & Setup

### Prerequisites

| Component | Required For | Notes |
|-----------|-------------|-------|
| Python 3.8+ | All stages | |
| CodeQL CLI | Stages 2 & 3 | [github/github-codeql](https://github.com/github/codeql) |
| CodeQL C/C++ libraries | Stages 2 & 3 | Included with CodeQL repository |
| CodeQL databases | Stages 2 & 3 | One per target project (pre-built) |
| OpenAI API access | Stages 1 & 2 | Or any compatible API endpoint |

### Installation

```bash
# 1. Navigate to the project directory
cd DSFDetect

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Create your environment configuration
cp .env.example .env

# 4. Edit .env with your actual values
#    - Set your OpenAI API key
#    - Set CodeQL CLI and database paths
```

### Configuration

All configuration is managed through environment variables (loaded via `.env`) and centralized in [`src/config.py`](src/config.py).

**Environment Variables (`.env`):**

```bash
# CodeQL CLI executable path
CODEQL_CLI=/path/to/codeql

# Directory containing CodeQL databases
CODEQL_DB_DIR=/path/to/codeql-databases

# CodeQL repository root
CODEQL_REPO_DIR=/path/to/codeql-repo

# OpenAI API configuration
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
OPENAI_BASE_URL=https://api.openai.com/v1/    # Default: OpenAI; change for proxy endpoints
LLM_MODEL=gpt-3.5-turbo                       # Default model for all stages
```

**CodeQL Database Naming:**

The system expects databases to be organized as follows under `CODEQL_DB_DIR`:

| Project | Database Directory | Config Key |
|---------|-------------------|-------------|
| ImageMagick | `ImageMagick` | `imagemagick` |
| LibRaw | `libraw-db` | `libraw` |
| LibTIFF | `libtiff-db` | `libtiff` |
| WolfSSL | `wolfssl-db` | `wolfssl` |

These mappings are defined in `src/config.py` → `CODEQL_DATABASES` and can be customized.

---

## Usage Guide

### Quick Start: Running the Full Pipeline

The following example demonstrates the complete workflow for ImageMagick:

```python
from src.stage1_extract.extractor import extract_functions_from_docs
from src.stage2_specification.spec_generator import generate_specifications
from src.codeql.runner import CodeQLRunner

# ===== Stage 1: Extract sensitive functions from documentation =====
summary_csv = extract_functions_from_docs(
    input_csv="data/input_docs/imagemagick_doc_input.csv",
    output_dir="data/results/stage1/imagemagick",
    model="gpt-3.5-turbo"
)
print(f"Stage 1 complete → {summary_csv}")

# ===== Stage 2: Generate taint specifications =====
source_yml, sink_yml, summary_yml = generate_specifications(
    csv_path="data/results/stage1/imagemagick/vulnerable_functions_summary.csv",
    output_dir="data/results/stage2/imagemagick",
    project="ImageMagick",
    model="gpt-4o-mini"
)

# ===== Stage 3: Run CodeQL with the generated models =====
runner = CodeQLRunner(
    db_name="ImageMagick",
    output_root="data/results/stage3/imagemagick"
)
runner.run_query_sarif(
    query_path="config/templates/cpp-lgtm-ql.txt",
    output_path="data/results/stage3/imagemagick/results.sarif",
    model_pack="config/models",
    additional_packs="/path/to/codeql-repo/cpp/ql/src/Mymodels"
)
```

### Stage-by-Stage Usage

#### Stage 1: Extract Sensitive Functions

```python
from src.stage1_extract.extractor import extract_functions_from_docs

# Extract functions from documentation snippets
summary_path = extract_functions_from_docs(
    input_csv="data/input_docs/libraw_doc_input.csv",
    output_dir="data/results/stage1/libraw",
    model="gpt-4o-mini"                # Optional; defaults to config.LLM_MODEL
)
# Returns: Path to vulnerable_functions_summary.csv
```

**Input CSV format** (one column):
```csv
content
"LibRaw::dcraw_clear_mem clears memory allocated for raw image processing..."
"bad_pixels() corrects dead or hot pixels in raw sensor data..."
```

**Output:** `data/results/stage1/<project>/` contains:
- `llm_response_0.txt`, `llm_response_1.txt`, ... — Raw GPT responses
- `vulnerable_functions_summary.csv` — Aggregated function list with taint roles

**Note:** Raw responses are saved to disk so you can inspect GPT output or resume without re-querying.

#### Stage 2: Generate Taint Specifications

**Option A: GPT-based specification generation**

```python
from src.stage2_specification.spec_generator import generate_specifications

source_yml, sink_yml, summary_yml = generate_specifications(
    csv_path="data/results/stage1/imagemagick/vulnerable_functions_summary.csv",
    output_dir="data/results/stage2/imagemagick",
    project="ImageMagick",
    model="gpt-4o-mini"
)
# Returns: (source_yml_path, sink_yml_path, summary_yml_path)
```

**Option B: Generate .ql query files from function name lists**

```python
from src.stage2_specification.ql_generator import generate_from_file

generate_from_file(
    input_file="data/function_names/libraw_func_name_final.txt",
    output_dir="queries/libraw"
)
# One .ql file per function name is created
```

**Option C: Build CodeQL model YAML from CSV (template-based)**

```python
from src.codeql.yaml_builder import generate_yaml_from_csv, modify_yaml_file

# Generate model YAML from a CSV with function_name + taint_role columns
generate_yaml_from_csv(
    csv_path="data/results/stage1/imagemagick/vulnerable_functions_summary.csv",
    output_path="config/models/imagemagick_models.yml"
)

# Post-process: modify existing YAML (e.g., change source tags from 'local' to 'remote')
modify_yaml_file(
    input_path="config/models/imagemagick_source.yml",
    output_path="config/models/imagemagick_source.modified.yml",
    changes={"sourceModel": "local_to_remote"}
)
```

**Option D: Generate QL predicate entries from CSV**

See `codeql_queries.py` for the `print_qlpack_entries()` helper (prints `targetFunctions` predicate lines from a CSV of function names).

#### Stage 3: Vulnerability Detection with CodeQL

**Option A: Run a single query**

```python
from src.codeql.runner import CodeQLRunner

runner = CodeQLRunner(
    db_name="ImageMagick",            # Uses db name from CODEQL_DATABASES
    output_root="data/results/stage3"
)

# Run query → SARIF output
success, error = runner.run_query_sarif(
    query_path="queries/imagemagick/AcquireQuantumMemory_source_sink.ql",
    output_path="data/results/stage3/AcquireQuantumMemory.sarif",
    rerun=True                        # Force re-analysis
)
```

**Option B: Batch run all queries in a directory**

```python
from src.codeql.runner import BatchRunner

runner = BatchRunner(
    queries_root="queries/imagemagick",
    db_name="ImageMagick",
    output_root="data/results/stage3/imagemagick_batch"
)
runner.run_all(output_format="csv")   # Each .ql → .bqrs → .csv
```

**Option C: Run queries across multiple databases**

```python
import os
from src.codeql.runner import MultiDBRunner
from src.config import CODEQL_DATABASES

# Collect all .ql files
ql_files = []
for root, _, files in os.walk("queries"):
    for f in files:
        if f.endswith('.ql'):
            ql_files.append(os.path.join(root, f))

# Run against all configured databases
runner = MultiDBRunner(
    queries_root="queries",
    output_root="data/results/stage3/multi_db"
)
runner.run_all_databases(
    db_names=list(CODEQL_DATABASES.values()),
    ql_files=ql_files
)
```

### Utility Functions

**CSV Operations:**

```python
from src.utils.csv_utils import (
    deduplicate_and_filter,
    merge_csvs,
    count_csv_files,
    compute_is_present_sum
)

# Deduplicate and filter against groundtruth
deduplicate_and_filter(
    input_csv="data/results/stage1/vulnerable_functions_summary.csv",
    output_csv="data/results/stage1/filtered_taint_functions.csv",
    groundtruth_csv="data/groundtruths/imagemagick_functions_gt.csv"
)

# Merge two CSV files
merge_csvs("file1.csv", "file2.csv", "merged.csv")

# Sum a column in a CSV
total = compute_is_present_sum("data/results/stage3/summary_result.csv", column="is_present")
```

**SARIF Processing:**

```python
from src.utils.sarif_utils import batch_process_sarif, generate_summary_csv

# Process all SARIF files in a directory → per-file CSVs
batch_process_sarif(
    sarif_dir="data/results/stage3/imagemagick",
    function_csv="data/groundtruths/imagemagick_functions_gt.csv",
    output_dir="data/results/stage3/sarif_parsed"
)

# Aggregate multiple CSVs into a summary (function × query matrix)
generate_summary_csv(
    result_dir="data/results/stage3/sarif_parsed",
    output_path="data/results/stage3/summary.csv",
    sort_by="total"                   # 'total' | 'max' | 'function'
)
```

---

## Module Reference

### `src/codeql/` — CodeQL Integration

#### `queries.py` — QL Templates & Predicates

Provides CodeQL query templates and pre-built target function predicate lists.

**YAML Model Templates:**

| Template | Purpose | Taint Token in Output |
|----------|---------|----------------------|
| `SourceModel` | Data source entry point | `"local"` |
| `SinkModel` | Data sink exit point | `"remote-sink"` |
| `SummaryModel` | Taint propagation through | `"taint"` |

Usage:
```python
from src.codeql.queries import SourceModel, SinkModel, SummaryModel

# Each uses {function_name} as a placeholder
source_entry = SourceModel.format(function_name="TIFFOpen")
# → YAML block for a sourceModel entry
```

**QL Query Templates:**

| Template | Direction | Purpose |
|----------|-----------|---------|
| `SOURCE_SINK_SEARCH` | Bidirectional | Full taint tracking: sources → function → sinks |
| `SOURCE_ONLY` | Downstream | Track data from function to ultimate sinks |
| `SINK_ONLY` | Upstream | Track data from sources into the function |

Each template uses `{function_name}` as a placeholder that gets substituted during `.ql` file generation.

**Pre-built Target Function Predicates** (`predicate targetFunctions(string funcName) { ... }`):

| Variable | Project | Functions |
|----------|---------|-----------|
| `imagemagick_targetFunctions` | ImageMagick | 500+ |
| `libraw_targetFunctions` | LibRaw | 250+ |
| `libtiff_targetFunctions` | LibTIFF | 80+ |
| `wolfssl_targetFunctions` | WolfSSL | 200+ |

These are hand-curated lists used for CodeQL queries that need explicit function targets.

#### `runner.py` — Query Execution

| Class | Purpose |
|-------|---------|
| `CodeQLRunner` | Run single `.ql` or `.qls` queries against one database |
| `BatchRunner(CodeQLRunner)` | Run all `.ql` files in a directory |
| `MultiDBRunner` | Run queries across multiple databases |

**CodeQLRunner Methods:**

```python
runner = CodeQLRunner(db_name="ImageMagick", output_root="./results")

runner.run_query_sarif(query_path, output_path,
    model_pack=None,         # e.g., "my-models/my-cpp-model-pack"
    additional_packs=None,   # e.g., "/path/to/Mymodels"
    rerun=True               # Force re-analysis even if cached
) → (success: bool, error: str | None)

runner.run_query_bqrs(ql_path, bqrs_path) → (success: bool, error: str | None)

runner.bqrs_to_csv(bqrs_path, csv_path)    # Convert intermediate → CSV
```

#### `yaml_builder.py` — YAML Model File Generation

```python
# Generate CodeQL model YAML from CSV
generate_yaml_from_csv(csv_path, output_path) → str

# Modify existing YAML (e.g., change sourceModel tag from 'local' to 'remote')
modify_yaml_file(input_path, output_path, changes={"sourceModel": True})
```

### `src/llm/` — LLM Integration

#### `client.py` — OpenAI API Wrapper

```python
from src.llm.client import chat

response = chat(
    messages=[
        {"role": "system", "content": "You are a security analyst."},
        {"role": "user", "content": "Analyze this function: read_image()"}
    ],
    model="gpt-4o-mini",             # Optional override
    temperature=0.2,                  # Lower = more deterministic
    max_tokens=1000,
    response_format={"type": "json_object"}  # Optional: force JSON mode
)
# Returns: str (response text), or "" on failure
```

All API parameters (key, base URL, model) are read from `src/config.py` → environment variables.

#### `prompts.py` — Centralized Prompt Templates

| Template | Stage | Purpose |
|----------|-------|---------|
| `STAGE1_EXTRACT_FUNCTIONS` | 1 | Extract function names + taint roles from docs |
| `STAGE2_TAINT_SPEC` | 2 | Generate CodeQL model specs with data-flow parameter mapping |
| `STAGE2_EXTRACT_FUNC_NAMES` | 2 (alt) | Simple function name extraction without role classification |

All templates use `{content}`, `{project}`, `{file}`, or `{func}` as format placeholders.

### `src/stage1_extract/` — Function Extraction

#### `extract_functions_from_docs(input_csv, output_dir, model="gpt-3.5-turbo")` → Path

Main Stage 1 entry point. Reads document snippets from a CSV, sends each to GPT, and saves aggregated results.

**Parameters:**
- `input_csv` — CSV file with a `content` column (one document chunk per row)
- `output_dir` — Directory for raw GPT responses + summary CSV
- `model` — GPT model name (default: `"gpt-3.5-turbo"`)

**Returns:** `Path` to the generated `vulnerable_functions_summary.csv`

**Internal helpers:**
- `_query_gpt(content, index, output_dir, model)` — Queries GPT for one snippet, saves raw response
- `_parse_response(response_text)` — Robust JSON parsing with fallback for malformed responses

### `src/stage2_specification/` — Specification Generation

#### `generate_specifications(csv_path, output_dir, project, model="gpt-4o-mini")` → Tuple

Generates three CodeQL model YAML files (source, sink, summary) from a CSV of functions.

**Parameters:**
- `csv_path` — CSV with `function_name` and `file_name` columns (output from Stage 1)
- `output_dir` — Directory for the three output `.yml` files
- `project` — Project name for prompt context (e.g., `"ImageMagick"`)
- `model` — GPT model (default: `"gpt-4o-mini"` — needs better reasoning)

**Returns:** `(source_yml_path, sink_yml_path, summary_yml_path)`

#### `generate_from_file(input_file, output_dir, template=None)` — Convenience

Reads function names from a text file (one per line) and generates `.ql` query files.

### `src/utils/` — Shared Utilities

#### `csv_utils.py`

| Function | Description |
|----------|-------------|
| `deduplicate_and_filter(input, output, groundtruth, subset)` | Deduplicate CSV, filter to groundtruth functions only |
| `merge_csvs(file1, file2, output, drop_duplicates)` | Concatenate two CSV files |
| `count_csv_files(directory)` | Count CSV files recursively |
| `compute_is_present_sum(csv_path, column)` | Sum values in a column |

#### `sarif_utils.py`

| Function | Description |
|----------|-------------|
| `load_function_names(csv_path)` | Load function→metadata mapping from CSV |
| `process_sarif_file(sarif_path, function_data)` | Extract function matches from one SARIF |
| `batch_process_sarif(sarif_dir, function_csv, output_dir)` | Process all SARIF files in a directory |
| `generate_summary_csv(result_dir, output_path, sort_by)` | Build function × query presence matrix |

---

## Data Formats

### Stage 1 Input: Document CSV

```csv
content
"LibRaw::dcraw_clear_mem clears memory allocated for raw image data processing..."
"The bad_pixels function corrects dead or hot pixels in raw sensor data..."
```

### Stage 1 Output: Functions Summary CSV

```csv
doc_index,function_name,taint_role,reason,source_text
0,dcraw_clear_mem,Source,"Reads untrusted image data","LibRaw::dcraw_clear_mem clears memory..."
0,bad_pixels,Inter_procedural_API,"Processes image data","bad_pixels function corrects..."
```

### Stage 2 Output: CodeQL Model YAML

```yaml
extensions:
  - addsTo:
      pack: codeql/cpp-all
      extensible: sourceModel
    data:
      - ["", "", false, "TIFFOpen", "", "", "Argument[*0]", "local", "manual"]
  - addsTo:
      pack: codeql/cpp-all
      extensible: sinkModel
    data:
      - ["", "", false, "TIFFClose", "", "", "Argument[*0]", "remote-sink", "manual"]
  - addsTo:
      pack: codeql/cpp-all
      extensible: summaryModel
    data:
      - ["", "", false, "TIFFReadRGBAImage", "", "", "Argument[*0]", "ReturnValue", "taint", "manual"]
```

### Groundtruth CSV Format

```csv
function_name,file_name,cve
AcquireQuantumMemory,MagickCore/memory.c,CVE-2016-8862
ReadPSDChannelZip,coders/psd.c,CVE-2014-1958
```

### SARIF Result → Per-Query CSV

```csv
function_name,is_present
AcquireQuantumMemory,1
TIFFOpen,0
```

### Aggregated Summary CSV

```csv
function_name,query1,query2,query3,total,max
AcquireQuantumMemory,15,8,3,26,15
TIFFOpen,0,2,1,3,2
```

---

## Supported Target Projects

| Project | Language | Description | Tracked Functions |
|---------|----------|-------------|-------------------|
| **ImageMagick** | C | Image processing and conversion library | 500+ |
| **LibRaw** | C++ | Raw image format decoding library | 250+ |
| **LibTIFF** | C | TIFF image format library | 80+ |
| **WolfSSL** | C | Embedded TLS/SSL cryptographic library | 200+ |

Each supported project has:
- Function name lists in `data/function_names/`
- Groundtruth datasets in `data/groundtruths/`
- Pre-built QL query files in `queries/<project>/`

---

## Troubleshooting

### CodeQL Issues

**"CodeQL CLI not found"**
```bash
which codeql
ls -la /path/to/codeql           # Verify the path
# Update .env: CODEQL_CLI=/correct/path/to/codeql
```

**"Database not found"**
```bash
codeql database list              # List all known databases
# Check that the database directory name matches CODEQL_DATABASES in config.py
```

**"No .ql files found"**
```bash
find queries/ -name "*.ql" | wc -l   # Should be > 0
```

### LLM / GPT Issues

**"API key not set"**
```bash
echo $OPENAI_API_KEY              # Verify environment variable
source .env                       # Or re-load from .env file
export OPENAI_API_KEY="sk-xxx"    # Or set directly
```

**Rate limiting or API errors**
- The Stage 1 extractor saves raw GPT responses to disk — you can inspect and resume
- Use `gpt-3.5-turbo` for Stage 1 (cheaper, faster) and `gpt-4o-mini` for Stage 2 (needs more precision)
- Consider adding `time.sleep()` between requests if hitting rate limits

**JSON parse errors in Stage 1 output**
- The `_parse_response()` function includes fallback logic for common format issues
- Inspect raw responses: `data/results/stage1/<project>/llm_response_*.txt`
- Adjust the prompt in `src/llm/prompts.py` if format compliance is consistently poor

### YAML Model Issues

**"CodeQL doesn't load the model"**
- Verify YAML syntax: each data line must start with exactly `      - [`
- Check that `pack: codeql/cpp-all` matches CodeQL's expected pack name
- Ensure the YAML file is in CodeQL's model search path

**"Wrong model classification"**
- Use `modify_yaml_file()` to batch-fix model tags:
```python
from src.codeql.yaml_builder import modify_yaml_file
modify_yaml_file(
    "config/models/imagemagick_source.yml",
    "config/models/imagemagick_source.modified.yml",
    changes={"sourceModel": "local_to_remote"}
)
```

---

## Contributing

The project follows a three-stage pipeline architecture. To add support for a new target library:

1. Add function name lists to `data/function_names/`
2. Add groundtruth data (if available) to `data/groundtruths/`
3. Add the database name mapping to `src/config.py` → `CODEQL_DATABASES`
4. Add the project to `PROJECTS` in `src/config.py`
5. Add target function predicates to `src/codeql/queries.py`
6. Generate QL queries from function names via `src/stage2_specification/ql_generator.py`
