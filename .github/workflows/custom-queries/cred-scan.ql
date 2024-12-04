import python

from Literal string
where
  string.isStringLiteral() and
  (
    string.getValue().toLowerCase().matches("%password%") or
    string.getValue().toLowerCase().matches("%secret%") or
    string.getValue().toLowerCase().matches("%token%")
  )
select string, "Hardcoded sensitive information found: " + string.getValue()
