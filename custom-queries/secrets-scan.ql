import python

/**
 * Detect hardcoded sensitive information like passwords or tokens.
 */
from Literal string
where
  string.getValue().regexpMatch("(?i)(password|token|secret|api_key)")
select string, "Potential hardcoded sensitive information: " + string.getValue()