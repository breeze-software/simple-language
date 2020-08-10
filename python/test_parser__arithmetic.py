import parser
from pprint import pprint

import pre


def test__addition__basic():
    data = "a + b"
    expected = {
        "node": "+",
        "left": {"node": "variable", "name": "a"},
        "right": {"node": "variable", "name": "b"},
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="expr")
    assert output == expected


def test__addition__multiple():
    data = "a + b + c + d"
    expected = {
        "node": "+",
        "left": {"node": "variable", "name": "a"},
        "right": {
            "node": "+",
            "left": {"node": "variable", "name": "b"},
            "right": {
                "node": "+",
                "left": {"node": "variable", "name": "c"},
                "right": {"node": "variable", "name": "d"},
            },
        },
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="expr")
    assert output == expected


def test__addition_and_multiplication():
    data = "a * b + c * d"
    expected = {
        "node": "+",
        "left": {
            "node": "*",
            "left": {"node": "variable", "name": "a"},
            "right": {"node": "variable", "name": "b"},
        },
        "right": {
            "node": "*",
            "left": {"node": "variable", "name": "c"},
            "right": {"node": "variable", "name": "d"},
        },
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="expr")
    assert output == expected
