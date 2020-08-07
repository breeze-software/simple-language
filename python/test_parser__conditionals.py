import parser

import pre


def test__if_signature__basic():
    data = "if a:"
    expected = {"node": "if", "condition": {"name": "a", "node": "variable"}}

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="if_signature")
    assert output == expected


def test__if_block__basic():
    data = "if a:\n    a = b"
    expected = {
        "node": "if",
        "condition": {"name": "a", "node": "variable"},
        "body": [
            {
                "from": {"name": "b", "node": "variable"},
                "node": "assign",
                "to": {"name": "a", "node": "variable"},
            }
        ],
    }

    data = pre.insert_brackets(data)
    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="if_block")
    assert output == expected


def test__elseif_signature_basic():
    data = "else if a:"
    expected = {"node": "else if", "condition": {"name": "a", "node": "variable"}}

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="elseif_signature")
    assert output == expected


def test__elseif_block__basic():
    data = "else if a:\n    a = b"
    expected = {
        "node": "else if",
        "condition": {"name": "a", "node": "variable"},
        "body": [
            {
                "from": {"name": "b", "node": "variable"},
                "node": "assign",
                "to": {"name": "a", "node": "variable"},
            }
        ],
    }

    data = pre.insert_brackets(data)
    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="elseif_block")
    assert output == expected


def test__else_signature_basic():
    data = "else:"
    expected = {"node": "else"}

    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="else_signature")
    assert output == expected


def test__else_block__basic():
    data = "else:\n    a = b"
    expected = {
        "node": "else",
        "body": [
            {
                "from": {"name": "b", "node": "variable"},
                "node": "assign",
                "to": {"name": "a", "node": "variable"},
            }
        ],
    }

    data = pre.insert_brackets(data)
    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="else_block")
    assert output == expected


def test__if__just_if():
    data = "\n".join(["if a:", "    d = 1"])
    expected = {
        "node": "conditional",
        "if": {
            "condition": {"name": "a", "node": "variable"},
            "body": [
                {
                    "from": {"node": "literal", "value": 1},
                    "node": "assign",
                    "to": {"name": "d", "node": "variable"},
                }
            ],
        },
        "else if": [],
        "else": {"body": []},
    }

    data = pre.insert_brackets(data)
    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="if")
    assert output == expected


def test__if__with_else():
    data = "\n".join(["if a:", "    d = 1", "else:", "    d = 4"])
    expected = {
        "node": "conditional",
        "if": {
            "condition": {"name": "a", "node": "variable"},
            "body": [
                {
                    "from": {"node": "literal", "value": 1},
                    "node": "assign",
                    "to": {"name": "d", "node": "variable"},
                }
            ],
        },
        "else if": [],
        "else": {
            "body": [
                {
                    "from": {"node": "literal", "value": 4},
                    "node": "assign",
                    "to": {"name": "d", "node": "variable"},
                }
            ]
        },
    }

    data = pre.insert_brackets(data)
    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="if")
    assert output == expected


def test__if__with_elseif():
    data = "\n".join(
        ["if a:", "    d = 1", "else if b:", "    d = 2", "else:", "    d = 4"]
    )
    expected = {
        "node": "conditional",
        "if": {
            "condition": {"name": "a", "node": "variable"},
            "body": [
                {
                    "from": {"node": "literal", "value": 1},
                    "node": "assign",
                    "to": {"name": "d", "node": "variable"},
                }
            ],
        },
        "else if": [
            {
                "body": [
                    {
                        "from": {"node": "literal", "value": 2},
                        "node": "assign",
                        "to": {"name": "d", "node": "variable"},
                    }
                ],
                "condition": {"name": "b", "node": "variable"},
            }
        ],
        "else": {
            "body": [
                {
                    "from": {"node": "literal", "value": 4},
                    "node": "assign",
                    "to": {"name": "d", "node": "variable"},
                }
            ]
        },
    }

    data = pre.insert_brackets(data)
    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="if")
    assert output == expected


def test__if__multiple_elseif():
    data = "\n".join(
        [
            "if a:",
            "    d = 1",
            "else if b:",
            "    d = 2",
            "else if c:",
            "    d = 3",
            "else:",
            "    d = 4",
        ]
    )
    expected = {
        "node": "conditional",
        "if": {
            "condition": {"name": "a", "node": "variable"},
            "body": [
                {
                    "from": {"node": "literal", "value": 1},
                    "node": "assign",
                    "to": {"name": "d", "node": "variable"},
                }
            ],
        },
        "else if": [
            {
                "body": [
                    {
                        "from": {"node": "literal", "value": 2},
                        "node": "assign",
                        "to": {"name": "d", "node": "variable"},
                    }
                ],
                "condition": {"name": "b", "node": "variable"},
            },
            {
                "body": [
                    {
                        "from": {"node": "literal", "value": 3},
                        "node": "assign",
                        "to": {"name": "d", "node": "variable"},
                    }
                ],
                "condition": {"name": "c", "node": "variable"},
            },
        ],
        "else": {
            "body": [
                {
                    "from": {"node": "literal", "value": 4},
                    "node": "assign",
                    "to": {"name": "d", "node": "variable"},
                }
            ]
        },
    }

    data = pre.insert_brackets(data)
    grammar = parser.read_grammar()
    output = parser.parse(grammar, data, entry="if")
    assert output == expected
