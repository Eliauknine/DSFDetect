/**
 * @name Function Analysis for Sink
 * @description A specialized query to extract information about a function that is marked as a sink,
 *              focusing on data flow, dangerous operations, and security implications
 * @kind problem
 * @problem.severity recommendation
 * @id cpp/function-analysis-sink
 */

import cpp
import semmle.code.cpp.dataflow.DataFlow
import semmle.code.cpp.security.Security

class TargetFunction extends Function {
  TargetFunction() {
    // You can modify this to match your specific function name
    this.getName() = "DestroyMagickWand"
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

string getFunctionCallsInfo(Function f) {
  exists(FunctionCall fc |
    fc.getEnclosingFunction() = f |
    result = "  Calls: " + fc.getTarget().getName() +
             " at line " + fc.getLocation().getStartLine().toString() + "\n"
  )
  or
  not exists(FunctionCall fc | fc.getEnclosingFunction() = f) and
  result = "  No function calls found\n"
}

string getFunctionCallers(Function f) {
  exists(FunctionCall fc |
    fc.getTarget() = f |
    result = "  Called from " + fc.getEnclosingFunction().getName() +
             " at " + fc.getLocation().getFile().getBaseName() +
             ":" + fc.getLocation().getStartLine().toString() + "\n" +
             "    Arguments:\n" +
             concat(int i |
               exists(fc.getArgument(i)) |
               "      " + i + ": " + fc.getArgument(i).toString() + " (" + fc.getArgument(i).getType().toString() + ")\n"
               order by i
             )
  )
  or
  not exists(FunctionCall fc | fc.getTarget() = f) and
  result = "  No callers found\n"
}

string getDangerousOperationsInfo(Function f) {
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
             " at line " + fc.getLocation().getStartLine().toString() + "\n"
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
  result = "  None detected\n"
}

string getPointerOperationsInfo(Function f) {
  exists(ArrayExpr ae |
    ae.getEnclosingFunction() = f |
    result = "  Array access at line " + ae.getLocation().getStartLine().toString() + "\n"
  )
  or
  exists(PointerDereferenceExpr pde |
    pde.getEnclosingFunction() = f |
    result = "  Pointer dereference at line " + pde.getLocation().getStartLine().toString() + "\n"
  )
  or
  not exists(ArrayExpr ae | ae.getEnclosingFunction() = f) and
  not exists(PointerDereferenceExpr pde | pde.getEnclosingFunction() = f) and
  result = "  None detected\n"
}

string getParametersInfo(Function f) {
  exists(Parameter p |
    p = f.getAParameter() |
    result = strictconcat(Parameter param |
      param = f.getAParameter() |
      "  " + param.getIndex() + ": " + getParameterDescription(param) + "\n"
      order by param.getIndex()
    )
  )
  or
  not exists(f.getAParameter()) and
  result = "  No parameters\n"
}

from TargetFunction f
select f,
  // Basic function information
  "Function Analysis (Sink) for: " + f.getName() + "\n" +
  "File: " + f.getFile().getBaseName() + "\n" +
  "Line: " + f.getLocation().getStartLine().toString() + "\n" +
  "Return Type: " + f.getType().toString() + "\n\n" +

  // Namespace information
  "Namespace: " + getNamespaceInfo(f) + "\n\n" +

  // Parameters with improved description
  "Parameters:\n" + getParametersInfo(f) + "\n" +

  // Calls to this function (where this function is used as sink)
  "Called From (Sink Usage):\n" + getFunctionCallers(f) + "\n" +

  // Functions called by this function
  "Functions Called By This Sink:\n" + getFunctionCallsInfo(f) + "\n" +

  // Dangerous operations
  "Potentially Dangerous Operations:\n" + getDangerousOperationsInfo(f) + "\n" +

  // Pointer/Array operations
  "Pointer/Array Operations:\n" + getPointerOperationsInfo(f) + "\n" +

  // Declaration information with full namespace
  "Full Declaration:\n" +
  "  " + getNamespacePrefix(f) + getDeclaringTypePrefix(f) + f.getName() +
  "(" + concat(Parameter p | p = f.getAParameter() | getParameterDescription(p) order by p.getIndex()) + ")" 
