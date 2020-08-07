grammar = r"""
source = eol* (func_def (eol* func_def)*)? eol*
func_def = func_signature eol indent eol body dedent eol
func_signature = "fn" whitespace+ var whitespace* "(" func_args "):" whitespace*

func_args = (var (comma whitespace* var whitespace*)*)?

body = (block / line)+
block = for / if
line = stmt_return / stmt_assign

stmt_assign = assign_target whitespace* "=" whitespace* expr eol
stmt_return = "return" whitespace+ expr eol

for = for_signature eol indent eol body dedent eol
for_signature = "for" whitespace+ assign_target whitespace+ "in" whitespace+ var whitespace* ":" whitespace*

if = if_block elseif_block* else_block?

if_block = if_signature eol indent eol body dedent eol
if_signature = "if" whitespace+ expr whitespace* ":" whitespace*

elseif_block = elseif_signature eol indent eol body dedent eol
elseif_signature = "else if" whitespace+ expr whitespace* ":" whitespace*

else_block = else_signature eol indent eol body dedent eol
else_signature = "else" whitespace* ":" whitespace*

assign_target = var

expr = expr_add_sub / value

expr_add_sub = value whitespace* (add / sub) whitespace* value whitespace*

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
