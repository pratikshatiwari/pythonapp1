import python

/**
 * Detect functions where logging is missing.
 */
from Call c
where
  not exists(FunctionCall logCall |
    logCall.getEnclosingCallable() = c.getEnclosingCallable() and
    logCall.getFunction().getName().matches("log|logger|audit"))
select c, "Missing log calls detected in critical function."
