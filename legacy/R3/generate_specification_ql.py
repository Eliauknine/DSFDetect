import os
import csv
import ast
from collections import defaultdict
from pathlib import Path
import codeql_queries

# 配置输入输出目录
INPUT_DIR = "R2/myquery/ql_source_sink_extract/result/result_specification_extract_gpt/imagemagic"  # ← 更新为你的路径
OUTPUT_DIR = "R3/ql_path_search/imagemagic/search_ql"

# 确保输出目录存在
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)


def extract_functions_from_structured_csv(csv_path):
    """从结构化CSV中提取函数信息，并细化到参数位置"""
    source_of_function_call = set()
    source_of_function_argument = defaultdict(set)
    sink_of_function_argument = defaultdict(set)

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            func_name = row.get('function_name', '').strip()
            taint_role = row.get('taint_role', '').strip()
            arg_pos_raw = row.get('arg_pos', '').strip()

            if not func_name or not taint_role or not arg_pos_raw:
                continue

            try:
                arg_pos = ast.literal_eval(arg_pos_raw)
                if not isinstance(arg_pos, list):
                    continue
            except (SyntaxError, ValueError):
                continue

            if taint_role == "Source":
                if arg_pos == ['func_call']:
                    source_of_function_call.add(func_name)
                else:
                    for arg in arg_pos:
                        source_of_function_argument[func_name].add(arg)
            elif taint_role == "Sink":
                if arg_pos == ['func_call']:
                    # 如果你不希望支持 Sink 的 func_call，可跳过
                    continue
                for arg in arg_pos:
                    sink_of_function_argument[func_name].add(arg)

    return source_of_function_call, source_of_function_argument, sink_of_function_argument



def generate_codeql_content(csv_name, source_func_calls, source_arguments, sink_arguments):
    sections = []

    if csv_name.endswith('_source_sink'):
        function_name = csv_name[:-len('_source_sink')]
    else:
        function_name = csv_name

    sections.append(f"""/**
 • @name Function presence in data flow paths
 • @description Checks if specific functions appear in data flow paths
 • @kind table
 • @id cpp/function-presence-in-paths
 */

import cpp
import semmle.code.cpp.dataflow.new.DataFlow
import semmle.code.cpp.dataflow.new.TaintTracking
""")

    sections.append(codeql_queries.imagemagick_targetFunctions)

    # 1. Source Call
    source_predicates = []
    if source_func_calls:
        source_call_list = ',\n            '.join(f'"{func}"' for func in sorted(source_func_calls))
        sections.append(f"""// ----------- Source: Function Call -----------
predicate isSourceFunctionCall(DataFlow::Node src) {{
    exists(FunctionCall fc |
        fc = src.asExpr() and
        fc.getTarget().getName() in [
            {source_call_list}
        ]
    )
}}""")
        source_predicates.append("isSourceFunctionCall(src)")

    # 2. Source Argument
    if source_arguments:
        arg_conditions = []
        for func in sorted(source_arguments):
            for arg in sorted(source_arguments[func], key=int):
                arg_conditions.append(f'(fc.getTarget().getName() = "{func}" and idx = {arg})')
        arg_str = ' or\n            '.join(arg_conditions)
        sections.append(f"""
// ----------- Source: Function Argument -----------
predicate isSourceFunctionArgument(DataFlow::Node src) {{
    exists(FunctionCall fc, int idx |
        src.asExpr() = fc.getArgument(idx) and
        (
            {arg_str}
        )
    )
}}""")
        source_predicates.append("isSourceFunctionArgument(src)")

    if not source_predicates:
        return None

    # 3. Source Global
    or_conditions = ' or\n    '.join(source_predicates)
    sections.append(f"""
predicate isSourceGlobal(DataFlow::Node src) {{
    {or_conditions}
}}""")

    # 4. Sink by argument
    if not sink_arguments:
        return None

    sink_arg_conditions = []
    for func in sorted(sink_arguments):
        for arg in sorted(sink_arguments[func], key=int):
            sink_arg_conditions.append(f'(fc.getTarget().getName() = "{func}" and idx = {arg})')
    sink_arg_str = ' or\n            '.join(sink_arg_conditions)

    sections.append(f"""
// ----------- Sink: Argument Specific -----------
predicate isSinkArgument(DataFlow::Node sink) {{
    exists(FunctionCall fc, int idx |
        sink.asExpr() = fc.getArgument(idx) and
        (
            {sink_arg_str}
        )
    )
}}""")

    # 5. 配置类
    sections.append("""
class CustomSourceSinkConfiguration extends TaintTracking::Configuration {
    CustomSourceSinkConfiguration() { this = "CustomSourceSinkConfiguration" }

    override predicate isSource(DataFlow::Node source) {
        isSourceGlobal(source)
    }

    override predicate isSink(DataFlow::Node sink) {
        isSinkArgument(sink)
    }
}
""")

    # 6. 路径检测 + 查询主体
    sections.append("""
predicate isFunctionInPath(string funcName, DataFlow::Node source, DataFlow::Node sink, CustomSourceSinkConfiguration config) {
    exists(DataFlow::Node n, FunctionCall fc |
        (n = source or config.hasFlow(source, n) or n = sink) and
        config.hasFlow(source, sink) and
        fc.getTarget().getName() = funcName and
        (
            fc = n.asExpr() or
            fc.getAnArgument() = n.asExpr()
        )
    )
}

from
    string functionName,
    int isPresent
where
    targetFunctions(functionName) and
    (
        if exists(DataFlow::Node source, DataFlow::Node sink, CustomSourceSinkConfiguration config |
            config.hasFlow(source, sink) and
            isFunctionInPath(functionName, source, sink, config)
        )
        then isPresent = 1
        else isPresent = 0
    )
select
    functionName as function_name,
    isPresent as is_present
""")

    return '\n'.join(sections)



def process_csv_files():
    """处理所有CSV文件"""
    csv_files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.csv')]
    generated_count = 0

    for csv_file in csv_files:
        csv_path = os.path.join(INPUT_DIR, csv_file)
        csv_name = os.path.splitext(csv_file)[0]

        source_functions, sink_functions, source_arguments = extract_functions_from_structured_csv(csv_path)

        ql_content = generate_codeql_content(csv_name, source_functions, sink_functions, source_arguments)

        if ql_content is not None:
            output_file = f"{csv_name}_path_num.ql"
            output_path = os.path.join(OUTPUT_DIR, output_file)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(ql_content)

            print(f"✅ Generated: {output_path}")
            generated_count += 1
        else:
            print(f"⏭️ Skipped: {csv_file} (no valid source/sink functions found)")

    print(f"\n📊 Processed {len(csv_files)} CSV files. Generated {generated_count} QL files in {OUTPUT_DIR}")


if __name__ == "__main__":
    process_csv_files()
