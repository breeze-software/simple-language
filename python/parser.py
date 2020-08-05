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
    tree = grammar[entry].parse(source)
    sv = SourceVisitor()
    output = sv.visit(tree)
    return output


if __name__ == "__main__":
    print("-" * 20)
    data = read_code()
    print(data)

    print("-" * 20)
    data = pre.insert_brackets(data)
    print(data)

    print("\n\n\n")
    print("-" * 20)
    grammar = read_grammar()
    output = parse(grammar, data)
    pprint(output)

    print("-" * 20)
    print(writer.scribe(output))
    print("-" * 20)
