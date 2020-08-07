import parser

import pre


def test__function_signature__minimal():
    data = "fn abc():"
    expected = {"node": "function", "name": "abc", "args": []}

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="func_signature")
    assert output == expected


def test__function_signature__single_arg():
    data = "fn abc(a):"
    expected = {
        "node": "function",
        "name": "abc",
        "args": [{"name": "a", "node": "variable"}],
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="func_signature")
    assert output == expected


def test__function_signature__multiple_args():
    data = "fn abc(a, b, c):"
    expected = {
        "node": "function",
        "name": "abc",
        "args": [
            {"name": "a", "node": "variable"},
            {"name": "b", "node": "variable"},
            {"name": "c", "node": "variable"},
        ],
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="func_signature")
    assert output == expected


def test__func_def__basic():
    data = "fn something(a):\n    return 4"
    expected = {
        "node": "function",
        "name": "something",
        "args": [{"name": "a", "node": "variable"}],
        "body": [{"from": [{"node": "literal", "value": 4}], "node": "return"}],
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="func_def")
    assert output == expected
