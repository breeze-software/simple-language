import visitor


def test__zip_arithmetic__all_add():
    values = ["a", "b", "c", "d"]
    ops = ["+", "+", "+"]

    expected = {
        "left": "a",
        "node": "+",
        "right": {
            "left": "b",
            "node": "+",
            "right": {"left": "c", "node": "+", "right": "d"},
        },
    }

    output = visitor.zip_arithmetic(values[0], ops, values[1:])
    assert output == expected
