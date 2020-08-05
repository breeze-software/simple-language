from pprint import pprint

import grammar as g
from parsimonious.grammar import Grammar
from visitor import SourceVisitor


def get_grammar():
    return Grammar(g.grammar)


data = "\n".join(
    [
        "fn something(a, b, c):",
        "{",
        "    c = a",
        "    c = 5",
        "    for i in something:",
        "{",
        "        a = c",
        "}",
        "    return c",
        "}",
        "",
    ]
)
#        "    c = 1 + 2 + a * b + c * 5",


def read_code():
    with open("code.lang", "r") as f:
        code = f.read()
    return code


def insert_brackets(code):
    code = [""] + code.split("\n") + ["", ""]

    out = []
    for a, b in zip(code, code[1:]):
        a = a.replace("\t", "    ")
        b = b.replace("\t", "    ")
        indent_a = len(a) - len(a.lstrip(" "))
        indent_b = len(b) - len(b.lstrip(" "))
        if indent_a > indent_b:
            out.append(a.lstrip(" "))
            out.append("}")
        elif indent_b > indent_a:
            out.append(a.lstrip(" "))
            out.append("{")
        else:
            out.append(a.lstrip(" "))

    return "\n".join(out)


grammar = get_grammar()

data = read_code()
print(data)
print("-" * 20)
data = insert_brackets(data)
print(data)
print("-" * 20)

tree = grammar.parse(data)
# print(tree)
sv = SourceVisitor()
output = sv.visit(tree)
print("\n\n\n")
pprint(output)
