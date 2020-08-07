import json
import parser
from pprint import pprint

import pre
import writer


def load_testing_triple(name):
    with open(f"./tests/data/{name}.input.lang", "r") as f:
        a = f.read()
    with open(f"./tests/data/{name}.ast.json", "r") as f:
        b = json.load(f)
    with open(f"./tests/data/{name}.output.lua", "r") as f:
        c = f.read()
    return (a, b, c)


def test__integration():
    _input, _ast, _output = load_testing_triple("a")

    grammar = parser.read_grammar()
    _ast2 = parser.parse(grammar, _input)
    _output2 = writer.scribe(_ast2)

    print("\n\n\n")
    pprint(_ast2)
    print("\n\n\n")
    print(_output2)
    print("\n\n\n")

    assert _ast == _ast2
    assert _output == _output2
