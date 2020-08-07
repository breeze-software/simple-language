from pprint import pprint

import grammar as g
import pre
import writer
from parsimonious.grammar import Grammar
from visitor import SourceVisitor


def read_grammar():
    return Grammar(g.grammar)


def read_code():
    with open("code.lang", "r") as f:
        code = f.read()
    return code


def parse(grammar, source, entry="source"):
    source = pre.insert_brackets(source)

    tree = grammar[entry].parse(source)
    sv = SourceVisitor()
    output = sv.visit(tree)
    return output
