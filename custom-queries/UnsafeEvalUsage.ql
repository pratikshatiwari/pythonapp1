/**
 * @name Unsafe usage of eval()
 * @description Identifies cases where the `eval()` function is used, which can lead to code execution vulnerabilities.
 * @kind problem
 * @problem.severity error
 * @tags security
 *       external/cwe/cwe-95
 * @id python/UnsafeEvalUsage
 */

import python

/** Find calls to the eval function */
from CallExpr call
where
  call.getTarget().getName() = "eval"
select call, "Unsafe usage of eval() function."
