# TODO: need to not insert brackets inside multi-line strings or expressions or whatever
def insert_brackets(code):
    code = [""] + code.split("\n") + ["", ""]

    out = []
    for a, b in zip(code, code[1:]):
        a = a.replace("\t", "    ")
        b = b.replace("\t", "    ")
        indent_a = len(a) - len(a.lstrip(" "))
        indent_b = len(b) - len(b.lstrip(" "))

        out.append(a.lstrip(" "))
        while indent_a < indent_b:
            out.append("{")
            indent_b -= 4
        while indent_b < indent_a:
            out.append("}")
            indent_a -= 4

    return ("\n".join(out)).lstrip("\n")
