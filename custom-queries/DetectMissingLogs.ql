import python

/**
 * Detect functions where logging is missing.
 */
from Call c
where
  not exists(Call logCall |
    logCall.getTarget().getName().matches("log|logger|audit") and
    logCall.getEnclosingCallable().getName() = c.getEnclosingCallable().getName())
select c, "Missing log calls detected in critical function."
