/**
 * @name Custom source to sink path search for _TIFFmalloc_source_sink
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
            "_TIFFmalloc"
        ]
    )
}

predicate isSourceFunctionArgument(DataFlow::Node src) {
    exists(FunctionCall fc, int idx |
        src.asExpr() = fc.getArgument(idx) and
        (
            (fc.getTarget().getName() = "_TIFFmalloc" and idx = 0)
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
            "TIFFComputeStrip",
            "TIFFComputeTile",
            "TIFFGetWriteProc",
            "TIFFReadDirEntryOutputErr",
            "TIFFRewriteDirectory",
            "TIFFWriteBufferSetup",
            "TIFFWriteCheck",
            "TIFFWriteDirectory",
            "TIFFWriteDirectorySec",
            "TIFFWriteDirectoryTagAscii",
            "TIFFWriteDirectoryTagByteArray",
            "TIFFWriteDirectoryTagBytePerSample",
            "TIFFWriteDirectoryTagCheckedAscii",
            "TIFFWriteDirectoryTagCheckedByteArray",
            "TIFFWriteDirectoryTagCheckedDoubleArray",
            "TIFFWriteDirectoryTagCheckedFloatArray",
            "TIFFWriteDirectoryTagCheckedIfd8Array",
            "TIFFWriteDirectoryTagCheckedIfdArray",
            "TIFFWriteDirectoryTagCheckedLong",
            "TIFFWriteDirectoryTagCheckedLong8Array",
            "TIFFWriteDirectoryTagCheckedLongArray",
            "TIFFWriteDirectoryTagCheckedRational",
            "TIFFWriteDirectoryTagCheckedRationalArray",
            "TIFFWriteDirectoryTagCheckedSbyteArray",
            "TIFFWriteDirectoryTagCheckedShort",
            "TIFFWriteDirectoryTagCheckedShortArray",
            "TIFFWriteDirectoryTagCheckedSlong8Array",
            "TIFFWriteDirectoryTagCheckedSlongArray",
            "TIFFWriteDirectoryTagCheckedSrationalArray",
            "TIFFWriteDirectoryTagCheckedSshortArray",
            "TIFFWriteDirectoryTagCheckedUndefinedArray",
            "TIFFWriteDirectoryTagColormap",
            "TIFFWriteDirectoryTagData",
            "TIFFWriteDirectoryTagDoubleArray",
            "TIFFWriteDirectoryTagDoublePerSample",
            "TIFFWriteDirectoryTagFloatArray",
            "TIFFWriteDirectoryTagFloatPerSample",
            "TIFFWriteDirectoryTagIfd8Array",
            "TIFFWriteDirectoryTagIfdArray",
            "TIFFWriteDirectoryTagLong",
            "TIFFWriteDirectoryTagLong8Array",
            "TIFFWriteDirectoryTagLongArray",
            "TIFFWriteDirectoryTagLongLong8Array",
            "TIFFWriteDirectoryTagLongPerSample",
            "TIFFWriteDirectoryTagRational",
            "TIFFWriteDirectoryTagRationalArray",
            "TIFFWriteDirectoryTagSampleformatPerSample",
            "TIFFWriteDirectoryTagSbyteArray",
            "TIFFWriteDirectoryTagSbytePerSample",
            "TIFFWriteDirectoryTagShort",
            "TIFFWriteDirectoryTagShortArray",
            "TIFFWriteDirectoryTagShortLong",
            "TIFFWriteDirectoryTagShortLongLong8Array",
            "TIFFWriteDirectoryTagShortPerSample",
            "TIFFWriteDirectoryTagSlong8Array",
            "TIFFWriteDirectoryTagSlongArray",
            "TIFFWriteDirectoryTagSlongPerSample",
            "TIFFWriteDirectoryTagSrationalArray",
            "TIFFWriteDirectoryTagSshortArray",
            "TIFFWriteDirectoryTagSshortPerSample",
            "TIFFWriteDirectoryTagSubifd",
            "TIFFWriteDirectoryTagTransferfunction",
            "TIFFWriteDirectoryTagUndefinedArray",
            "TIFFWriteEncodedStrip",
            "TIFFWriteEncodedTile",
            "TIFFWriteOvrRow",
            "TIFFWriteRawStrip",
            "TIFFWriteRawTile",
            "TIFFWriteScanline",
            "TIFFWriteTile",
            "TIFF_WriteOverview",
            "_TIFFmemcpy",
            "__builtin___memcpy_chk",
            "__builtin___strcpy_chk",
            "fputc",
            "fwrite",
            "putc",
            "t2pWriteFile",
            "t2p_readwrite_pdf_image",
            "t2p_readwrite_pdf_image_tile",
            "t2p_write_advance_directory",
            "t2p_write_pdf",
            "t2p_write_pdf_catalog",
            "t2p_write_pdf_header",
            "t2p_write_pdf_info",
            "t2p_write_pdf_obj_end",
            "t2p_write_pdf_obj_start",
            "t2p_write_pdf_page",
            "t2p_write_pdf_page_content_stream",
            "t2p_write_pdf_pages",
            "t2p_write_pdf_stream",
            "t2p_write_pdf_stream_dict",
            "t2p_write_pdf_stream_dict_end",
            "t2p_write_pdf_stream_dict_start",
            "t2p_write_pdf_stream_end",
            "t2p_write_pdf_stream_length",
            "t2p_write_pdf_stream_start",
            "t2p_write_pdf_string",
            "t2p_write_pdf_trailer",
            "t2p_write_pdf_transfer",
            "t2p_write_pdf_transfer_dict",
            "t2p_write_pdf_transfer_stream",
            "t2p_write_pdf_xobject_calcs",
            "t2p_write_pdf_xobject_cs",
            "t2p_write_pdf_xobject_decode",
            "t2p_write_pdf_xobject_icccs",
            "t2p_write_pdf_xobject_icccs_dict",
            "t2p_write_pdf_xobject_icccs_stream",
            "t2p_write_pdf_xobject_palettecs_stream",
            "t2p_write_pdf_xobject_stream_dict",
            "t2p_write_pdf_xobject_stream_filter",
            "t2p_write_pdf_xreftable",
            "writeBufferToContigStrips",
            "writeBufferToContigTiles",
            "writeBufferToSeparateStrips",
            "writeBufferToSeparateTiles",
            "writeCroppedImage",
            "writeImageSections",
            "writeSingleSection"
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
