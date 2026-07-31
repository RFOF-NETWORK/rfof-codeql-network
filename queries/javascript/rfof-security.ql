/**
 * @name RFOF JavaScript Strict Security Rule
 * @description Enforces global security standards in the JavaScript/TypeScript monolith and blocks insecure code evaluations.
 * @kind problem
 * @security-severity 8.5
 * @precision high
 * @id rfof/javascript/strict-security
 * @tags security
 */

import javascript

from DataFlow::Node source, DataFlow::Node sink, GlobalEvalCall eval
where eval.getArgument() = sink.asExpr()
select sink, "RFOF WARNING: Insecure code execution (GlobalEval) detected in the decentralized network monolith!"
