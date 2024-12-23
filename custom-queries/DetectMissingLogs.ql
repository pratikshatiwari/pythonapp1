import python

/**
 * Detect functions where logging is missing.
 */
from Call c
where
  // Ensure the call is not a logging-related function
  not exists(Call logCall |
    logCall.getCallee().getName().matches("log|logger|audit") and
    logCall.getEnclosingCallable() = c.getEnclosingCallable())
select c, "This function call might require logging."
