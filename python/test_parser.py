import parser

import pre


def test_variable():
    data = "abc"
    expected = {"node": "variable", "name": "abc"}

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="var")
    assert output == expected

    data = "_4thing__something2_3__"
    expected = {"node": "variable", "name": "_4thing__something2_3__"}

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="var")
    assert output == expected


def test__function_signature__minimal():
    data = "fn abc():"
    expected = {
        "args": [],
        "name": {"name": "abc", "node": "variable"},
        "node": "function",
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="func_signature")
    assert output == expected


def test__function_signature__single_arg():
    data = "fn abc(a):"
    expected = {
        "args": [{"name": "a", "node": "variable"}],
        "name": {"name": "abc", "node": "variable"},
        "node": "function",
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="func_signature")
    assert output == expected


def test__function_signature__multiple_args():
    data = "fn abc(a, b, c):"
    expected = {
        "args": [
            {"name": "a", "node": "variable"},
            {"name": "b", "node": "variable"},
            {"name": "c", "node": "variable"},
        ],
        "name": {"name": "abc", "node": "variable"},
        "node": "function",
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="func_signature")
    assert output == expected


def test__for_signature__basic():
    data = "for a in b:"
    expected = {
        "iterator": {"name": "b", "node": "variable"},
        "node": "for",
        "var": {"name": "a", "node": "variable"},
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="for_signature")
    assert output == expected
