import python

/**
 * Detect critical functions where logging is missing.
 */
from Call c, Function f
where
  c.getEnclosingCallable() = f and
  not exists(Call logCall |
    logCall.getEnclosingCallable() = f and
    logCall.getFunction().getName().matches("log|logger|audit"))
select c, "Critical operation without logging detected."
