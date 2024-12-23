import python
import semmle.python.security.dataflow.DefaultTaintTracking

from FunctionCall fc
select fc, "Potential issue with this function call."
