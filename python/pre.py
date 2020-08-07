# TODO: need to not insert brackets inside multi-line strings or expressions or whatever


def split_indent(source):
    return [(len(line) - len(line.lstrip(" ")), line.lstrip(" ")) for line in source]


def insert_brackets_helper(source):
    source = source.strip("\n")
    source = source.replace("\t", " " * 4)
    source = source.split("\n")

    stack = [0]
    out = []
    for i, s in split_indent(source):
        if i > stack[-1]:
            yield "{"
            stack.append(i)
        else:
            while i < stack[-1]:
                yield "}"
                stack.pop()

        yield s

    yield from ["}"] * len(stack[1:])
    yield "\n"


def insert_brackets(source):
    if "\n" not in source and not (source.startswith(" ") or source.startswith("\t")):
        return source
    return "\n".join(insert_brackets_helper(source))
