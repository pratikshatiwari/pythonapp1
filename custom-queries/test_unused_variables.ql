import python

/**
 * @name Unused variable
 * @description Identifies variables that are declared but never used.
 * @kind problem
 * @tags maintainability
 * @problem.severity warning
 */
from LocalVariable v
where not exists (v.getAnAccess())
select v, "The variable '" + v.getName() + "' is declared but never used."
