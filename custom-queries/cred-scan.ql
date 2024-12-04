import python

from Literal string, Variable variable
where string.isStringLiteral() and
      (
        string.toLowerCase().matches("%password%") or
        string.toLowerCase().matches("%secret%") or
        string.toLowerCase().matches("%token%")
      )
select variable, "Hardcoded sensitive information found in this variable."