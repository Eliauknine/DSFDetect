/**
 * @name Test Custom Models Loading
 * @description Test if custom models are properly loaded by listing all defined models
 * @kind table
 * @id cpp/test-custom-models-loading
 */

import cpp
import semmle.code.cpp.dataflow.TaintTracking
import semmle.code.cpp.security.Security

from string name, string kind
where
  (
    exists(string namespace, string type, boolean subtypes, string signature,
           string ext, string output, string provenance |
      sourceModel(namespace, type, subtypes, name, signature, ext, output, kind, provenance)
    ) and
    kind = "source"
  )
  or
  (
    exists(string namespace, string type, boolean subtypes, string signature,
           string ext, string input, string provenance |
      sinkModel(namespace, type, subtypes, name, signature, ext, input, kind, provenance)
    ) and
    kind = "sink"
  )
  or
  (
    exists(string namespace, string type, boolean subtypes, string signature,
           string ext, string input, string output, string provenance |
      summaryModel(namespace, type, subtypes, name, signature, ext, input, output, kind, provenance)
    ) and
    kind = "summary"
  )
select name, kind 