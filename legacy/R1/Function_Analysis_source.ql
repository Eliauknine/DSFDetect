/**
 * @name Function Analysis Generic
 * @description A generic query to extract detailed information about a function including its definition, parameter sources, and context
 * @kind problem
 * @problem.severity recommendation
 * @id cpp/function-analysis-generic
 */

import cpp

class TargetFunction extends Function {
  TargetFunction() {
    // You can modify this to match your specific function name
    this.getName() = "ConstituteImage"
  }
}

string getParameterDescription(Parameter p) {
  exists(string paramName, string paramType |
    paramType = p.getType().toString() and
    (
      if exists(p.getName())
      then paramName = p.getName()
      else paramName = "arg" + p.getIndex().toString()
    ) |
    result = paramType + " " + paramName
  )
}

string getArgumentDescription(FunctionCall fc, int i) {
  exists(Expr arg |
    arg = fc.getArgument(i) |
    result = arg.toString() + " (" + arg.getType().toString() + ")"
  )
}

string getNamespacePrefix(Function f) {
  exists(Namespace n | n = f.getNamespace() |
    if n.getQualifiedName() = "::" or n.getQualifiedName() = ""
    then result = ""
    else result = n.getQualifiedName() + "::"
  )
  or
  not exists(f.getNamespace()) and result = ""
}

string getDeclaringTypePrefix(Function f) {
  if exists(f.getDeclaringType())
  then result = f.getDeclaringType().getName() + "::"
  else result = ""
}

string getNamespaceInfo(Function f) {
  if exists(f.getNamespace())
  then result = f.getNamespace().getQualifiedName()
  else result = "<global>"
}

from TargetFunction f
select f,
  // Basic function information
  "Function Analysis for: " + f.getName() + "\n" +
  "File: " + f.getFile().getBaseName() + "\n" +
  "Line: " + f.getLocation().getStartLine().toString() + "\n" +
  "Return Type: " + f.getType().toString() + "\n\n" +

  // Namespace information
  "Namespace: " + getNamespaceInfo(f) + "\n\n" +

  // Parameters with improved description
  "Parameters:\n" +
  strictconcat(Parameter p | p = f.getAParameter() |
    "  " + p.getIndex() + ": " + getParameterDescription(p) + "\n"
    order by p.getIndex()
  ) + "\n" +

  // Function calls with argument information
  "Function Calls:\n" +
  strictconcat(FunctionCall fc | fc.getTarget() = f |
    "  Called from " + fc.getEnclosingFunction().getName() +
    " at " + fc.getLocation().getFile().getBaseName() +
    ":" + fc.getLocation().getStartLine().toString() + "\n" +
    strictconcat(int i | i in [0 .. fc.getNumberOfArguments() - 1] |
      "    Arg " + i + ": " + getArgumentDescription(fc, i) + "\n"
      order by i
    )
    order by fc.getLocation().getStartLine()
  ) + "\n" +

  // Location information
  "Location Details:\n" +
  "  Start line: " + f.getLocation().getStartLine().toString() + "\n" +
  "  End line: " + f.getLocation().getEndLine().toString() + "\n" +
  "  Start column: " + f.getLocation().getStartColumn().toString() + "\n" +
  "  End column: " + f.getLocation().getEndColumn().toString() + "\n" +

  // Declaration information with full namespace
  "Declaration:\n" +
  "  " + getNamespacePrefix(f) + getDeclaringTypePrefix(f) + f.getName() +
  "(" + concat(Parameter p | p = f.getAParameter() | getParameterDescription(p) order by p.getIndex()) + ")" 
