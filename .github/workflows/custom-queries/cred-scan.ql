import python

/**
 * Identifies hardcoded strings in Python files
 * that may indicate sensitive information, such as passwords, secrets, or tokens.
 */
from PyLiteralExpr string
where
  string.getValue().regexpMatch("(?i)(password|secret|token)")
select string, "Hardcoded sensitive information found: " + string.getValue()