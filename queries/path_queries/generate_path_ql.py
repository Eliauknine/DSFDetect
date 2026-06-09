import os
import csv
import re
from collections import defaultdict
from pathlib import Path
import codeql_queries

# 配置输入输出目录
INPUT_DIR = "/Users/mycp/CodeQL/result/source_sink_extract/wolfssl"
OUTPUT_DIR = "/Users/mycp/CodeQL/codeql-repo/codeql-main/cpp/ql/src/Security/CWE/node_wolfssl/wolfssl"

# 确保输出目录存在
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

# 正则表达式模式
source_function_call_pattern = r"Source: Function call: (\w+)"
sink_function_pattern = r"Sink: Argument of (\w+)"
source_function_argument_pattern = r"Source: Argument (\d+) of (\w+)"


def extract_functions_from_csv(csv_path):
    """从CSV文件中提取三类函数信息"""
    source_of_function_call = set()
    source_of_function = set()
    source_of_function_argument = defaultdict(set)

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if 'col2' not in row:
                continue

            text = row['col2']

            # 提取Source Function Calls
            if match := re.search(source_function_call_pattern, text):
                source_of_function_call.add(match.group(1))

            # 提取Sink Functions
            if match := re.search(sink_function_pattern, text):
                source_of_function.add(match.group(1))

            # 提取Source Function Arguments
            if match := re.search(source_function_argument_pattern, text):
                func_name = match.group(2)
                arg_index = match.group(1)
                source_of_function_argument[func_name].add(arg_index)

    return source_of_function_call, source_of_function, source_of_function_argument


def generate_codeql_content(csv_name, source_functions, sink_functions, source_arguments):
    """生成CodeQL查询内容"""
    sections = []

    # Remove "_source_sink" suffix from csv_name to get function_name
    if csv_name.endswith('_source_sink'):
        function_name = csv_name[:-len('_source_sink')]
    else:
        function_name = csv_name  # fallback if suffix not present

    # 1. 文件头
    sections.append(f"""/**
 * @name Function presence in data flow paths
 * @description Checks if specific functions appear in data flow paths
 * @kind table
 * @id cpp/function-presence-in-paths
 */

import cpp
import semmle.code.cpp.dataflow.new.DataFlow
import semmle.code.cpp.dataflow.new.TaintTracking

""")
    sections.append(codeql_queries.wolfssl_targetFunctions)
    # 2. Source Function Call
    source_predicates = []
    if source_functions:
        source_call_list = ',\n            '.join(f'"{func}"' for func in sorted(source_functions))
        sections.append(f"""// ----------- Source Definitions -----------
predicate isSourceFunctionCall(DataFlow::Node src) {{
    exists(FunctionCall fc |
        fc = src.asExpr() and
        fc.getTarget().getName() in [
            {source_call_list}
        ]
    )
}}""")
        source_predicates.append("isSourceFunctionCall(src)")

    # 3. Source Function Argument
    if source_arguments:
        arg_conditions = []
        for func in sorted(source_arguments):
            for arg in sorted(source_arguments[func], key=int):
                arg_conditions.append(f'(fc.getTarget().getName() = "{func}" and idx = {arg})')
        arg_conditions_str = ' or\n            '.join(arg_conditions)
        sections.append(f"""
predicate isSourceFunctionArgument(DataFlow::Node src) {{
    exists(FunctionCall fc, int idx |
        src.asExpr() = fc.getArgument(idx) and
        (
            {arg_conditions_str}
        )
    )
}}""")
        source_predicates.append("isSourceFunctionArgument(src)")

    # 如果没有有效的源谓词，直接返回None
    if not source_predicates:
        return None

    # 4. Global Source Predicate
    # 修改这里：将换行符放在f-string之外
    or_conditions = ' or\n    '.join(source_predicates)
    sections.append(f"""
predicate isSourceGlobal(DataFlow::Node src) {{
    {or_conditions}
}}""")

    # 5. Sink Definition
    if not sink_functions:
        return None  # 没有有效的接收器定义，跳过生成文件

    sink_list = ',\n            '.join(f'"{func}"' for func in sorted(sink_functions))
    sections.append(f"""
// ----------- Sink Definitions -----------
predicate isSinkGlobal(DataFlow::Node sink) {{
    exists(FunctionCall fc |
        sink.asExpr() = fc.getAnArgument() and
        fc.getTarget().getName() in [
            {sink_list}
        ]
    )
}}""")

    # 6. 固定配置和查询部分
    sections.append("""
class CustomSourceSinkConfiguration extends TaintTracking::Configuration {
    CustomSourceSinkConfiguration() { this = "CustomSourceSinkConfiguration" }

    override predicate isSource(DataFlow::Node source) {
        isSourceGlobal(source)
    }

    override predicate isSink(DataFlow::Node sink) {
        isSinkGlobal(sink)
    }
}

// 检查函数是否出现在路径中的任何节点
predicate isFunctionInPath(string funcName, DataFlow::Node source, DataFlow::Node sink, CustomSourceSinkConfiguration config) {
    exists(DataFlow::Node n, FunctionCall fc |
        // 检查节点是否在路径上
        (n = source or config.hasFlow(source, n) or n = sink) and
        config.hasFlow(source, sink) and
        // 检查函数调用
        fc.getTarget().getName() = funcName and
        (
            fc = n.asExpr() or
            fc.getAnArgument() = n.asExpr()
        )
    )
}
""")
    sections.append(f"""
// ----------- Main Query -----------
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

        # 提取函数信息
        source_functions, sink_functions, source_arguments = extract_functions_from_csv(csv_path)

        # 生成QL内容
        ql_content = generate_codeql_content(csv_name, source_functions, sink_functions, source_arguments)

        # 只有当有有效的源和接收器时才生成文件
        if ql_content is not None:
            output_file = f"{csv_name}_path_num.ql"
            output_path = os.path.join(OUTPUT_DIR, output_file)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(ql_content)

            print(f"Generated: {output_path}")
            generated_count += 1
        else:
            print(f"Skipped: {csv_file} (no valid source/sink functions found)")

    print(f"\nProcessed {len(csv_files)} CSV files. Generated {generated_count} QL files in {OUTPUT_DIR}")


if __name__ == "__main__":
    process_csv_files()



# import os
# import csv
# import re
# from collections import defaultdict
# from pathlib import Path
#
# # 配置输入输出目录
# INPUT_DIR = "/Users/mycp/CodeQL/result/ImageMagick"
# OUTPUT_DIR = "path_ql/path_num/path_num_imagemagick"
#
# # 确保输出目录存在
# Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
#
# # 正则表达式模式
# source_function_call_pattern = r"Source: Function call: (\w+)"
# sink_function_pattern = r"Sink: Argument of (\w+)"
# source_function_argument_pattern = r"Source: Argument (\d+) of (\w+)"
#
#
# def extract_functions_from_csv(csv_path):
#     """从CSV文件中提取三类函数信息"""
#     source_of_function_call = set()
#     source_of_function = set()
#     source_of_function_argument = defaultdict(set)
#
#     with open(csv_path, 'r', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             if 'col2' not in row:
#                 continue
#
#             text = row['col2']
#
#             # 提取Source Function Calls
#             if match := re.search(source_function_call_pattern, text):
#                 source_of_function_call.add(match.group(1))
#
#             # 提取Sink Functions
#             if match := re.search(sink_function_pattern, text):
#                 source_of_function.add(match.group(1))
#
#             # 提取Source Function Arguments
#             if match := re.search(source_function_argument_pattern, text):
#                 func_name = match.group(2)
#                 arg_index = match.group(1)
#                 source_of_function_argument[func_name].add(arg_index)
#
#     return source_of_function_call, source_of_function, source_of_function_argument
#
#
# def generate_codeql_content(csv_name, source_functions, sink_functions, source_arguments):
#     """生成CodeQL查询内容"""
#     sections = []
#
#     # Remove "_source_sink" suffix from csv_name to get function_name
#     if csv_name.endswith('_source_sink'):
#         function_name = csv_name[:-len('_source_sink')]
#     else:
#         function_name = csv_name  # fallback if suffix not present
#
#     # 1. 文件头
#     sections.append(f"""/**
#  * @name Custom source to sink path search for {csv_name}
#  * @description Finds paths from custom defined sources to sinks
#  * @kind path-problem
#  * @problem.severity warning
#  * @precision high
#  * @id cpp/custom-source-sink-path
#  * @tags security
#  */
#
# import cpp
# import semmle.code.cpp.dataflow.new.DataFlow
# import semmle.code.cpp.dataflow.new.TaintTracking
# import DataFlow::PathGraph
#
# // ----------- Source Definitions -----------""")
#
#     # 2. Source Function Call
#     source_predicates = []
#     if source_functions:
#         source_call_list = ',\n            '.join(f'"{func}"' for func in sorted(source_functions))
#         sections.append(f"""
# predicate isSourceFunctionCall(DataFlow::Node src) {{
#     exists(FunctionCall fc |
#         fc = src.asExpr() and
#         fc.getTarget().getName() in [
#             {source_call_list}
#         ]
#     )
# }}""")
#         source_predicates.append("isSourceFunctionCall(src)")
#
#     # 3. Source Function Argument
#     if source_arguments:
#         arg_conditions = []
#         for func in sorted(source_arguments):
#             for arg in sorted(source_arguments[func], key=int):
#                 arg_conditions.append(f'(fc.getTarget().getName() = "{func}" and idx = {arg})')
#         arg_conditions_str = ' or\n            '.join(arg_conditions)
#         sections.append(f"""
# predicate isSourceFunctionArgument(DataFlow::Node src) {{
#     exists(FunctionCall fc, int idx |
#         src.asExpr() = fc.getArgument(idx) and
#         (
#             {arg_conditions_str}
#         )
#     )
# }}""")
#         source_predicates.append("isSourceFunctionArgument(src)")
#
#     # 如果没有有效的源谓词，直接返回None
#     if not source_predicates:
#         return None
#
#     # 4. Global Source Predicate
#     # 修改这里：将换行符放在f-string之外
#     or_conditions = ' or\n    '.join(source_predicates)
#     sections.append(f"""
# predicate isSourceGlobal(DataFlow::Node src) {{
#     {or_conditions}
# }}""")
#
#     # 5. Sink Definition
#     if not sink_functions:
#         return None  # 没有有效的接收器定义，跳过生成文件
#
#     sink_list = ',\n            '.join(f'"{func}"' for func in sorted(sink_functions))
#     sections.append(f"""
# // ----------- Sink Definitions -----------
# predicate isSinkGlobal(DataFlow::Node sink) {{
#     exists(FunctionCall fc |
#         sink.asExpr() = fc.getAnArgument() and
#         fc.getTarget().getName() in [
#             {sink_list}
#         ]
#     )
# }}""")
#
#     # 6. 固定配置和查询部分
#     sections.append("""
# // ----------- Path Query Configuration -----------
# class CustomSourceSinkConfiguration extends TaintTracking::Configuration {
#     CustomSourceSinkConfiguration() { this = "CustomSourceSinkConfiguration" }
#
#     override predicate isSource(DataFlow::Node source) {
#         isSourceGlobal(source)
#     }
#
#     override predicate isSink(DataFlow::Node sink) {
#         isSinkGlobal(sink)
#     }
#
#     override predicate isAdditionalTaintStep(DataFlow::Node node1, DataFlow::Node node2) {
#         // Assignment
#         exists(AssignExpr assign |
#             node1.asExpr() = assign.getRValue() and
#             node2.asExpr() = assign.getLValue()
#         )
#         or
#         // Parameter passing
#         exists(FunctionCall call, int i |
#             node1.asExpr() = call.getArgument(i) and
#             exists(Parameter p |
#                 p = call.getTarget().getParameter(i) and
#                 node2.asParameter() = p
#             )
#         )
#         or
#         // Return value
#         exists(FunctionCall call, ReturnStmt ret |
#             ret.getEnclosingFunction() = call.getTarget() and
#             node1.asExpr() = ret.getExpr() and
#             node2.asExpr() = call
#         )
#     }
# }
#
# // Get function name
# string getFunctionName(DataFlow::Node node) {
#     exists(FunctionCall fc |
#         (node.asExpr() = fc or node.asExpr() = fc.getAnArgument()) and
#         result = fc.getTarget().getName()
#     )
#     or
#     exists(Parameter p |
#         node.asParameter() = p and
#         result = p.getFunction().getName()
#     )
# }
# """)
#     sections.append(f"""
# // ----------- Main Query -----------
# from
#     DataFlow::PathNode source,
#     DataFlow::PathNode sink,
#     CustomSourceSinkConfiguration config,
#     string sourceInfo,
#     string sinkInfo,
#     // 添加新的变量用于统计
#     int totalPaths,
#     int functionPaths
# where
#     config.hasFlowPath(source, sink) and
#     sourceInfo = getFunctionName(source.getNode()) and
#     sinkInfo = getFunctionName(sink.getNode()) and
#     // 计算总路径数
#     totalPaths = count(DataFlow::PathNode src, DataFlow::PathNode snk |
#         config.hasFlowPath(src, snk)
#     ) and
#     // 计算包含 AcquireImage 的路径数
#     functionPaths = count(DataFlow::PathNode src, DataFlow::PathNode snk |
#         config.hasFlowPath(src, snk) and
#         getFunctionName(src.getNode()) = "{function_name}"
#     )
# select
#     sink.getNode(),
#     source,
#     sink,
#     "Data flow path from " + sourceInfo + " to " + sinkInfo + "\\n" +
#     "Total paths: " + totalPaths.toString() + "\\n" +
#     "Paths with AcquireImage: " + functionPaths.toString() + "\\n" +
#     "Percentage: " + ((100.0 * functionPaths) / totalPaths).toString() + "%",
#     source.getNode().getLocation().toString(),
#     sourceInfo,
#     sink.getNode().getLocation().toString(),
#     sinkInfo
#
# """)
#
#     return '\n'.join(sections)
#
#
# def process_csv_files():
#     """处理所有CSV文件"""
#     csv_files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.csv')]
#     generated_count = 0
#
#     for csv_file in csv_files:
#         csv_path = os.path.join(INPUT_DIR, csv_file)
#         csv_name = os.path.splitext(csv_file)[0]
#
#         # 提取函数信息
#         source_functions, sink_functions, source_arguments = extract_functions_from_csv(csv_path)
#
#         # 生成QL内容
#         ql_content = generate_codeql_content(csv_name, source_functions, sink_functions, source_arguments)
#
#         # 只有当有有效的源和接收器时才生成文件
#         if ql_content is not None:
#             output_file = f"{csv_name}_path_num.ql"
#             output_path = os.path.join(OUTPUT_DIR, output_file)
#
#             with open(output_path, 'w', encoding='utf-8') as f:
#                 f.write(ql_content)
#
#             print(f"Generated: {output_path}")
#             generated_count += 1
#         else:
#             print(f"Skipped: {csv_file} (no valid source/sink functions found)")
#
#     print(f"\nProcessed {len(csv_files)} CSV files. Generated {generated_count} QL files in {OUTPUT_DIR}")
#
#
# if __name__ == "__main__":
#     process_csv_files()


# import csv
# import re
# from collections import defaultdict
#
# # 输入文件路径
# input_csv = "/Users/mycp/CodeQL/result/ImageMagick/AcquireQuantumMemory_source_sink.csv"
#
# # 正则表达式模式
# source_function_call_pattern = r"Source: Function call: (\w+)"
# sink_function_pattern = r"Sink: Argument of (\w+)"
# source_function_argument_pattern = r"Source: Argument (\d+) of (\w+)"
#
# # 存储提取结果
# source_of_function_call = set()
# source_of_function = set()
# source_of_function_argument = defaultdict(set)
#
#
# def extract_info(text):
#     """从文本中提取三种关键信息"""
#     if match := re.search(source_function_call_pattern, text):
#         source_of_function_call.add(match.group(1))
#     if match := re.search(sink_function_pattern, text):
#         source_of_function.add(match.group(1))
#     if match := re.search(source_function_argument_pattern, text):
#         source_of_function_argument[match.group(2)].add(match.group(1))
#
#
# def generate_codeql_query():
#     """生成完全符合模板的CodeQL查询"""
#     # 生成source函数列表（保持原模板中的2个示例）
#     source_call_list = sorted(source_of_function_call)
#     source_call_functions = ',\n            '.join(f'"{func}"' for func in source_call_list)
#
#     # 生成带参数的source条件（保持原模板中的2个示例格式）
#     argument_conditions = []
#     for func in sorted(source_of_function_argument):
#         for arg in sorted(source_of_function_argument[func], key=int):
#             argument_conditions.append(f'(fc.getTarget().getName() = "{func}" and idx = {arg})')
#     argument_conditions_str = ' or\n            '.join(argument_conditions)
#
#     # 生成sink函数列表（保持原模板中的6个示例）
#     sink_list = sorted(source_of_function)
#     sink_functions = ',\n            '.join(f'"{func}"' for func in sink_list)
#
#     return f"""/**
#  * @name Custom source to sink path search (all-in-one)
#  * @description Finds paths from custom defined sources to sinks
#  * @kind path-problem
#  * @problem.severity warning
#  * @precision high
#  * @id cpp/custom-source-sink-path
#  * @tags security
#  */
#
# import cpp
# import semmle.code.cpp.dataflow.new.DataFlow
# import semmle.code.cpp.dataflow.new.TaintTracking
# import DataFlow::PathGraph
#
# // ----------- 源定义（原mysource.qll内容） -----------
#
# // 只知道函数名的source
# predicate isSourceFunctionCall(DataFlow::Node src) {{
#     exists(FunctionCall fc |
#         fc = src.asExpr() and
#         fc.getTarget().getName() in [
#             {source_call_functions}
#             // 更多函数名
#         ]
#     )
# }}
#
# // 知道函数名和参数位置的source
# predicate isSourceFunctionArgument(DataFlow::Node src) {{
#     exists(FunctionCall fc, int idx |
#         src.asExpr() = fc.getArgument(idx) and
#         (
#             {argument_conditions_str}
#             // 更多 (函数名, 参数索引) 对
#         )
#     )
# }}
#
# // 全局source谓词
# predicate isSourceGlobal(DataFlow::Node src) {{
#     isSourceFunctionCall(src) or
#     isSourceFunctionArgument(src)
# }}
#
# // 全局sink谓词
# predicate isSinkGlobal(DataFlow::Node sink) {{
#     exists(FunctionCall fc |
#         sink.asExpr() = fc.getAnArgument() and
#         fc.getTarget().getName() in [
#             {sink_functions}
#             // 更多函数名
#         ]
#     )
# }}
#
# // ----------- 路径查询主体 -----------
#
# class CustomSourceSinkConfiguration extends TaintTracking::Configuration {{
#     CustomSourceSinkConfiguration() {{ this = "CustomSourceSinkConfiguration" }}
#
#     override predicate isSource(DataFlow::Node source) {{
#         isSourceGlobal(source)
#     }}
#
#     override predicate isSink(DataFlow::Node sink) {{
#         isSinkGlobal(sink)
#     }}
#
#     override predicate isAdditionalTaintStep(DataFlow::Node node1, DataFlow::Node node2) {{
#         // 赋值
#         exists(AssignExpr assign |
#             node1.asExpr() = assign.getRValue() and
#             node2.asExpr() = assign.getLValue()
#         )
#         or
#         // 参数传递
#         exists(FunctionCall call, int i |
#             node1.asExpr() = call.getArgument(i) and
#             exists(Parameter p |
#                 p = call.getTarget().getParameter(i) and
#                 node2.asParameter() = p
#             )
#         )
#         or
#         // 返回值
#         exists(FunctionCall call, ReturnStmt ret |
#             ret.getEnclosingFunction() = call.getTarget() and
#             node1.asExpr() = ret.getExpr() and
#             node2.asExpr() = call
#         )
#     }}
# }}
#
# // 获取函数名
# string getFunctionName(DataFlow::Node node) {{
#     exists(FunctionCall fc |
#         (node.asExpr() = fc or node.asExpr() = fc.getAnArgument()) and
#         result = fc.getTarget().getName()
#     )
#     or
#     exists(Parameter p |
#         node.asParameter() = p and
#         result = p.getFunction().getName()
#     )
# }}
#
# from
#     DataFlow::PathNode source,
#     DataFlow::PathNode sink,
#     CustomSourceSinkConfiguration config,
#     string sourceInfo,
#     string sinkInfo
# where
#     config.hasFlowPath(source, sink) and
#     sourceInfo = getFunctionName(source.getNode()) and
#     sinkInfo = getFunctionName(sink.getNode())
# select
#     sink.getNode(),
#     source,
#     sink,
#     "Data flow path from " + sourceInfo + " to " + sinkInfo,
#     source.getNode().getLocation().toString(),
#     sourceInfo,
#     sink.getNode().getLocation().toString(),
#     sinkInfo
# """
#
#
# def process_csv():
#     """处理CSV文件并生成CodeQL查询"""
#     with open(input_csv, 'r', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             if 'col2' in row:
#                 extract_info(row['col2'])
#
#     # 生成并打印CodeQL查询
#     print(generate_codeql_query())
#
#
# if __name__ == "__main__":
#     process_csv()