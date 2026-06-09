/**
 * @name Test Custom Models
 * @description Test if custom models are properly loaded
 * @kind problem
 * @problem.severity warning
 * @id cpp/test-custom-models
 */

import cpp
import semmle.code.cpp.dataflow.TaintTracking
import semmle.code.cpp.security.Security

from FunctionCall call, Function f
where
  f = call.getTarget() and
  (
    // 测试source model
    exists(string namespace, string type, boolean subtypes, string name, string signature,
           string ext, string output, string kind, string provenance |
      sourceModel(namespace, type, subtypes, name, signature, ext, output, kind, provenance) and
      f.hasName(name)
    )
    or
    // 测试sink model
    exists(string namespace, string type, boolean subtypes, string name, string signature,
           string ext, string input, string kind, string provenance |
      sinkModel(namespace, type, subtypes, name, signature, ext, input, kind, provenance) and
      f.hasName(name)
    )
    or
    // 测试summary model
    exists(string namespace, string type, boolean subtypes, string name, string signature,
           string ext, string input, string output, string kind, string provenance |
      summaryModel(namespace, type, subtypes, name, signature, ext, input, output, kind, provenance) and
      f.hasName(name)
    )
  )
select call,
  "Found a call to function that matches our custom models: " + f.getName() 