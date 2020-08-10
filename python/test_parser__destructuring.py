import parser

import pre


def test__assign_to_variable():
    data = "abc"
    expected = {"name": "abc", "node": "variable"}

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="assign_target")
    assert output == expected


def test__assign_to_list():
    data = "[a, b, c]"
    expected = {
        "node": "target_list",
        "elements": [
            {"name": "a", "node": "variable"},
            {"name": "b", "node": "variable"},
            {"name": "c", "node": "variable"},
        ],
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="assign_target")
    assert output == expected


def test__assign_to_wildcard_list():
    data = "[a, b, **c]"
    expected = {
        "node": "target_list",
        "elements": [
            {"name": "a", "node": "variable"},
            {"name": "b", "node": "variable"},
            {"name": "c", "node": "wildcard"},
        ],
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="assign_target")
    assert output == expected


def test__assign_to_string():
    data = '''"aaa", bbb, "ccc"'''
    expected = {
        "node": "target_string",
        "elements": [
            {"node": "literal", "value": "aaa"},
            {"node": "variable", "name": "bbb"},
            {"node": "literal", "value": "ccc"},
        ],
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="assign_target")
    assert output == expected


def test__assign_to_string_complex():
    data = """aaa, "bbb", ccc, "ddd", eee"""
    expected = {
        "node": "target_string",
        "elements": [
            {"node": "variable", "name": "aaa"},
            {"node": "literal", "value": "bbb"},
            {"node": "variable", "name": "ccc"},
            {"node": "literal", "value": "ddd"},
            {"node": "variable", "name": "eee"},
        ],
    }

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="assign_target")
    assert output == expected
