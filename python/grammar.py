grammar = r"""
source = eol* (func_def (eol* func_def)*)? eol*
func_def = "fn" whitespace+ var whitespace* "(" list_contents "):" whitespace* eol indent eol line+ dedent eol

line = for / return / assign

assign = var whitespace* "=" whitespace* expr eol
return = "return" whitespace+ expr eol

for = "for" whitespace+ var whitespace+ "in" whitespace+ var whitespace* ":" eol indent eol assign+ dedent eol

expr = value

list = "[" whitespace* list_contents whitespace* "]"
list_contents = (var (tail_arg)*)?
tail_arg = comma whitespace* value whitespace*

add = "+"
sub = "-"
mult = "*"
div = "/"
comma = ","
indent = "{"
dedent = "}"
value = var / int_literal
var = ~r"[a-zA-Z_][a-zA-Z0-9_]*"
int_literal = ~r"[1-9][0-9]*"
whitespace = (" " / "\t")+
eol = "\n" / "\r" / "\r\n" / "\n\r"
"""
