"""
DSFDetect centralized configuration.

All paths, API keys, and tunable parameters are managed here.
Sensitive values are read from environment variables with fallback defaults.
"""
import os
from pathlib import Path

# ---- Project root ----
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ---- Paths (relative to project root) ----
DATA_DIR = PROJECT_ROOT / "data"
FUNCTION_NAMES_DIR = DATA_DIR / "function_names"
GROUNDTRUTHS_DIR = DATA_DIR / "groundtruths"
INPUT_DOCS_DIR = DATA_DIR / "input_docs"
RESULTS_DIR = DATA_DIR / "results"

CONFIG_DIR = PROJECT_ROOT / "config"
MODELS_DIR = CONFIG_DIR / "models"
TEMPLATES_DIR = CONFIG_DIR / "templates"

QUERIES_DIR = PROJECT_ROOT / "queries"
THIRD_PARTY_DIR = PROJECT_ROOT / "third_party"

# ---- CodeQL CLI ----
CODEQL_CLI = os.environ.get("CODEQL_CLI", "/Users/mycp/CodeQL/codeql-cli/codeql/codeql")
CODEQL_DB_DIR = os.environ.get("CODEQL_DB_DIR", "/Users/mycp/CodeQL/databases")
CODEQL_REPO_DIR = os.environ.get("CODEQL_REPO_DIR", "/Users/mycp/CodeQL/codeql-repo/codeql-main")

# ---- OpenAI / LLM API ----
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1/")
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-3.5-turbo")

# ---- CodeQL databases (per project) ----
CODEQL_DATABASES = {
    "imagemagick": "ImageMagick",
    "libraw": "libraw-db",
    "libtiff": "libtiff-db",
    "wolfssl": "wolfssl-db",
}

# ---- Supported projects ----
PROJECTS = ["imagemagick", "libraw", "libtiff", "wolfssl"]

# ---- Output ----
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "data" / "results"
