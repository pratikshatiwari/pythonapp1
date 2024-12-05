import python

from PyLiteralExpr string
where
  string.getValue().regexpMatch("(?i)(password|secret|token)")
select string, "Potential hardcoded sensitive information found."