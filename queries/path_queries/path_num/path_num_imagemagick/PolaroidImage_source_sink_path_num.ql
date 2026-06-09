/**
 * @name Custom source to sink path search for PolaroidImage_source_sink
 * @description Finds paths from custom defined sources to sinks
 * @kind path-problem
 * @problem.severity warning
 * @precision high
 * @id cpp/custom-source-sink-path
 * @tags security
 */

import cpp
import semmle.code.cpp.dataflow.new.DataFlow
import semmle.code.cpp.dataflow.new.TaintTracking
import DataFlow::PathGraph

// ----------- Source Definitions -----------

predicate isSourceFunctionCall(DataFlow::Node src) {
    exists(FunctionCall fc |
        fc = src.asExpr() and
        fc.getTarget().getName() in [
            "GetFirstImageInList",
            "GetImageProperty",
            "GetNextValueInSplayTree",
            "GetPseudoRandomValue",
            "GetValueFromSplayTree",
            "__get_long_pointer",
            "__get_pointer",
            "__get_short_pointer"
        ]
    )
}

predicate isSourceFunctionArgument(DataFlow::Node src) {
    exists(FunctionCall fc, int idx |
        src.asExpr() = fc.getArgument(idx) and
        (
            (fc.getTarget().getName() = "PolaroidImage" and idx = 0)
        )
    )
}

predicate isSourceGlobal(DataFlow::Node src) {
    isSourceFunctionCall(src) or
    isSourceFunctionArgument(src)
}

// ----------- Sink Definitions -----------
predicate isSinkGlobal(DataFlow::Node sink) {
    exists(FunctionCall fc |
        sink.asExpr() = fc.getAnArgument() and
        fc.getTarget().getName() in [
            "PolaroidImage",
            "SetPixelWriteMask",
            "WriteImages"
        ]
    )
}

// ----------- Path Query Configuration -----------
class CustomSourceSinkConfiguration extends TaintTracking::Configuration {
    CustomSourceSinkConfiguration() { this = "CustomSourceSinkConfiguration" }

    override predicate isSource(DataFlow::Node source) {
        isSourceGlobal(source)
    }

    override predicate isSink(DataFlow::Node sink) {
        isSinkGlobal(sink)
    }

    override predicate isAdditionalTaintStep(DataFlow::Node node1, DataFlow::Node node2) {
        // Assignment
        exists(AssignExpr assign |
            node1.asExpr() = assign.getRValue() and
            node2.asExpr() = assign.getLValue()
        )
        or
        // Parameter passing
        exists(FunctionCall call, int i |
            node1.asExpr() = call.getArgument(i) and
            exists(Parameter p |
                p = call.getTarget().getParameter(i) and
                node2.asParameter() = p
            )
        )
        or
        // Return value
        exists(FunctionCall call, ReturnStmt ret |
            ret.getEnclosingFunction() = call.getTarget() and
            node1.asExpr() = ret.getExpr() and
            node2.asExpr() = call
        )
    }
}

// Get function name
string getFunctionName(DataFlow::Node node) {
    exists(FunctionCall fc |
        (node.asExpr() = fc or node.asExpr() = fc.getAnArgument()) and
        result = fc.getTarget().getName()
    )
    or
    exists(Parameter p |
        node.asParameter() = p and
        result = p.getFunction().getName()
    )
}


// ----------- Main Query -----------
from
    DataFlow::PathNode source,
    DataFlow::PathNode sink,
    CustomSourceSinkConfiguration config,
    string sourceInfo,
    string sinkInfo,
    // 添加新的变量用于统计
    int totalPaths,
    int functionPaths
where
    config.hasFlowPath(source, sink) and
    sourceInfo = getFunctionName(source.getNode()) and
    sinkInfo = getFunctionName(sink.getNode()) and
    // 计算总路径数
    totalPaths = count(DataFlow::PathNode src, DataFlow::PathNode snk |
        config.hasFlowPath(src, snk)
    ) and
    // 计算包含 AcquireImage 的路径数
    functionPaths = count(DataFlow::PathNode src, DataFlow::PathNode snk |
        config.hasFlowPath(src, snk) and
        getFunctionName(src.getNode()) = "PolaroidImage"
    )
select
    sink.getNode(),
    source,
    sink,
    "Data flow path from " + sourceInfo + " to " + sinkInfo + "\n" +
    "Total paths: " + totalPaths.toString() + "\n" +
    "Paths with AcquireImage: " + functionPaths.toString() + "\n" +
    "Percentage: " + ((100.0 * functionPaths) / totalPaths).toString() + "%",
    source.getNode().getLocation().toString(),
    sourceInfo,
    sink.getNode().getLocation().toString(),
    sinkInfo

