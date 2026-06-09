/**
 * @name Custom source to sink path search for wolfSSL_Malloc_source_sink
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
            "GetASNHeader",
            "GetASNNull",
            "GetASNObjectId",
            "GetAlgoId",
            "GetBoolean",
            "GetCertHeader",
            "GetInputData",
            "GetKey",
            "GetName",
            "GetObjectId",
            "GetOctetString",
            "GetRecordHeader",
            "GetSignature",
            "GetValidity",
            "TLSX_PointFormat_GetSize",
            "TLSX_SignatureAlgorithms_GetSize",
            "TLSX_SupportedCurve_GetSize",
            "get_rand_digit",
            "mp_read_unsigned_bin",
            "wc_HashGetDigestSize",
            "wc_Md5GetHash",
            "wc_Sha256GetHash",
            "wc_Sha384GetHash",
            "wc_Sha512GetHash",
            "wc_ShaGetHash",
            "wc_SignatureGetSize",
            "wolfSSL_GetMaxOutputSize",
            "wolfSSL_GetMaxRecordSize",
            "wolfSSL_Malloc",
            "wolfSSL_read",
            "wolfSSL_read_internal"
        ]
    )
}

predicate isSourceFunctionArgument(DataFlow::Node src) {
    exists(FunctionCall fc, int idx |
        src.asExpr() = fc.getArgument(idx) and
        (
            (fc.getTarget().getName() = "wolfSSL_Malloc" and idx = 0)
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
            "ClientBenchmarkThroughput",
            "ClientWrite",
            "GetInputData",
            "GrowInputBuffer",
            "GrowOutputBuffer",
            "HashInput",
            "HashOutput",
            "HashOutputRaw",
            "SendAlert",
            "SendBuffered",
            "SendCertificate",
            "SendCertificateRequest",
            "SendCertificateStatus",
            "SendCertificateVerify",
            "SendChangeCipher",
            "SendClientHello",
            "SendClientKeyExchange",
            "SendData",
            "SendFinished",
            "SendServerHello",
            "SendServerHelloDone",
            "SendServerKeyExchange",
            "ServerWrite",
            "ShrinkInputBuffer",
            "ShrinkOutputBuffer",
            "TLSX_PointFormat_Write",
            "TLSX_SignatureAlgorithms_Write",
            "TLSX_SupportedCurve_Write",
            "TLSX_Write",
            "TLSX_WriteRequest",
            "TLSX_WriteResponse",
            "WriteSEQ",
            "__builtin___memcpy_chk",
            "wolfSSL_CTX_SetIOSend",
            "wolfSSL_GetMaxOutputSize",
            "wolfSSL_Malloc",
            "wolfSSL_SetIOWriteCtx",
            "wolfSSL_set_write_fd",
            "wolfSSL_write"
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
    string sinkInfo
where
    config.hasFlowPath(source, sink) and
    sourceInfo = getFunctionName(source.getNode()) and
    sinkInfo = getFunctionName(sink.getNode())
select
    sink.getNode(),
    source,
    sink,
    "Data flow path from " + sourceInfo + " to " + sinkInfo,
    source.getNode().getLocation().toString(),
    sourceInfo,
    sink.getNode().getLocation().toString(),
    sinkInfo
