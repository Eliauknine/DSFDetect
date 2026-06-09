'''存放CodeQL查询模板的文件'''

# Source分析模板
SOURCE_TEMPLATE = '''/**
 * @name {function_name} Analysis Generic
 * @description A generic query to extract detailed information about a function including its definition, parameter sources, and context
 * @kind problem
 * @problem.severity recommendation
 * @id cpp/function-analysis-generic
 */

import cpp

class TargetFunction extends Function {{
  TargetFunction() {{
    // You can modify this to match your specific function name
    this.getName() = "{function_name}"
  }}
}}

string getParameterDescription(Parameter p) {{
  exists(string paramName, string paramType |
    paramType = p.getType().toString() and
    (
      if exists(p.getName())
      then paramName = p.getName()
      else paramName = "arg" + p.getIndex().toString()
    ) |
    result = paramType + " " + paramName
  )
}}

string getArgumentDescription(FunctionCall fc, int i) {{
  exists(Expr arg |
    arg = fc.getArgument(i) |
    result = arg.toString() + " (" + arg.getType().toString() + ")"
  )
}}

string getNamespacePrefix(Function f) {{
  exists(Namespace n | n = f.getNamespace() |
    if n.getQualifiedName() = "::" or n.getQualifiedName() = ""
    then result = ""
    else result = n.getQualifiedName() + "::"
  )
  or
  not exists(f.getNamespace()) and result = ""
}}

string getDeclaringTypePrefix(Function f) {{
  if exists(f.getDeclaringType())
  then result = f.getDeclaringType().getName() + "::"
  else result = ""
}}

string getNamespaceInfo(Function f) {{
  if exists(f.getNamespace())
  then result = f.getNamespace().getQualifiedName()
  else result = "<global>"
}}

from TargetFunction f
select f,
  // Basic function information
  "Function Analysis for: " + f.getName() + "\\n" +
  "File: " + f.getFile().getBaseName() + "\\n" +
  "Line: " + f.getLocation().getStartLine().toString() + "\\n" +
  "Return Type: " + f.getType().toString() + "\\n\\n" +

  // Namespace information
  "Namespace: " + getNamespaceInfo(f) + "\\n\\n" +

  // Parameters with improved description
  "Parameters:\\n" +
  strictconcat(Parameter p | p = f.getAParameter() |
    "  " + p.getIndex() + ": " + getParameterDescription(p) + "\\n"
    order by p.getIndex()
  ) + "\\n" +

  // Function calls with argument information
  "Function Calls:\\n" +
  strictconcat(FunctionCall fc | fc.getTarget() = f |
    "  Called from " + fc.getEnclosingFunction().getName() +
    " at " + fc.getLocation().getFile().getBaseName() +
    ":" + fc.getLocation().getStartLine().toString() + "\\n" +
    strictconcat(int i | i in [0 .. fc.getNumberOfArguments() - 1] |
      "    Arg " + i + ": " + getArgumentDescription(fc, i) + "\\n"
      order by i
    )
    order by fc.getLocation().getStartLine()
  ) + "\\n" +

  // Location information
  "Location Details:\\n" +
  "  Start line: " + f.getLocation().getStartLine().toString() + "\\n" +
  "  End line: " + f.getLocation().getEndLine().toString() + "\\n" +
  "  Start column: " + f.getLocation().getStartColumn().toString() + "\\n" +
  "  End column: " + f.getLocation().getEndColumn().toString() + "\\n" +

  // Declaration information with full namespace
  "Declaration:\\n" +
  "  " + getNamespacePrefix(f) + getDeclaringTypePrefix(f) + f.getName() +
  "(" + concat(Parameter p | p = f.getAParameter() | getParameterDescription(p) order by p.getIndex()) + ")" 
'''

# Sink分析模板
SINK_TEMPLATE = '''/**
 * @name {function_name} Analysis for Sink
 * @description A specialized query to extract information about a function that is marked as a sink,
 *              focusing on data flow, dangerous operations, and security implications
 * @kind problem
 * @problem.severity recommendation
 * @id cpp/function-analysis-sink
 */

import cpp
import semmle.code.cpp.dataflow.DataFlow
import semmle.code.cpp.security.Security

class TargetFunction extends Function {{
  TargetFunction() {{
    // You can modify this to match your specific function name
    this.getName() = "{function_name}"
  }}
}}

string getParameterDescription(Parameter p) {{
  exists(string paramName, string paramType |
    paramType = p.getType().toString() and
    (
      if exists(p.getName())
      then paramName = p.getName()
      else paramName = "arg" + p.getIndex().toString()
    ) |
    result = paramType + " " + paramName
  )
}}

string getArgumentDescription(FunctionCall fc, int i) {{
  exists(Expr arg |
    arg = fc.getArgument(i) |
    result = arg.toString() + " (" + arg.getType().toString() + ")"
  )
}}

string getNamespacePrefix(Function f) {{
  exists(Namespace n | n = f.getNamespace() |
    if n.getQualifiedName() = "::" or n.getQualifiedName() = ""
    then result = ""
    else result = n.getQualifiedName() + "::"
  )
  or
  not exists(f.getNamespace()) and result = ""
}}

string getDeclaringTypePrefix(Function f) {{
  if exists(f.getDeclaringType())
  then result = f.getDeclaringType().getName() + "::"
  else result = ""
}}

string getNamespaceInfo(Function f) {{
  if exists(f.getNamespace())
  then result = f.getNamespace().getQualifiedName()
  else result = "<global>"
}}

string getFunctionCallsInfo(Function f) {{
  exists(FunctionCall fc |
    fc.getEnclosingFunction() = f |
    result = "  Calls: " + fc.getTarget().getName() +
             " at line " + fc.getLocation().getStartLine().toString() + "\\n"
  )
  or
  not exists(FunctionCall fc | fc.getEnclosingFunction() = f) and
  result = "  No function calls found\\n"
}}

string getFunctionCallers(Function f) {{
  exists(FunctionCall fc |
    fc.getTarget() = f |
    result = "  Called from " + fc.getEnclosingFunction().getName() +
             " at " + fc.getLocation().getFile().getBaseName() +
             ":" + fc.getLocation().getStartLine().toString() + "\\n" +
             "    Arguments:\\n" +
             concat(int i |
               exists(fc.getArgument(i)) |
               "      " + i + ": " + fc.getArgument(i).toString() + " (" + fc.getArgument(i).getType().toString() + ")\\n"
               order by i
             )
  )
  or
  not exists(FunctionCall fc | fc.getTarget() = f) and
  result = "  No callers found\\n"
}}

string getDangerousOperationsInfo(Function f) {{
  exists(FunctionCall fc |
    fc.getEnclosingFunction() = f and
    (
      fc.getTarget().getName().matches("%memcpy%") or
      fc.getTarget().getName().matches("%strcpy%") or
      fc.getTarget().getName().matches("%system%") or
      fc.getTarget().getName().matches("%exec%") or
      fc.getTarget().getName().matches("%popen%") or
      fc.getTarget().getName().matches("%fork%") or
      fc.getTarget().getName().matches("%sprintf%") or
      fc.getTarget().getName().matches("%scanf%")
    ) |
    result = "  Dangerous call: " + fc.getTarget().getName() +
             " at line " + fc.getLocation().getStartLine().toString() + "\\n"
  )
  or
  not exists(FunctionCall fc |
    fc.getEnclosingFunction() = f and
    (
      fc.getTarget().getName().matches("%memcpy%") or
      fc.getTarget().getName().matches("%strcpy%") or
      fc.getTarget().getName().matches("%system%") or
      fc.getTarget().getName().matches("%exec%") or
      fc.getTarget().getName().matches("%popen%") or
      fc.getTarget().getName().matches("%fork%") or
      fc.getTarget().getName().matches("%sprintf%") or
      fc.getTarget().getName().matches("%scanf%")
    )
  ) and
  result = "  None detected\\n"
}}

string getPointerOperationsInfo(Function f) {{
  exists(ArrayExpr ae |
    ae.getEnclosingFunction() = f |
    result = "  Array access at line " + ae.getLocation().getStartLine().toString() + "\\n"
  )
  or
  exists(PointerDereferenceExpr pde |
    pde.getEnclosingFunction() = f |
    result = "  Pointer dereference at line " + pde.getLocation().getStartLine().toString() + "\\n"
  )
  or
  not exists(ArrayExpr ae | ae.getEnclosingFunction() = f) and
  not exists(PointerDereferenceExpr pde | pde.getEnclosingFunction() = f) and
  result = "  None detected\\n"
}}

string getParametersInfo(Function f) {{
  exists(Parameter p |
    p = f.getAParameter() |
    result = "  " + p.getIndex() + ": " + getParameterDescription(p) + "\\n"
  )
  or
  not exists(Parameter p | p = f.getAParameter()) and
  result = "  No parameters\\n"
}}

from TargetFunction f
select f,
  // Basic function information
  "Function Analysis for: " + f.getName() + "\\n" +
  "File: " + f.getFile().getBaseName() + "\\n" +
  "Line: " + f.getLocation().getStartLine().toString() + "\\n" +
  "Return Type: " + f.getType().toString() + "\\n\\n" +

  // Namespace information
  "Namespace: " + getNamespaceInfo(f) + "\\n\\n" +

  // Parameters
  "Parameters:\\n" + getParametersInfo(f) + "\\n" +

  // Function calls
  "Function Calls:\\n" + getFunctionCallsInfo(f) + "\\n" +

  // Callers
  "Callers:\\n" + getFunctionCallers(f) + "\\n" +

  // Dangerous operations
  "Dangerous Operations:\\n" + getDangerousOperationsInfo(f) + "\\n" +

  // Pointer operations
  "Pointer Operations:\\n" + getPointerOperationsInfo(f)
'''

# Inter-procedural分析模板
Inter_procedural_TEMPLATE = '''/**
 * @name {function_name} Analysis for Inter-procedural
 * @description A specialized query to extract information about a function that is marked as inter-procedural,
 *              focusing on data flow between functions and cross-function interactions
 * @kind problem
 * @problem.severity recommendation
 * @id cpp/function-analysis-interprocedural
 */

import cpp
import semmle.code.cpp.dataflow.DataFlow
import semmle.code.cpp.controlflow.ControlFlowGraph

class TargetFunction extends Function {{
  TargetFunction() {{
    // You can modify this to match your specific function name
    this.getName() = "{function_name}"
  }}
}}

string getParameterDescription(Parameter p) {{
  exists(string paramName, string paramType |
    paramType = p.getType().toString() and
    (
      if exists(p.getName())
      then paramName = p.getName()
      else paramName = "arg" + p.getIndex().toString()
    ) |
    result = paramType + " " + paramName
  )
}}

string getArgumentDescription(FunctionCall fc, int i) {{
  exists(Expr arg |
    arg = fc.getArgument(i) |
    result = arg.toString() + " (" + arg.getType().toString() + ")"
  )
}}

string getNamespacePrefix(Function f) {{
  exists(Namespace n | n = f.getNamespace() |
    if n.getQualifiedName() = "::" or n.getQualifiedName() = ""
    then result = ""
    else result = n.getQualifiedName() + "::"
  )
  or
  not exists(f.getNamespace()) and result = ""
}}

string getDeclaringTypePrefix(Function f) {{
  if exists(f.getDeclaringType())
  then result = f.getDeclaringType().getName() + "::"
  else result = ""
}}

string getNamespaceInfo(Function f) {{
  if exists(f.getNamespace())
  then result = f.getNamespace().getQualifiedName()
  else result = "<global>"
}}

string getFunctionCallsInfo(Function f) {{
  exists(FunctionCall fc |
    fc.getEnclosingFunction() = f |
    result = "  Calls: " + fc.getTarget().getName() +
             " at line " + fc.getLocation().getStartLine().toString() + "\\n"
  )
  or
  not exists(FunctionCall fc | fc.getEnclosingFunction() = f) and
  result = "  No function calls found\\n"
}}

string getFunctionCallers(Function f) {{
  exists(FunctionCall fc |
    fc.getTarget() = f |
    result = "  Called from " + fc.getEnclosingFunction().getName() +
             " at " + fc.getLocation().getFile().getBaseName() +
             ":" + fc.getLocation().getStartLine().toString() + "\\n" +
             "    Arguments:\\n" +
             concat(int i |
               exists(fc.getArgument(i)) |
               "      " + i + ": " + fc.getArgument(i).toString() + " (" + fc.getArgument(i).getType().toString() + ")\\n"
               order by i
             )
  )
  or
  not exists(FunctionCall fc | fc.getTarget() = f) and
  result = "  No callers found\\n"
}}

string getControlFlowInfo(Function f) {{
  exists(ControlFlowNode cfn |
    cfn.getControlFlowScope() = f |
    result = "  Control flow node at line " + cfn.getLocation().getStartLine().toString() + "\\n"
  )
  or
  not exists(ControlFlowNode cfn | cfn.getControlFlowScope() = f) and
  result = "  No control flow information found\\n"
}}

string getDataFlowInfo(Function f) {{
  exists(DataFlow::Node dfn |
    dfn.getFunction() = f |
    result = "  Data flow node at line " + dfn.getLocation().getStartLine().toString() + "\\n"
  )
  or
  not exists(DataFlow::Node dfn | dfn.getFunction() = f) and
  result = "  No data flow information found\\n"
}}

from TargetFunction f
select f,
  // Basic function information
  "Function Analysis for: " + f.getName() + "\\n" +
  "File: " + f.getFile().getBaseName() + "\\n" +
  "Line: " + f.getLocation().getStartLine().toString() + "\\n" +
  "Return Type: " + f.getType().toString() + "\\n\\n" +

  // Namespace information
  "Namespace: " + getNamespaceInfo(f) + "\\n\\n" +

  // Parameters
  "Parameters:\\n" +
  strictconcat(Parameter p | p = f.getAParameter() |
    "  " + p.getIndex() + ": " + getParameterDescription(p) + "\\n"
    order by p.getIndex()
  ) + "\\n" +

  // Function calls
  "Function Calls:\\n" + getFunctionCallsInfo(f) + "\\n" +

  // Callers
  "Callers:\\n" + getFunctionCallers(f) + "\\n" +

  // Control flow
  "Control Flow Information:\\n" + getControlFlowInfo(f) + "\\n" +

  // Data flow
  "Data Flow Information:\\n" + getDataFlowInfo(f)
'''
