import python

from Call c
where c.getCallee().getName() = "eval"
select c, "Avoid using 'eval', as it can introduce security vulnerabilities."
