"""
Prompt templates for all LLM interactions across the three pipeline stages.

All prompts are centralized here for easy maintenance and version control.
"""

# =============================================================================
# Stage 1: Sensitive Function Extraction
# =============================================================================

STAGE1_EXTRACT_FUNCTIONS = """
You are an expert in secure coding and C/C++ API development. Analyze the following document snippet to:
1. Identify potentially vulnerable functions
2. Determine their role in taint analysis (Source, Sink, or Inter_procedural_API)

**Definitions**:
- Source: Functions that introduce untrusted data into the program (e.g., reading user input, network data)
- Sink: Functions that consume data in a security-sensitive way (e.g., system commands, file operations)
- Inter_procedural_API: Functions that process data between sources and sinks

**Required Output Format**:
Return a SINGLE JSON array containing ALL vulnerable functions found, using this exact format:
{{
    "functions": [
        {{
            "function_name": "LibRaw::dcraw_clear_mem",
            "taint_role": "Source",
            "reason": "Reads untrusted image data"
        }},
        {{
            "function_name": "bad_pixels",
            "taint_role": "Inter_procedural_API",
            "reason": "Processes image data between input and output"
        }}
    ]
}}
If no vulnerable functions are found, return: {{"functions": []}}

**Document Content**:
{content}
"""

# =============================================================================
# Stage 2: Taint Specification Generation
# =============================================================================

STAGE2_TAINT_SPEC = """
Below is a function from the {project} project along with its file location:
File path: {file}
Function name: {func}

Based on your knowledge and understanding of {project}, determine which of the following model types best describe this function (may be multiple), and fill in the data-flow parameter parts:

1. **sourceModel**
   Represents a function that is a data source (reads from external input, files, network, user input).
   Data-flow parameter refers to the function's input parameter, e.g. Argument[*0], Argument[*1], or ReturnValue.
   Output format: - ["", "", false, "{func}", "", "", "data-flow-param", "local", "manual"]

2. **sinkModel**
   Represents a function that is a data sink or performs sensitive operations (writes to file, network send, calls dangerous APIs).
   Data-flow parameter refers to the function's sensitive input/output parameter, e.g. Argument[*0], Argument[*1], or ReturnValue.
   Output format: - ["", "", false, "{func}", "", "", "data-flow-param", "remote-sink", "manual"]

3. **summaryModel**
   Represents a function that propagates data between input parameters and return value (data-flow through).
   Data-flow parameters:
   - 4th from end: input parameter, e.g. Argument[*0], Argument[*1]
   - 3rd from end: output or return value, e.g. Argument[*0], Argument[*1], or ReturnValue
   Output format: - ["", "", false, "{func}", "", "", "input-param", "return-value", "taint", "manual"]

Important notes:
- If a function fits multiple model types, output each result on its own line.
- Output ONLY the YAML data lines (starting with "- ["), no explanations.
- Separate namespace from function name. For example, "Magick::Image::gaussianBlurChannel" should have "Magick::Image" as namespace in the first position, and "gaussianBlurChannel" as the function name.
- Do NOT include function parameters like "( const ChannelType channel_, ...)" in the function name.
- Correct example: ["MagickWand", "", false, "MagickGetImageBluePrimary", "", "", "Argument[*0]", "local", "manual"]
"""

# =============================================================================
# Stage 2: Function Name Only Extraction
# =============================================================================

STAGE2_EXTRACT_FUNC_NAMES = """
You are an expert in secure coding and C/C++ API development. Analyze the following document snippet to see if it contains function names that could lead to vulnerabilities.

**Required Output Format**:
Return a SINGLE JSON array containing ALL vulnerable functions found, using this exact format:
{{
    "functions": [
        {{"function_name": "LibRaw::dcraw_clear_mem"}},
        {{"function_name": "bad_pixels"}}
    ]
}}
If no vulnerable functions are found, return: {{"functions": []}}

**Document Content**:
{content}
"""
