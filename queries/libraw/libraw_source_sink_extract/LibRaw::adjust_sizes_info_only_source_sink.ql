/**
 * @name Find upstream sources and downstream sinks for function_name
 * @description Finds the ultimate sources flowing into function_name and ultimate sinks receiving data from function_name
 * @kind problem
 * @problem.severity warning
 * @id cpp/function-flow-endpoints
 */

import cpp
import semmle.code.cpp.dataflow.new.DataFlow
import semmle.code.cpp.dataflow.new.TaintTracking

// 定义向下游追踪的配置
class DownstreamFlow extends TaintTracking::Configuration {
    DownstreamFlow() { this = "DownstreamFlow" }

    // ReadPSDChannelZip作为source
    override predicate isSource(DataFlow::Node source) {
        exists(FunctionCall fc |
            fc.getTarget().getName() = "LibRaw::adjust_sizes_info_only" and
            (
                // 函数调用本身作为source
                source.asExpr() = fc
                or
                // 函数的参数作为source（可能被修改的参数）
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
                fc.getTarget().getName().matches("%write%") or
                fc.getTarget().getName().matches("%Write%") or
                fc.getTarget().getName().matches("%put%") or
                fc.getTarget().getName().matches("%Put%")
            )
            or
            // 网络发送
            exists(FunctionCall fc | e = fc.getAnArgument() |
                fc.getTarget().getName().matches("%send%") or
                fc.getTarget().getName().matches("%Send%")
            )
            or
            // 命令执行
            exists(FunctionCall fc | e = fc.getAnArgument() |
                fc.getTarget().getName() = "system" or
                fc.getTarget().getName().matches("%exec%") or
                fc.getTarget().getName().matches("%spawn%")
            )
            or
            // 内存写入
            exists(FunctionCall fc | e = fc.getAnArgument() |
                fc.getTarget().getName().matches("%memcpy%") or
                fc.getTarget().getName().matches("%strcpy%")
            )
        )
    }
}

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

    // ReadPSDChannelZip作为sink
    override predicate isSink(DataFlow::Node sink) {
        exists(FunctionCall fc |
            fc.getTarget().getName() = "LibRaw::adjust_sizes_info_only" and
            sink.asExpr() = fc.getAnArgument()
        )
    }
}

// 获取所有相关的source和sink
from
    DataFlow::Node source,
    DataFlow::Node sink,
    string flowDescription,
    string sourceInfo,
    string sinkInfo
where
    (
        // 向下游的数据流
        exists(DownstreamFlow downConfig |
            downConfig.hasFlow(source, sink) and
            flowDescription = "Downstream flow from function_name to sink" and
            (
                exists(FunctionCall fc | source.asExpr() = fc |
                    sourceInfo = "Function call: " + fc.getTarget().getName()
                )
                or
                exists(FunctionCall fc, int i | source.asExpr() = fc.getArgument(i) |
                    sourceInfo = "Argument " + i + " of " + fc.getTarget().getName()
                )
            ) and
            (
                exists(FunctionCall fc | sink.asExpr() = fc.getAnArgument() |
                    sinkInfo = "Argument of " + fc.getTarget().getName()
                )
                or
                exists(FunctionCall fc | sink.asExpr() = fc |
                    sinkInfo = "Call to " + fc.getTarget().getName()
                )
            )
        )
        or
        // 向上游的数据流
        exists(UpstreamFlow upConfig |
            upConfig.hasFlow(source, sink) and
            flowDescription = "Upstream flow from source to function_name" and
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
    )
select
    source,
    sink,
    flowDescription + "\n" +
    "Source: " + sourceInfo + " at " + source.getLocation().toString() + "\n" +
    "Sink: " + sinkInfo + " at " + sink.getLocation().toString()

