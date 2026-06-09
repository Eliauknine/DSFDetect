'''test2.ql存放最新更新的ql，有空可以跑一遍'''
SourceModel = """
  - addsTo:
      pack: codeql/cpp-all
      extensible: sourceModel
    data:
      - ["", "", false, "{function_name}", "", "", "ReturnValue", "remote", "manual"]
"""

SinkModel = """
  - addsTo:
      pack: codeql/cpp-all
      extensible: sinkModel
    data:
      - ["", "", false, "{function_name}", "", "", "ReturnValue", "remote-sink", "manual"]"""

SummaryModel = """
  - addsTo:
      pack: codeql/cpp-all
      extensible: summaryModel
    data:
      - ["", "", false, "{function_name}", "", "", "Argument[*0]", "ReturnValue", "taint", "manual"]
"""


SOURCE_SINK_SEARCH = """/**
 * @name Find taint analysis candidates related to {function_name}
 * @description Identifies potential sources and sinks related to {function_name} function
 * @kind problem
 * @problem.severity warning
 * @id cpp/queue-authentic-pixels-taint-analysis
 */

import cpp
import semmle.code.cpp.dataflow.new.DataFlow
import semmle.code.cpp.dataflow.new.TaintTracking

// 定义外部调用筛选
predicate isExternalCall(FunctionCall fc) {
    // 排除标准库中的一些常见函数
    not fc.getTarget().getName().matches("std::%") and
    not fc.getTarget().getName().matches("__builtin_%") and
    not fc.getTarget().getName().matches("__cxa_%") and
    // 排除测试相关函数
    not fc.getTarget().getName().matches("TEST%") and
    not fc.getTarget().getName().matches("test%") and
    not fc.getTarget().getName().matches("mock%")
}

// 获取函数完整签名
string getFullSignature(Function f) {
    result = f.getName() + "(" +
        concat(int i | i = [0 .. f.getNumberOfParameters()] |
            f.getParameter(i).getType().getName() + " " + f.getParameter(i).getName(),
            ", " order by i asc
        ) + ")"
}

// 获取函数注释
string getFunctionComment(Function f) {
    exists(FunctionDeclarationEntry entry, Comment c |
        entry = f.getADeclarationEntry() and
        c.getCommentedElement() = entry and
        result = c.getContents()
    )
    or
    result = ""
}

// 定义向上游追踪的配置
class UpstreamFlow extends TaintTracking::Configuration {
    UpstreamFlow() { this = "UpstreamFlow" }

    // 定义最初的source点
    override predicate isSource(DataFlow::Node source) {
        exists(Expr e | e = source.asExpr() |
            // 文件读取
            exists(FunctionCall fc | fc = e |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%read%") or
                    fc.getTarget().getName().matches("%Read%") or
                    fc.getTarget().getName().matches("%get%") or
                    fc.getTarget().getName().matches("%Get%") or
                    fc.getTarget().getName().matches("%fread%") or
                    fc.getTarget().getName().matches("%fscanf%")
                )
            )
            or
            // 网络接收
            exists(FunctionCall fc | fc = e |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%recv%") or
                    fc.getTarget().getName().matches("%Recv%") or
                    fc.getTarget().getName().matches("%recvfrom%") or
                    fc.getTarget().getName().matches("%receive%")
                )
            )
            or
            // 用户输入
            exists(FunctionCall fc | fc = e |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%scanf%") or
                    fc.getTarget().getName().matches("%input%") or
                    fc.getTarget().getName().matches("%gets%") or
                    fc.getTarget().getName().matches("%fgets%")
                )
            )
            or
            // 内存分配
            exists(FunctionCall fc | fc = e |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%malloc%") or
                    fc.getTarget().getName().matches("%new%") or
                    fc.getTarget().getName().matches("%calloc%")
                )
            )
            or
            // 图像处理相关
            exists(FunctionCall fc | fc = e |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%image%") or
                    fc.getTarget().getName().matches("%pixel%") or
                    fc.getTarget().getName().matches("%bitmap%") or
                    fc.getTarget().getName().matches("%decode%") or
                    fc.getTarget().getName().matches("%load%")
                )
            )
        )
    }

    // {function_name}作为sink
    override predicate isSink(DataFlow::Node sink) {
        exists(FunctionCall fc |
            fc.getTarget().getName() = "{function_name}" and
            isExternalCall(fc) and
            sink.asExpr() = fc.getAnArgument()
        )
    }
}

// 定义向下游追踪的配置
class DownstreamFlow extends TaintTracking::Configuration {
    DownstreamFlow() { this = "DownstreamFlow" }

    // {function_name}作为source
    override predicate isSource(DataFlow::Node source) {
        exists(FunctionCall fc |
            fc.getTarget().getName() = "{function_name}" and
            isExternalCall(fc) and
            (
                source.asExpr() = fc
                or
                exists(int i |
                    source.asExpr() = fc.getArgument(i)
                )
            )
        )
    }

    // 定义最终的sink点
    override predicate isSink(DataFlow::Node sink) {
        exists(Expr e | e = sink.asExpr() |
            // 文件写入
            exists(FunctionCall fc | e = fc.getAnArgument() |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%write%") or
                    fc.getTarget().getName().matches("%Write%") or
                    fc.getTarget().getName().matches("%put%") or
                    fc.getTarget().getName().matches("%Put%") or
                    fc.getTarget().getName().matches("%fwrite%") or
                    fc.getTarget().getName().matches("%fprintf%")
                )
            )
            or
            // 网络发送
            exists(FunctionCall fc | e = fc.getAnArgument() |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%send%") or
                    fc.getTarget().getName().matches("%Send%") or
                    fc.getTarget().getName().matches("%sendto%")
                )
            )
            or
            // 内存写入
            exists(FunctionCall fc | e = fc.getAnArgument() |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%memcpy%") or
                    fc.getTarget().getName().matches("%strcpy%") or
                    fc.getTarget().getName().matches("%strncpy%") or
                    fc.getTarget().getName().matches("%memmove%")
                )
            )
            or
            // 图像处理相关
            exists(FunctionCall fc | e = fc.getAnArgument() |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%image%") or
                    fc.getTarget().getName().matches("%pixel%") or
                    fc.getTarget().getName().matches("%bitmap%") or
                    fc.getTarget().getName().matches("%encode%") or
                    fc.getTarget().getName().matches("%save%")
                )
            )
        )
    }
}

// 主查询
from
    DataFlow::Node source,
    DataFlow::Node sink,
    string flowDescription,
    string sourceInfo,
    string sinkInfo,
    string sourceComment,
    string sinkComment,
    string sourceSignature,
    string sinkSignature
where
    (
        // 向上游的数据流
        exists(UpstreamFlow upConfig |
            upConfig.hasFlow(source, sink) and
            flowDescription = "Upstream flow from source to {function_name}" and
            (
                exists(FunctionCall fc | source.asExpr() = fc |
                    sourceInfo = "Function call: " + fc.getTarget().getName() and
                    sourceComment = getFunctionComment(fc.getTarget()) and
                    sourceSignature = getFullSignature(fc.getTarget())
                )
                or
                exists(Parameter p | source.asParameter() = p |
                    sourceInfo = "Parameter of " + p.getFunction().getName() and
                    sourceComment = getFunctionComment(p.getFunction()) and
                    sourceSignature = getFullSignature(p.getFunction())
                )
            ) and
            (
                exists(FunctionCall fc | sink.asExpr() = fc.getAnArgument() |
                    sinkInfo = "Argument of " + fc.getTarget().getName() and
                    sinkComment = getFunctionComment(fc.getTarget()) and
                    sinkSignature = getFullSignature(fc.getTarget())
                )
            )
        )
        or
        // 向下游的数据流
        exists(DownstreamFlow downConfig |
            downConfig.hasFlow(source, sink) and
            flowDescription = "Downstream flow from {function_name} to sink" and
            (
                exists(FunctionCall fc | source.asExpr() = fc |
                    sourceInfo = "Function call: " + fc.getTarget().getName() and
                    sourceComment = getFunctionComment(fc.getTarget()) and
                    sourceSignature = getFullSignature(fc.getTarget())
                )
                or
                exists(FunctionCall fc, int i | source.asExpr() = fc.getArgument(i) |
                    sourceInfo = "Argument " + i + " of " + fc.getTarget().getName() and
                    sourceComment = getFunctionComment(fc.getTarget()) and
                    sourceSignature = getFullSignature(fc.getTarget())
                )
            ) and
            (
                exists(FunctionCall fc | sink.asExpr() = fc.getAnArgument() |
                    sinkInfo = "Argument of " + fc.getTarget().getName() and
                    sinkComment = getFunctionComment(fc.getTarget()) and
                    sinkSignature = getFullSignature(fc.getTarget())
                )
                or
                exists(FunctionCall fc | sink.asExpr() = fc |
                    sinkInfo = "Call to " + fc.getTarget().getName() and
                    sinkComment = getFunctionComment(fc.getTarget()) and
                    sinkSignature = getFullSignature(fc.getTarget())
                )
            )
        )
    )
select
    source,
    sink,
    flowDescription + "\\n" +
    "Source: " + sourceInfo + "\\n" +
    "Source Signature: " + sourceSignature + "\\n" +
    "Source Comment: " + sourceComment + "\\n" +
    "Source Location: " + source.getLocation().toString() + "\\n" +
    "Sink: " + sinkInfo + "\\n" +
    "Sink Signature: " + sinkSignature + "\\n" +
    "Sink Comment: " + sinkComment + "\\n" +
    "Sink Location: " + sink.getLocation().toString()


"""


SOURCE_ONLY = """/**
 * @name Find downstream sinks for {function_name}
 * @description Finds ultimate sinks receiving data from {function_name} function
 * @kind problem
 * @problem.severity warning
 * @id cpp/bad-pixels-flow-sinks
 */

import cpp
import semmle.code.cpp.dataflow.new.DataFlow
import semmle.code.cpp.dataflow.new.TaintTracking

// 定义外部调用筛选
predicate isExternalCall(FunctionCall fc) {
    // 排除标准库中的一些常见函数
    not fc.getTarget().getName().matches("std::%") and
    not fc.getTarget().getName().matches("__builtin_%") and
    not fc.getTarget().getName().matches("__cxa_%") and
    // 排除测试相关函数
    not fc.getTarget().getName().matches("TEST%") and
    not fc.getTarget().getName().matches("test%") and
    not fc.getTarget().getName().matches("mock%")
}

// 获取函数完整签名
string getFullSignature(Function f) {
    result = f.getName() + "(" +
        concat(int i | i = [0 .. f.getNumberOfParameters()] |
            f.getParameter(i).getType().getName() + " " + f.getParameter(i).getName(),
            ", " order by i asc
        ) + ")"
}

// 获取函数注释
string getFunctionComment(Function f) {
    exists(FunctionDeclarationEntry entry, Comment c |
        entry = f.getADeclarationEntry() and
        c.getCommentedElement() = entry and
        result = c.getContents()
    )
    or
    result = ""
}

// 定义向下游追踪的配置
class DownstreamFlow extends TaintTracking::Configuration {
    DownstreamFlow() { this = "DownstreamFlow" }

    // {function_name}作为source
    override predicate isSource(DataFlow::Node source) {
        exists(FunctionCall fc |
            fc.getTarget().getName() = "{function_name}" and
            isExternalCall(fc) and
            (
                source.asExpr() = fc
                or
                exists(int i |
                    source.asExpr() = fc.getArgument(i)
                )
            )
        )
    }

    // 定义最终的sink点
    override predicate isSink(DataFlow::Node sink) {
        exists(Expr e | e = sink.asExpr() |
            // 文件写入
            exists(FunctionCall fc | e = fc.getAnArgument() |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%write%") or
                    fc.getTarget().getName().matches("%Write%") or
                    fc.getTarget().getName().matches("%put%") or
                    fc.getTarget().getName().matches("%Put%") or
                    fc.getTarget().getName().matches("%fwrite%") or
                    fc.getTarget().getName().matches("%fprintf%")
                )
            )
            or
            // 网络发送
            exists(FunctionCall fc | e = fc.getAnArgument() |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%send%") or
                    fc.getTarget().getName().matches("%Send%") or
                    fc.getTarget().getName().matches("%sendto%")
                )
            )
            or
            // 内存写入
            exists(FunctionCall fc | e = fc.getAnArgument() |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%memcpy%") or
                    fc.getTarget().getName().matches("%strcpy%") or
                    fc.getTarget().getName().matches("%strncpy%") or
                    fc.getTarget().getName().matches("%memmove%")
                )
            )
            or
            // 图像处理相关
            exists(FunctionCall fc | e = fc.getAnArgument() |
                isExternalCall(fc) and
                (
                    fc.getTarget().getName().matches("%image%") or
                    fc.getTarget().getName().matches("%pixel%") or
                    fc.getTarget().getName().matches("%bitmap%") or
                    fc.getTarget().getName().matches("%encode%") or
                    fc.getTarget().getName().matches("%save%")
                )
            )
        )
    }
}

// 主查询
from
    DataFlow::Node source,
    DataFlow::Node sink,
    string flowDescription,
    string sourceInfo,
    string sinkInfo,
    string sourceComment,
    string sinkComment,
    string sourceSignature,
    string sinkSignature
where
    exists(DownstreamFlow downConfig |
        downConfig.hasFlow(source, sink) and
        flowDescription = "Downstream flow from {function_name} to sink" and
        (
            exists(FunctionCall fc | source.asExpr() = fc |
                sourceInfo = "Function call: " + fc.getTarget().getName() and
                sourceComment = getFunctionComment(fc.getTarget()) and
                sourceSignature = getFullSignature(fc.getTarget())
            )
            or
            exists(FunctionCall fc, int i | source.asExpr() = fc.getArgument(i) |
                sourceInfo = "Argument " + i + " of " + fc.getTarget().getName() and
                sourceComment = getFunctionComment(fc.getTarget()) and
                sourceSignature = getFullSignature(fc.getTarget())
            )
        ) and
        (
            exists(FunctionCall fc | sink.asExpr() = fc.getAnArgument() |
                sinkInfo = "Argument of " + fc.getTarget().getName() and
                sinkComment = getFunctionComment(fc.getTarget()) and
                sinkSignature = getFullSignature(fc.getTarget())
            )
            or
            exists(FunctionCall fc | sink.asExpr() = fc |
                sinkInfo = "Call to " + fc.getTarget().getName() and
                sinkComment = getFunctionComment(fc.getTarget()) and
                sinkSignature = getFullSignature(fc.getTarget())
            )
        )
    )
select
    source,
    sink,
    flowDescription + "\\n" +
    "Source: " + sourceInfo + "\\n" +
    "Source Signature: " + sourceSignature + "\\n" +
    "Source Comment: " + sourceComment + "\\n" +
    "Source Location: " + source.getLocation().toString() + "\\n" +
    "Sink: " + sinkInfo + "\\n" +
    "Sink Signature: " + sinkSignature + "\\n" +
    "Sink Comment: " + sinkComment + "\\n" +
    "Sink Location: " + sink.getLocation().toString()
"""

SINK_ONLY = """/**
 * @name Find upstream sources for {function_name}
 * @description Finds ultimate sources flowing into {function_name}
 * @kind problem
 * @problem.severity warning
 * @id cpp/function-flow-sources
 */

import cpp
import semmle.code.cpp.dataflow.new.DataFlow
import semmle.code.cpp.dataflow.new.TaintTracking

// 定义向上游追踪的配置
class UpstreamFlow extends TaintTracking::Configuration {
    UpstreamFlow() { this = "UpstreamFlow" }

    // 定义最初的source点
    override predicate isSource(DataFlow::Node source) {
        exists(Expr e | e = source.asExpr() |
            // 文件读取
            exists(FunctionCall fc | fc = e |
                fc.getTarget().getName().matches("%read%") or
                fc.getTarget().getName().matches("%Read%") or
                fc.getTarget().getName().matches("%get%") or
                fc.getTarget().getName().matches("%Get%")
            )
            or
            // 网络接收
            exists(FunctionCall fc | fc = e |
                fc.getTarget().getName().matches("%recv%") or
                fc.getTarget().getName().matches("%Recv%") or
                fc.getTarget().getName().matches("%receive%")
            )
            or
            // 用户输入
            exists(FunctionCall fc | fc = e |
                fc.getTarget().getName().matches("%scanf%") or
                fc.getTarget().getName().matches("%input%")
            )
            or
            // 命令行参数
            exists(Function f | f.getName() = "main" |
                source.asParameter() = f.getAParameter()
            )
        )
    }

    // {function_name}作为sink
    override predicate isSink(DataFlow::Node sink) {
        exists(FunctionCall fc |
            fc.getTarget().getName() = "{function_name}" and
            sink.asExpr() = fc.getAnArgument()
        )
    }
}

from
    DataFlow::Node source,
    DataFlow::Node sink,
    string flowDescription,
    string sourceInfo,
    string sinkInfo
where
    exists(UpstreamFlow upConfig |
        upConfig.hasFlow(source, sink) and
        flowDescription = "Upstream flow from source to {function_name}" and
        (
            exists(FunctionCall fc | source.asExpr() = fc |
                sourceInfo = "Function call: " + fc.getTarget().getName()
            )
            or
            exists(Parameter p | source.asParameter() = p |
                sourceInfo = "Parameter of " + p.getFunction().getName()
            )
        ) and
        (
            exists(FunctionCall fc | sink.asExpr() = fc.getAnArgument() |
                sinkInfo = "Argument of " + fc.getTarget().getName()
            )
        )
    )
select
    source,
    sink,
    flowDescription + "\\n" +
    "Source: " + sourceInfo + " at " + source.getLocation().toString() + "\\n" +
    "Sink: " + sinkInfo + " at " + sink.getLocation().toString()
"""



libraw_targetFunctions = """predicate targetFunctions(string funcName) {
    funcName = "minolta_z2" or
    funcName = "crop_masked_pixels" or
    funcName = "_CanonConvertAperture" or
    funcName = "parseFujiMakernotes" or
    funcName = "phase_one_flat_field" or
    funcName = "vng_interpolate" or
    funcName = "ahd_interpolate_r_and_b_and_convert_to_cielab" or
    funcName = "Canon_WBpresets" or
    funcName = "flip_index" or
    funcName = "foveon_huff" or
    funcName = "bad_pixels" or
    funcName = "kodak_65000_decode" or
    funcName = "process_Sony_0x9050" or
    funcName = "nikon_coolscan_load_raw" or
    funcName = "cielab" or
    funcName = "parse_makernote" or
    funcName = "get_timestamp" or
    funcName = "parse_jpeg" or
    funcName = "fill_holes" or
    funcName = "canon_rmf_load_raw" or
    funcName = "ljpeg_idct" or
    funcName = "linear_table" or
    funcName = "tiff_get" or
    funcName = "ljpeg_end" or
    funcName = "merror" or
    funcName = "samsung2_load_raw" or
    funcName = "unpacked_load_raw" or
    funcName = "rollei_thumb" or
    funcName = "panasonic_load_raw" or
    funcName = "foveon_interpolate" or
    funcName = "phase_one_load_raw" or
    funcName = "strncasecmp" or
    funcName = "parse_smal" or
    funcName = "fcol" or
    funcName = "parse_rollei" or
    funcName = "ljpeg_start" or
    funcName = "get2" or
    funcName = "canon_600_coeff" or
    funcName = "ahd_interpolate_green_h_and_v" or
    funcName = "parse_minolta" or
    funcName = "adobe_copy_pixel" or
    funcName = "ljpeg_row" or
    funcName = "int_to_float" or
    funcName = "raw" or
    funcName = "minolta_rd175_load_raw" or
    funcName = "parse_riff" or
    funcName = "foveon_camf_param" or
    funcName = "nikon_3700" or
    funcName = "foveon_sd_load_raw" or
    funcName = "short" or
    funcName = "convert_to_rgb" or
    funcName = "bcd2dec" or
    funcName = "parse_tiff_ifd" or
    funcName = "olympus_load_raw" or
    funcName = "foveon_avg" or
    funcName = "remove_zeroes" or
    funcName = "processCanonCameraInfo" or
    funcName = "samsung_load_raw" or
    funcName = "kodak_ycbcr_load_raw" or
    funcName = "canon_sraw_load_raw" or
    funcName = "read_shorts" or
    funcName = "wavelet_denoise" or
    funcName = "setCanonBodyFeatures" or
    funcName = "ciff_block_1030" or
    funcName = "border_interpolate" or
    funcName = "pre_interpolate" or
    funcName = "process_Sony_0x940c" or
    funcName = "sony_arw2_load_raw" or
    funcName = "ahd_interpolate_build_homogeneity_map" or
    funcName = "foveon_gets" or
    funcName = "fc" or
    funcName = "unpacked_load_raw_reversed" or
    funcName = "getint" or
    funcName = "subtract" or
    funcName = "parse_sinar_ia" or
    funcName = "foveon_make_curves" or
    funcName = "sget2" or
    funcName = "lin_interpolate" or
    funcName = "foveon_make_curve" or
    funcName = "parse_gps_libraw" or
    funcName = "ppg_interpolate" or
    funcName = "float" or
    funcName = "sony_decrypt" or
    funcName = "ppm16_thumb" or
    funcName = "adobe_dng_load_raw_lj" or
    funcName = "canon_compressed_load_raw" or
    funcName = "android_loose_load_raw" or
    funcName = "fuji_load_raw" or
    funcName = "canon_600_color" or
    funcName = "make_decoder" or
    funcName = "parse_ciff" or
    funcName = "crw_init_tables" or
    funcName = "processNikonLensData" or
    funcName = "make_decoder_ref" or
    funcName = "saneSonyCameraInfo" or
    funcName = "parse_mos" or
    funcName = "PentaxISO" or
    funcName = "smal_decode_segment" or
    funcName = "identify" or
    funcName = "crop_pixels" or
    funcName = "xtrans_interpolate" or
    funcName = "Canon_WBCTpresets" or
    funcName = "pana_bits" or
    funcName = "derror" or
    funcName = "if" or
    funcName = "smal_v9_load_raw" or
    funcName = "nikon_compressed_load_raw" or
    funcName = "pseudoinverse" or
    funcName = "smal_v6_load_raw" or
    funcName = "scale_colors" or
    funcName = "fMAX" or
    funcName = "blend_highlights" or
    funcName = "nikon_is_compressed" or
    funcName = "powf_lim" or
    funcName = "Kodak_WB_0x08tags" or
    funcName = "ppm_thumb" or
    funcName = "ushort" or
    funcName = "kodak_radc_load_raw" or
    funcName = "android_tight_load_raw" or
    funcName = "sget2Rev" or
    funcName = "kodak_c603_load_raw" or
    funcName = "my_roundf" or
    funcName = "median4" or
    funcName = "packed_load_raw" or
    funcName = "parse_kodak_ifd" or
    funcName = "rollei_load_raw" or
    funcName = "parseSonyLensFeatures" or
    funcName = "kodak_c330_load_raw" or
    funcName = "remove_trailing_spaces" or
    funcName = "apply_tiff" or
    funcName = "romm_coeff" or
    funcName = "hasselblad_load_raw" or
    funcName = "nikon_load_raw" or
    funcName = "ph1_bithuff" or
    funcName = "parseSonyLensType2" or
    funcName = "broadcom_load_raw" or
    funcName = "quicktake_100_load_raw" or
    funcName = "local_strnlen" or
    funcName = "canon_600_auto_wb" or
    funcName = "ahd_interpolate" or
    funcName = "nikon_yuv_load_raw" or
    funcName = "phase_one_correct" or
    funcName = "kodak_jpeg_load_raw" or
    funcName = "foveon_fixed" or
    funcName = "my_memmem" or
    funcName = "median_filter" or
    funcName = "adobe_coeff" or
    funcName = "nokia_load_raw" or
    funcName = "ahd_interpolate_combine_homogeneous_pixels" or
    funcName = "recover_highlights" or
    funcName = "find_green" or
    funcName = "foveon_camf_matrix" or
    funcName = "Canon_CameraSettings" or
    funcName = "leaf_hdr_load_raw" or
    funcName = "layer_thumb" or
    funcName = "foveon_apply_curve" or
    funcName = "foveon_thumb" or
    funcName = "write_ppm_tiff" or
    funcName = "getreal" or
    funcName = "char" or
    funcName = "sget4" or
    funcName = "strcmp" or
    funcName = "stread" or
    funcName = "foveon_decoder" or
    funcName = "lossless_jpeg_load_raw" or
    funcName = "kodak_rgb_load_raw" or
    funcName = "calc_64cbrt" or
    funcName = "fill_input_buffer" or
    funcName = "parse_redcine" or
    funcName = "eight_bit_load_raw" or
    funcName = "canon_s2is" or
    funcName = "nikon_e2100" or
    funcName = "jpeg_thumb" or
    funcName = "_CanonConvertEV" or
    funcName = "setSonyBodyFeatures" or
    funcName = "pentax_load_raw" or
    funcName = "nikon_e995" or
    funcName = "setPentaxBodyFeatures" or
    funcName = "tiff_set" or
    funcName = "kodak_65000_load_raw" or
    funcName = "kodak_thumb_load_raw" or
    funcName = "guess_byte_order" or
    funcName = "adobe_dng_load_raw_nc" or
    funcName = "parse_phase_one" or
    funcName = "ahd_interpolate_r_and_b_in_rgb_and_convert_to_cielab" or
    funcName = "parse_makernote_0xc634" or
    funcName = "PentaxLensInfo" or
    funcName = "simple_coeff" or
    funcName = "phase_one_load_raw_c" or
    funcName = "tiff_head" or
    funcName = "lossless_dng_load_raw" or
    funcName = "sony_load_raw" or
    funcName = "foveon_dp_load_raw" or
    funcName = "parse_gps" or
    funcName = "canon_600_correct" or
    funcName = "gamma_curve" or
    funcName = "foveon_load_camf" or
    funcName = "samsung3_load_raw" or
    funcName = "sinar_4shot_load_raw" or
    funcName = "jpegErrorExit" or
    funcName = "my_strcasestr" or
    funcName = "parseCanonMakernotes" or
    funcName = "parse_broadcom" or
    funcName = "imacon_full_load_raw" or
    funcName = "stretch" or
    funcName = "sony_arw_load_raw" or
    funcName = "parse_cine" or
    funcName = "parse_exif" or
    funcName = "kodak_262_load_raw" or
    funcName = "bayer" or
    funcName = "get4" or
    funcName = "green_matching" or
    funcName = "parse_thumb_note" or
    funcName = "parse_foveon" or
    funcName = "getbithuff" or
    funcName = "parse_tiff" or
    funcName = "getwords" or
    funcName = "jpeg_thumb_writer" or
    funcName = "hat_transform" or
    funcName = "setOlympusBodyFeatures" or
    funcName = "canon_has_lowbits" or
    funcName = "lossy_dng_load_raw" or
    funcName = "colorcheck" or
    funcName = "canon_600_load_raw" or
    funcName = "cam_xyz_coeff" or
    funcName = "setPhaseOneFeatures" or
    funcName = "fuji_rotate" or
    funcName = "ljpeg_diff" or
    funcName = "parse_qt" or
    funcName = "packed_dng_load_raw" or
    funcName = "canon_600_fixed_wb" or
    funcName = "kodak_yrgb_load_raw" or
    funcName = "lin_interpolate_loop" or
    funcName = "canon_load_raw" or
    funcName = "redcine_load_raw" or
    funcName = "double" or
    funcName = "strcasecmp" or
    funcName = "parse_external_jpeg" or
    funcName = "cubic_spline" or
    funcName = "powf64" or
    funcName = "parse_fuji" or
    funcName = "kodak_dc120_load_raw"
    // 可以继续添加其他函数名
}


"""

libtiff_targetFunctions = """predicate targetFunctions(string funcName) {
    funcName = "TIFFInitOJPEG" or
    funcName = "OJPEGPreDecode" or
    funcName = "OJPEGReadHeaderInfoSecTablesQTable" or
    funcName = "OJPEGWriteStreamAcTable" or
    funcName = "OJPEGDecodeRaw" or
    funcName = "OJPEGReadHeaderInfo" or
    funcName = "OJPEGReadHeaderInfoSecStreamSos" or
    funcName = "OJPEGReadHeaderInfoSecStreamDri" or
    funcName = "_TIFFmalloc" or
    funcName = "OJPEGReadHeaderInfoSecStreamDqt" or
    funcName = "OJPEGPostDecode" or
    funcName = "OJPEGLibjpegJpegSourceMgrSkipInputData" or
    funcName = "OJPEGDecodeScanlines" or
    funcName = "OJPEGReadWord" or
    funcName = "OJPEGCleanup" or
    funcName = "TIFFFdOpen" or
    funcName = "_tiffMapProc" or
    funcName = "OJPEGReadHeaderInfoSec" or
    funcName = "OJPEGLibjpegJpegErrorMgrErrorExit" or
    funcName = "OJPEGPreEncode" or
    funcName = "OJPEGVSetField" or
    funcName = "OJPEGLibjpegJpegSourceMgrInitSource" or
    funcName = "OJPEGWriteStreamSos" or
    funcName = "_TIFFmemcmp" or
    funcName = "OJPEGPostEncode" or
    funcName = "OJPEGWriteStreamEoi" or
    funcName = "_tiffWriteProc" or
    funcName = "OJPEGReadHeaderInfoSecStreamSof" or
    funcName = "OJPEGLibjpegJpegSourceMgrFillInputBuffer" or
    funcName = "OJPEGWriteStream" or
    funcName = "OJPEGWriteStreamDri" or
    funcName = "OJPEGReadSecondarySos" or
    funcName = "OJPEGSetupDecode" or
    funcName = "OJPEGPreDecodeSkipScanlines" or
    funcName = "OJPEGReadBufferFill" or
    funcName = "OJPEGVGetField" or
    funcName = "OJPEGSubsamplingCorrect" or
    funcName = "_TIFFmemset" or
    funcName = "OJPEGReadByte" or
    funcName = "OJPEGReadHeaderInfoSecStreamDht" or
    funcName = "OJPEGReadBytePeek" or
    funcName = "TIFFOpenW" or
    funcName = "OJPEGDecode" or
    funcName = "OJPEGEncode" or
    funcName = "OJPEGLibjpegJpegSourceMgrResyncToRestart" or
    funcName = "OJPEGSetupEncode" or
    funcName = "OJPEGWriteStreamSof" or
    funcName = "_TIFFrealloc" or
    funcName = "OJPEGReadHeaderInfoSecTablesAcTable" or
    funcName = "_tiffSizeProc" or
    funcName = "OJPEGLibjpegJpegSourceMgrTermSource" or
    funcName = "_TIFFfree" or
    funcName = "OJPEGReadByteAdvance" or
    funcName = "return" or
    funcName = "OJPEGWriteStreamQTable" or
    funcName = "TIFFOpen" or
    funcName = "_tiffCloseProc" or
    funcName = "_tiffSeekProc" or
    funcName = "OJPEGWriteStreamDcTable" or
    funcName = "_tiffReadProc" or
    funcName = "OJPEGLibjpegSessionAbort" or
    funcName = "OJPEGPreDecodeSkipRaw" or
    funcName = "OJPEGWriteStreamRst" or
    funcName = "OJPEGReadHeaderInfoSecTablesDcTable" or
    funcName = "jpeg_create_decompress_encap" or
    funcName = "OJPEGPrintDir" or
    funcName = "OJPEGReadSkip" or
    funcName = "OJPEGWriteStreamCompressed" or
    funcName = "OJPEGLibjpegJpegErrorMgrOutputMessage" or
    funcName = "OJPEGReadBlock" or
    funcName = "_tiffUnmapProc" or
    funcName = "_TIFFmemcpy" or
    funcName = "OJPEGWriteHeaderInfo" or
    funcName = "OJPEGWriteStreamSoi"
    // 可以继续添加其他函数名
}

"""

wolfssl_targetFunctions = """predicate targetFunctions(string funcName) {
    funcName = "wc_ecc_sign_hash_ex" or
    funcName = "wc_ecc_gen_k" or
    funcName = "wc_ecc_encrypt" or
    funcName = "wc_ecc_export_x963" or
    funcName = "wc_ecc_decrypt" or
    funcName = "wc_X963_KDF" or
    funcName = "wc_ecc_export_point_der" or
    funcName = "accel_fp_mul" or
    funcName = "accel_fp_mul2add" or
    funcName = "ecc_mul2add" or
    funcName = "wc_ecc_verify_hash_ex" or
    funcName = "wc_ecc_shared_secret_gen" or
    funcName = "ecc_check_privkey_gen" or
    funcName = "wc_ecc_curve_load_item" or
    funcName = "ecc_check_privkey_gen_helper" or
    funcName = "_wc_ecc_curve_free" or
    funcName = "wc_ecc_curve_load" or
    funcName = "wc_ecc_curve_cache_free" or
    funcName = "wc_ecc_curve_free" or
    funcName = "wc_ecc_shared_secret_gen_sync" or
    funcName = "wc_ecc_check_key" or
    funcName = "wc_ecc_import_x963_ex" or
    funcName = "wc_ecc_make_key_ex" or
    funcName = "wc_ecc_sign_hash" or
    funcName = "wc_ecc_mulmod_ex" or
    funcName = "ecc_check_pubkey_order" or
    funcName = "wc_ecc_free" or
    funcName = "wc_ecc_verify_hash" or
    funcName = "wc_ecc_shared_secret_ex" or
    funcName = "wc_ecc_init_ex" or
    funcName = "wc_ecc_free_rs" or
    funcName = "wc_ecc_shared_secret" or
    funcName = "wc_ecc_set_curve" or
    funcName = "wc_ecc_init" or
    funcName = "wc_ecc_import_raw" or
    funcName = "wc_ecc_set_custom_curve" or
    funcName = "wc_ecc_import_x963" or
    funcName = "wc_ecc_import_raw_ex" or
    funcName = "wc_ecc_import_raw_private" or
    funcName = "wc_ecc_get_oid" or
    funcName = "wc_ecc_dump_oids" or
    funcName = "wc_ecc_make_key" or
    funcName = "wc_ecc_export_x963_compressed" or
    funcName = "wc_SignatureGenerate" or
    funcName = "wc_SignatureDerEncode" or
    funcName = "wc_SignatureVerify" or
    funcName = "wc_SignatureVerifyHash" or
    funcName = "wc_SignatureGenerateHash" or
    funcName = "wc_SignatureGetSize" or
    funcName = "wc_ecc_sig_to_rs" or
    funcName = "wc_ecc_rs_raw_to_sig" or
    funcName = "wc_ecc_cmp_param" or
    funcName = "ecc_map" or
    funcName = "wc_ecc_rs_to_sig" or
    funcName = "wc_ecc_make_pub_ex" or
    funcName = "wc_ecc_is_point" or
    funcName = "ecc_projective_dbl_point" or
    funcName = "wc_ecc_import_point_der" or
    funcName = "ecc_projective_add_point" or
    funcName = "wc_ecc_fp_free" or
    funcName = "wc_ecc_make_pub" or
    funcName = "wc_ecc_import_private_key_ex" or
    funcName = "wc_ecc_export_raw" or
    funcName = "fp_to_unsigned_bin_at_pos" or
    funcName = "fp_read_radix" or
    funcName = "fp_read_radix_16" or
    funcName = "mp_addmod" or
    funcName = "mp_jacobi" or
    funcName = "wc_ecc_mulmod" or
    funcName = "build_lut" or
    funcName = "wc_ecc_shared_secret_ssh" or
    funcName = "mp_submod" or
    funcName = "fp_submod" or
    funcName = "mp_sqrtmod_prime" or
    funcName = "fp_mulmod" or
    funcName = "ecc_is_point" or
    funcName = "fp_addmod" or
    funcName = "mp_to_unsigned_bin" or
    funcName = "fp_isprime" or
    funcName = "fp_invmod" or
    funcName = "wc_ecc_ctx_set_info" or
    funcName = "mp_sqrmod" or
    funcName = "mp_div_2" or
    funcName = "find_hole" or
    funcName = "fp_count_bits" or
    funcName = "wc_ecc_ctx_new" or
    funcName = "ecc_new_point" or
    funcName = "fp_mod" or
    funcName = "s_is_power_of_two" or
    funcName = "fp_cmp_d" or
    funcName = "mp_sub_d" or
    funcName = "mp_mod" or
    funcName = "mp_lcm" or
    funcName = "mp_copy" or
    funcName = "mp_leading_bit" or
    funcName = "mp_count_bits" or
    funcName = "fp_prime_miller_rabin" or
    funcName = "fp_add_d" or
    funcName = "fp_set" or
    funcName = "fp_montgomery_setup" or
    funcName = "mp_invmod" or
    funcName = "fp_read_unsigned_bin" or
    funcName = "fp_div_2d" or
    funcName = "mp_add" or
    funcName = "mp_set" or
    funcName = "fp_mod_2d" or
    funcName = "wc_ecc_size" or
    funcName = "wc_ecc_ctx_set_peer_salt" or
    funcName = "mp_iszero" or
    funcName = "fp_leading_bit" or
    funcName = "mp_init_multi" or
    funcName = "fp_add" or
    funcName = "fp_lcm" or
    funcName = "wc_ecc_fp_free_cache" or
    funcName = "fp_gcd" or
    funcName = "mp_add_d" or
    funcName = "get_digit_count" or
    funcName = "fp_montgomery_calc_normalization" or
    funcName = "s_fp_sub" or
    funcName = "ecc_mulmod" or
    funcName = "fp_lshd" or
    funcName = "fp_mul_2d" or
    funcName = "wc_wc_ecc_export_x963_ex" or
    funcName = "mp_montgomery_calc_normalization" or
    funcName = "fp_cmp" or
    funcName = "wc_ecc_sig_size" or
    funcName = "mp_cnt_lsb" or
    funcName = "fp_2expt" or
    funcName = "mp_mul" or
    funcName = "ecc_ctx_init" or
    funcName = "CheckRunTimeSettings" or
    funcName = "fp_sub" or
    funcName = "fp_exptmod" or
    funcName = "fp_montgomery_reduce" or
    funcName = "_fp_exptmod" or
    funcName = "mp_exptmod" or
    funcName = "ecc_del_point" or
    funcName = "mp_rshb" or
    funcName = "add_entry" or
    funcName = "mp_clear" or
    funcName = "fp_mul" or
    funcName = "mp_read_unsigned_bin" or
    funcName = "mp_gcd" or
    funcName = "wc_ecc_ctx_reset" or
    funcName = "s_fp_add" or
    funcName = "mp_mulmod" or
    funcName = "fp_sqr_comba" or
    funcName = "ecc_is_valid_idx" or
    funcName = "fp_invmod_slow" or
    funcName = "mp_unsigned_bin_size" or
    funcName = "mp_prime_is_prime" or
    funcName = "mp_mod_d" or
    funcName = "mp_sub" or
    funcName = "fp_unsigned_bin_size" or
    funcName = "fp_div_2" or
    funcName = "mp_montgomery_reduce" or
    funcName = "fp_sqr" or
    funcName = "find_base" or
    funcName = "fp_cnt_lsb" or
    funcName = "mp_isodd" or
    funcName = "fp_reverse" or
    funcName = "ecc_get_key_sizes" or
    funcName = "mp_sqr" or
    funcName = "fp_mod_d" or
    funcName = "get_digit" or
    funcName = "wc_ecc_import_private_key" or
    funcName = "fp_sqrmod" or
    funcName = "fp_mul_comba" or
    funcName = "mp_init_copy" or
    funcName = "fp_sub_d" or
    funcName = "mp_div_2d" or
    funcName = "mp_set_int" or
    funcName = "fp_div" or
    funcName = "CheckRunTimeFastMath" or
    funcName = "ecc_ctx_set_salt" or
    funcName = "wc_ecc_ctx_free" or
    funcName = "mp_cmp" or
    funcName = "wc_ecc_ctx_get_own_salt" or
    funcName = "fp_to_unsigned_bin" or
    funcName = "fp_div_d" or
    funcName = "fp_rshb" or
    funcName = "fp_mul_d" or
    funcName = "wc_ecc_export_private_only" or
    funcName = "mp_cmp_d" or
    funcName = "mp_montgomery_setup" or
    funcName = "fp_cmp_mag" or
    funcName = "mp_read_radix" or
    funcName = "fp_rshd" or
    funcName = "fp_mul_2" or
    funcName = "mp_init"
    // 可以继续添加其他函数名
}

"""

imagemagick_targetFunctions = """predicate targetFunctions(string funcName) {
    funcName = "ReadPSDChannelZip" or
    funcName = "GetPSDRowSize" or
    funcName = "ConvertPSDCompression" or
    funcName = "ReadPSDChannel" or
    funcName = "ReadPSDLayer" or
    funcName = "GetPSDPacketSize" or
    funcName = "ReadPSDChannelRLE" or
    funcName = "ReadPSDChannelRaw" or
    funcName = "ReadPSDChannelPixels" or
    funcName = "ReadPSDRLEOffsets" or
    funcName = "ReadPSDImage" or
    funcName = "ReadPSDMergedImage" or
    funcName = "ReadPSDLayers" or
    funcName = "CorrectPSDOpacity" or
    funcName = "DrawImage" or
    funcName = "DrawDashPolygon" or
    funcName = "TracePath" or
    funcName = "GetDrawInfo" or
    funcName = "DrawClipPath" or
    funcName = "DrawPatternPath" or
    funcName = "DrawPrimitive" or
    funcName = "DrawPolygonPrimitive" or
    funcName = "DrawAffineImage" or
    funcName = "DrawGradientImage" or
    funcName = "GetPixelOpacity" or
    funcName = "DrawStrokePolygon" or
    funcName = "CloneDrawInfo" or
    funcName = "ReadDCMImage" or
    funcName = "ReadPICTImage" or
    funcName = "ReadTIFFImage" or
    funcName = "TIFFGetProperties" or
    funcName = "WriteTXTImage" or
    funcName = "ReadTXTImage" or
    funcName = "WritePTIFImage" or
    funcName = "TIFFSetProperties" or
    funcName = "InsertRow" or
    funcName = "ReadCUTImage" or
    funcName = "GetCutColors" or
    funcName = "SpliceImage" or
    funcName = "TransposeImage" or
    funcName = "TransverseImage" or
    funcName = "ConsolidateCMYKImages" or
    funcName = "ChopImage" or
    funcName = "FlipImage" or
    funcName = "ExcerptImage" or
    funcName = "CropImage" or
    funcName = "FlopImage" or
    funcName = "CopyImageRegion" or
    funcName = "ReadMATImage" or
    funcName = "WriteTGAImage" or
    funcName = "ReadTGAImage" or
    funcName = "WriteTGAPixel" or
    funcName = "ClampPixel" or
    funcName = "ClampImage" or
    funcName = "CompositeImage" or
    funcName = "CompositeOverImage" or
    funcName = "CompositeHSB" or
    funcName = "HSBComposite" or
    funcName = "TIFFAcquireCustomStreamForReading" or
    funcName = "TIFFSeekCustomStream" or
    funcName = "TIFFAcquireCustomStreamForWriting" or
    funcName = "TIFFTellCustomStream" or
    funcName = "InitPSDInfo" or
    funcName = "TIFFWritePhotoshopLayers" or
    funcName = "TIFFWriteCustomStream" or
    funcName = "TIFFReadPhotoshopLayers" or
    funcName = "TIFFReadCustomStream" or
    funcName = "WriteTIFFImage" or
    funcName = "AutoResizeImage" or
    funcName = "WriteICONImage" or
    funcName = "AcquireVirtualMemory" or
    funcName = "RelinquishVirtualMemory" or
    funcName = "AcquireQuantumMemory" or
    funcName = "ReadICONImage" or
    funcName = "DecodeImage" or
    funcName = "WritePICTImage" or
    funcName = "RegisterTIFFImage" or
    funcName = "UnregisterTIFFImage" or
    funcName = "ReadGROUP4Image" or
    funcName = "WriteGROUP4Image" or
    funcName = "WriteLSBLong" or
    funcName = "SetQuantumDepth" or
    funcName = "GetQuantumExtent" or
    funcName = "ProcessMSLScript" or
    funcName = "ReadPropertyUnsignedLong" or
    funcName = "ReadPropertySignedShort" or
    funcName = "ReadPropertyUnsignedShort" or
    funcName = "ReadPropertySignedLong" or
    funcName = "GetEXIFProperty" or
    funcName = "ReadPropertyShort" or
    funcName = "ReadProfileMSBLong" or
    funcName = "ReadProfileShort" or
    funcName = "ReadProfileLong" or
    funcName = "ReadPropertyMSBLong" or
    funcName = "Get8BIMProperty" or
    funcName = "TraceSVGClippath" or
    funcName = "TracePSClippath" or
    funcName = "ReadPropertyMSBShort" or
    funcName = "ReadPropertyLong" or
    funcName = "ReadProfileMSBShort" or
    funcName = "SyncExifProfile" or
    funcName = "Sync8BimProfile" or
    funcName = "RemoveImageProfile" or
    funcName = "GetProfilesFromResourceBlock" or
    funcName = "ReadResourceShort" or
    funcName = "DeleteImageProfile" or
    funcName = "WriteResourceLong" or
    funcName = "SetImageProfileInternal" or
    funcName = "SetImageProfile" or
    funcName = "WriteTo8BimProfile" or
    funcName = "WriteProfileShort" or
    funcName = "WriteProfileLong" or
    funcName = "SyncImageProfiles" or
    funcName = "SetImageProperty" or
    funcName = "WriteCompressionStart" or
    funcName = "WritePSDChannel" or
    funcName = "ReadSUNImage" or
    funcName = "WriteSUNImage" or
    funcName = "ReadHDRImage" or
    funcName = "WriteHDRImage" or
    funcName = "CLIListOperatorImages" or
    funcName = "WritePDFImage" or
    funcName = "ParseImageResourceBlocks" or
    funcName = "DestroyLayerInfo" or
    funcName = "WritePSDImage" or
    funcName = "WriteImageChannels" or
    funcName = "NegateCMYK" or
    funcName = "WriteResolutionResourceBlock" or
    funcName = "PSDPackbitsEncodeImage" or
    funcName = "SetPSDOffset" or
    funcName = "DecodePSDPixels" or
    funcName = "SetPSDSize" or
    funcName = "WritePascalString" or
    funcName = "WritePackbitsLength" or
    funcName = "WriteOneChannel" or
    funcName = "SetPixelY" or
    funcName = "SetPixelIndex" or
    funcName = "GetPixelChannel" or
    funcName = "GetPixelCyan" or
    funcName = "GetPixelInfoIntensity" or
    funcName = "IsPixelInfoEquivalent" or
    funcName = "GetPixelY" or
    funcName = "GetPixelYellowTraits" or
    funcName = "SetPixelGreen" or
    funcName = "GetPixelInfoLuminance" or
    funcName = "GetPixelAlphaTraits" or
    funcName = "GetPixelTraits" or
    funcName = "GetPixelRedTraits" or
    funcName = "SetPixelCyan" or
    funcName = "IsPixelGray" or
    funcName = "IsPixelInfoMonochrome" or
    funcName = "SetPixelBlue" or
    funcName = "GetPixelMetacontentExtent" or
    funcName = "IsPixelMonochrome" or
    funcName = "SetPixelInfoPixel" or
    funcName = "GetPixelAlpha" or
    funcName = "SetPixelRed" or
    funcName = "GetPixelCyanTraits" or
    funcName = "GetPixelInfoPixel" or
    funcName = "GetPixelCb" or
    funcName = "SetPixelChannel" or
    funcName = "GetPixelGrayTraits" or
    funcName = "GetPixelLuminance" or
    funcName = "GetPixelChannels" or
    funcName = "SetPixelBlack" or
    funcName = "SetPixelChannelMapChannel" or
    funcName = "GetPixelCbTraits" or
    funcName = "GetPixelMagenta" or
    funcName = "IsPixelInfoGray" or
    funcName = "GetPixelBlue" or
    funcName = "SetPixelCb" or
    funcName = "SetPixelAlpha" or
    funcName = "GetPixelGreen" or
    funcName = "GetPixelCr" or
    funcName = "GetPixelBlack" or
    funcName = "GetPixelMagentaTraits" or
    funcName = "GetPixelRed" or
    funcName = "GetPixelIntensity" or
    funcName = "GetPixelChannelMapTraits" or
    funcName = "GetPixelChannelMapChannel" or
    funcName = "SetPixelInfo" or
    funcName = "GetPixelMetaChannels" or
    funcName = "IsPixelEquivalent" or
    funcName = "GetPixelGreenTraits" or
    funcName = "GetPixelGray" or
    funcName = "SetPixelGray" or
    funcName = "SetPixelYellow" or
    funcName = "GetPixelIndexTraits" or
    funcName = "GetPixelYellow" or
    funcName = "SetPixelMagenta" or
    funcName = "GetPixelYTraits" or
    funcName = "SetPixelCr" or
    funcName = "GetPixelBlueTraits" or
    funcName = "GetPixelCrTraits" or
    funcName = "GetPixelBlackTraits" or
    funcName = "GetPixelIndex" or
    funcName = "RenderMVGContent" or
    funcName = "TraceBezier" or
    funcName = "ReadXBMImage" or
    funcName = "XBMInteger" or
    funcName = "ReadYUVImage" or
    funcName = "CheckMemoryOverflow" or
    funcName = "ReadVIFFImage" or
    funcName = "AcquireAlignedMemory" or
    funcName = "ResizeQuantumMemory" or
    funcName = "ReadLABELImage" or
    funcName = "InitializeExceptionInfo" or
    funcName = "DestroyExceptionInfo" or
    funcName = "CatchException" or
    funcName = "ThrowMagickExceptionList" or
    funcName = "WriteVIFFImage" or
    funcName = "GetVirtualMemoryBlob" or
    funcName = "InheritException" or
    funcName = "ClearMagickException" or
    funcName = "ThrowException" or
    funcName = "ReadRLEImage" or
    funcName = "ReadPSDLayersInternal" or
    funcName = "FilterAdditionalLayerInformation" or
    funcName = "ReversePSDString" or
    funcName = "GetPSDSize" or
    funcName = "WriteGIFImage" or
    funcName = "ReadGIFImage" or
    funcName = "WriteCALSImage" or
    funcName = "ReadCALSImage" or
    funcName = "RegisterPNGImage" or
    funcName = "ReadOnePNGImage" or
    funcName = "WriteOnePNGImage" or
    funcName = "UnregisterPNGImage" or
    funcName = "LocaleUppercase" or
    funcName = "LocaleLowercase" or
    funcName = "LocaleLower" or
    funcName = "LocaleUpper" or
    funcName = "WaveletDenoiseImage" or
    funcName = "HatTransform" or
    funcName = "ImportCMYKQuantum" or
    funcName = "ImportBGRAQuantum" or
    funcName = "ImportRGBQuantum" or
    funcName = "ImportRGBAQuantum" or
    funcName = "ImportBlueQuantum" or
    funcName = "ImportAlphaQuantum" or
    funcName = "ImportBGRQuantum" or
    funcName = "ImportQuantumPixels" or
    funcName = "ImportIndexQuantum" or
    funcName = "ImportGrayAlphaQuantum" or
    funcName = "ImportCbYCrYQuantum" or
    funcName = "ImportRedQuantum" or
    funcName = "ImportOpacityQuantum" or
    funcName = "ImportBlackQuantum" or
    funcName = "ImportGreenQuantum" or
    funcName = "ImportIndexAlphaQuantum" or
    funcName = "ImportGrayQuantum" or
    funcName = "ImportCMYKAQuantum" or
    funcName = "PushColormapIndex" or
    funcName = "sixel_decode" or
    funcName = "ReadSIXELImage" or
    funcName = "WriteSIXELImage" or
    funcName = "sixel_advance" or
    funcName = "RegisterSIXELImage" or
    funcName = "sixel_put_flash" or
    funcName = "hls_to_rgb" or
    funcName = "get_params" or
    funcName = "sixel_put_pixel" or
    funcName = "sixel_output_create" or
    funcName = "IsSIXEL" or
    funcName = "sixel_put_node" or
    funcName = "sixel_node_del" or
    funcName = "UnregisterSIXELImage" or
    funcName = "sixel_encode_impl" or
    funcName = "hue_to_rgb" or
    funcName = "EnhanceImage" or
    funcName = "ReadCINImage" or
    funcName = "WriteJNGImage" or
    funcName = "ReadJNGImage" or
    funcName = "LosslessReduceDepthOK" or
    funcName = "WriteMNGImage" or
    funcName = "WritePNGImage" or
    funcName = "WriteOneJNGImage" or
    funcName = "ImageIsGray" or
    funcName = "MagickPNGWarningHandler" or
    funcName = "ReadMNGImage" or
    funcName = "ReadOneJNGImage" or
    funcName = "Magick_png_read_raw_profile" or
    funcName = "ReadPNGImage" or
    funcName = "MagickPNGErrorHandler" or
    funcName = "mng_read_box" or
    funcName = "read_user_chunk_callback" or
    funcName = "ReadMATImageV4" or
    funcName = "AnnotateImage" or
    funcName = "ReadWPGImage" or
    funcName = "ReadSVGImage" or
    funcName = "ComplexImages" or
    funcName = "ConcatenateImages" or
    funcName = "ProcessScriptOptions" or
    funcName = "MagickImageCommand" or
    funcName = "ProcessCommandOptions" or
    funcName = "MagickCommandProcessOptions" or
    funcName = "MagickSpecialOption" or
    funcName = "MagickUsage" or
    funcName = "ReadYCBCRImage" or
    funcName = "ReadICCProfile" or
    funcName = "ReadIPTCProfile" or
    funcName = "ReadProfile" or
    funcName = "GetCharacter" or
    funcName = "ReadComment" or
    funcName = "ReadJPEGImage" or
    funcName = "Image" or
    funcName = "quiet" or
    funcName = "draw" or
    funcName = "geometry" or
    funcName = "montageGeometry" or
    funcName = "format" or
    funcName = "read" or
    funcName = "directory" or
    funcName = "medianFilter" or
    funcName = "fillPattern" or
    funcName = "contrastStretchChannel" or
    funcName = "colorMap" or
    funcName = "swirl" or
    funcName = "contrast" or
    funcName = "mask" or
    funcName = "rotationalBlur" or
    funcName = "iptcProfile" or
    funcName = "transform" or
    funcName = "clamp" or
    funcName = "equalize" or
    funcName = "flop" or
    funcName = "transpose" or
    funcName = "colorMatrix" or
    funcName = "gaussianBlurChannel" or
    funcName = "adaptiveResize" or
    funcName = "autoGamma" or
    funcName = "syncPixels" or
    funcName = "polaroid" or
    funcName = "sigmoidalContrast" or
    funcName = "vignette" or
    funcName = "crop" or
    funcName = "morphologyChannel" or
    funcName = "uniqueColors" or
    funcName = "frame" or
    funcName = "writePixels" or
    funcName = "cdl" or
    funcName = "blur" or
    funcName = "grayscale" or
    funcName = "shear" or
    funcName = "deskew" or
    funcName = "floodFill" or
    funcName = "edge" or
    funcName = "alpha" or
    funcName = "perceptible" or
    funcName = "composite" or
    funcName = "gaussianBlur" or
    funcName = "autoOrient" or
    funcName = "thumbnail" or
    funcName = "haldClut" or
    funcName = "autoGammaChannel" or
    funcName = "brightnessContrast" or
    funcName = "quantize" or
    funcName = "stegano" or
    funcName = "cycleColormap" or
    funcName = "sepiaTone" or
    funcName = "charcoal" or
    funcName = "write" or
    funcName = "modifyImage" or
    funcName = "linearStretch" or
    funcName = "selectiveBlurChannel" or
    funcName = "annotate" or
    funcName = "autoLevel" or
    funcName = "selectiveBlur" or
    funcName = "motionBlur" or
    funcName = "compare" or
    funcName = "threshold" or
    funcName = "transverse" or
    funcName = "strip" or
    funcName = "opaque" or
    funcName = "orderedDitherChannel" or
    funcName = "levelColors" or
    funcName = "totalColors" or
    funcName = "profile" or
    funcName = "map" or
    funcName = "rotate" or
    funcName = "orderedDither" or
    funcName = "affineTransform" or
    funcName = "modulate" or
    funcName = "display" or
    funcName = "sharpenChannel" or
    funcName = "tint" or
    funcName = "whiteThreshold" or
    funcName = "morphology" or
    funcName = "blackThreshold" or
    funcName = "chop" or
    funcName = "zoom" or
    funcName = "shadow" or
    funcName = "blurChannel" or
    funcName = "pixelColor" or
    funcName = "getMetacontent" or
    funcName = "distort" or
    funcName = "comment" or
    funcName = "flip" or
    funcName = "clut" or
    funcName = "classType" or
    funcName = "type" or
    funcName = "houghLine" or
    funcName = "negate" or
    funcName = "wave" or
    funcName = "convolve" or
    funcName = "attribute" or
    funcName = "randomThresholdChannel" or
    funcName = "unsharpmaskChannel" or
    funcName = "decipher" or
    funcName = "border" or
    funcName = "compareChannel" or
    funcName = "kuwaharaChannel" or
    funcName = "spread" or
    funcName = "determineType" or
    funcName = "shave" or
    funcName = "fontTypeMetrics" or
    funcName = "exifProfile" or
    funcName = "normalize" or
    funcName = "getConstPixels" or
    funcName = "reduceNoise" or
    funcName = "colorSpaceType" or
    funcName = "scale" or
    funcName = "level" or
    funcName = "inverseFourierTransform" or
    funcName = "roll" or
    funcName = "whiteThresholdChannel" or
    funcName = "transparent" or
    funcName = "trim" or
    funcName = "liquidRescale" or
    funcName = "randomThreshold" or
    funcName = "contrastStretch" or
    funcName = "cannyEdge" or
    funcName = "channelDepth" or
    funcName = "sharpen" or
    funcName = "emboss" or
    funcName = "sketch" or
    funcName = "shade" or
    funcName = "colorMapSize" or
    funcName = "label" or
    funcName = "replaceImage" or
    funcName = "gamma" or
    funcName = "getConstMetacontent" or
    funcName = "blackThresholdChannel" or
    funcName = "minify" or
    funcName = "splice" or
    funcName = "clampChannel" or
    funcName = "posterize" or
    funcName = "alphaChannel" or
    funcName = "extent" or
    funcName = "connectedComponents" or
    funcName = "modulusDepth" or
    funcName = "addNoise" or
    funcName = "despeckle" or
    funcName = "fx" or
    funcName = "oilPaint" or
    funcName = "boundingBox" or
    funcName = "adaptiveBlur" or
    funcName = "setPixels" or
    funcName = "adaptiveSharpenChannel" or
    funcName = "rotationalBlurChannel" or
    funcName = "channel" or
    funcName = "process" or
    funcName = "perceptibleChannel" or
    funcName = "colorize" or
    funcName = "quantumOperator" or
    funcName = "addNoiseChannel" or
    funcName = "raise" or
    funcName = "subImageSearch" or
    funcName = "strokePattern" or
    funcName = "enhance" or
    funcName = "statistics" or
    funcName = "clipPath" or
    funcName = "blueShift" or
    funcName = "implode" or
    funcName = "resample" or
    funcName = "stereo" or
    funcName = "virtualPixelMethod" or
    funcName = "fontTypeMetricsMultiline" or
    funcName = "moments" or
    funcName = "resize" or
    funcName = "encipher" or
    funcName = "sparseColor" or
    funcName = "levelColorsChannel" or
    funcName = "autoLevelChannel" or
    funcName = "adaptiveThreshold" or
    funcName = "transparentChroma" or
    funcName = "floodFillAlpha" or
    funcName = "clip" or
    funcName = "adaptiveSharpen" or
    funcName = "formatExpression" or
    funcName = "sample" or
    funcName = "magnify" or
    funcName = "posterizeChannel" or
    funcName = "segment" or
    funcName = "readPixels" or
    funcName = "getPixels" or
    funcName = "negateChannel" or
    funcName = "solarize" or
    funcName = "separate" or
    funcName = "levelChannel" or
    funcName = "unsharpmask" or
    funcName = "erase" or
    funcName = "colorSpace" or
    funcName = "brightnessContrastChannel" or
    funcName = "clutChannel" or
    funcName = "kuwahara" or
    funcName = "perceptualHash" or
    funcName = "texture" or
    funcName = "ModeToString" or
    funcName = "CompositeOperatorToPSDBlendMode" or
    funcName = "load_tile" or
    funcName = "ReadSGIImage" or
    funcName = "RemoveResolutionFromResourceBlock" or
    funcName = "WritePSDOffset" or
    funcName = "WriteChannelSize" or
    funcName = "AcquireCompactPixels" or
    funcName = "ImportCMYKOQuantum" or
    funcName = "ImportRGBOQuantum" or
    funcName = "ImportBGROQuantum" or
    funcName = "ReadBMPImage" or
    funcName = "EqualizeImage" or
    funcName = "ModulateImage" or
    funcName = "ContrastImage" or
    funcName = "GrayscaleImage" or
    funcName = "ReadMPCImage" or
    funcName = "WriteMPCImage" or
    funcName = "GammaImage" or
    funcName = "SigmoidalContrastImage" or
    funcName = "LevelImage" or
    funcName = "LevelImageColors" or
    funcName = "BrightnessContrastImage" or
    funcName = "ContrastStretchImage" or
    funcName = "LevelizeImage" or
    funcName = "ClutImage" or
    funcName = "ColorDecisionListImage" or
    funcName = "NegateImage" or
    funcName = "HaldClutImage" or
    funcName = "LinearStretchImage" or
    funcName = "LevelPixel" or
    funcName = "ReadXWDImage" or
    funcName = "RegisterXWDImage" or
    funcName = "RegisterHDRImage" or
    funcName = "IsHDR"
    // 可以继续添加其他函数名
}


"""