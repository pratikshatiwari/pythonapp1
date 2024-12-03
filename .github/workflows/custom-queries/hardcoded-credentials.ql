/**
 * @name Hardcoded Credentials
 * @description Detects hardcoded usernames and passwords in Python code
 * @kind problem
 * @problem.severity error
 * @security-severity 9.0
 * @precision high
 * @id python/hardcoded-credentials
 * @tags security
 *       credentials
 */

import python

from StringLiteral str
where
  exists(AssignStmt assign |
    assign.getValue() = str and
    (
      assign.getTarget().(Name).getId().toLowerCase().matches("%password%") or
      assign.getTarget().(Name).getId().toLowerCase().matches("%passwd%") or
      assign.getTarget().(Name).getId().toLowerCase().matches("%secret%") or
      assign.getTarget().(Name).getId().toLowerCase().matches("%key%") or
      assign.getTarget().(Name).getId().toLowerCase().matches("%token%") or
      assign.getTarget().(Name).getId().toLowerCase().matches("%username%") or
      assign.getTarget().(Name).getId().toLowerCase().matches("%user%")
    )
  )
select str, "Hardcoded credential detected"