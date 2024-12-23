import python

from FunctionCall fc, Function f
where
  fc.getEnclosingCallable() = f and
  not exists(FunctionCall logCall |
    logCall.getEnclosingCallable() = f and
    logCall.getTarget().getName().matches("log|logger|audit"))
select fc, "Critical operation without logging detected."
