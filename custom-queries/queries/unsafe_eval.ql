/**
 * @name Unsafe eval usage
 * @description Finds unsafe usage of the eval function in Python code
 * @kind problem
 */

import python

from CallExpr call
where call.getTarget().hasName("eval")
select call, "Unsafe usage of eval detected."
