def scribe_variable(tree):
    yield tree["name"]


def scribe_literal(tree):
    yield str(tree["value"])


def scribe_return(tree, indent):
    yield " " * indent
    yield "return"
    yield " "
    yield from scribe_helper(tree["from"], indent)
    yield "\n"


def scribe_assign(tree, indent):
    yield " " * indent
    yield "local"
    yield " "
    yield from scribe_helper(tree["to"], indent)
    yield " "
    yield "="
    yield " "
    yield from scribe_helper(tree["from"], indent)
    yield "\n"


def scribe_conditional(tree, indent):
    yield " " * indent
    yield "if"
    yield " "
    yield from scribe_helper(tree["if"]["condition"], indent)
    yield " "
    yield "then"
    yield "\n"
    yield from scribe_helper(tree["if"]["body"], indent + 4)

    for branch in tree["else if"]:
        yield " " * indent
        yield "elseif"
        yield " "
        yield from scribe_helper(branch["condition"], indent)
        yield " "
        yield "then"
        yield "\n"
        yield from scribe_helper(branch["body"], indent + 4)

    if tree["else"]["body"] != []:
        yield " " * indent
        yield "else"
        yield "\n"
        yield from scribe_helper(tree["else"]["body"], indent + 4)

    yield " " * indent
    yield "end"
    yield "\n"


def scribe_for(tree, indent):
    yield " " * indent
    yield "for"
    yield " "
    yield from scribe_helper(tree["var"], indent)
    yield " "
    yield "in"
    yield " "
    yield from scribe_helper(tree["iterator"], indent)
    yield " "
    yield "do"
    yield "\n"

    yield from scribe_helper(tree["body"], indent + 4)

    yield " " * indent
    yield "end"
    yield "\n"


def scribe_function(tree, indent):
    yield " " * indent
    yield "function"
    yield " "
    yield tree["name"]
    yield "("
    yield ", ".join("".join(scribe_helper(arg, indent=0)) for arg in tree["args"])
    yield ") do\n"

    yield from scribe_helper(tree["body"], indent + 4)

    yield " " * indent
    yield "end"
    yield "\n\n\n"


def scribe_helper(tree, indent):
    if isinstance(tree, list):
        for e in tree:
            yield from scribe_helper(e, indent)
        return

    if tree["node"] == "function":
        yield from scribe_function(tree, indent)
        return

    if tree["node"] == "conditional":
        yield from scribe_conditional(tree, indent)
        return

    if tree["node"] == "for":
        yield from scribe_for(tree, indent)
        return

    if tree["node"] == "return":
        yield from scribe_return(tree, indent)
        return

    if tree["node"] == "assign":
        yield from scribe_assign(tree, indent)
        return

    if tree["node"] == "variable":
        yield from scribe_variable(tree)
        return

    if tree["node"] == "literal":
        yield from scribe_literal(tree)
        return

    yield f"writer.py ERROR: {tree['node']}\n"


def sort_imports(imports):
    # TODO: will eventually be a more sophisticated scheme, like isort
    return sorted(imports)


def scribe(tree):
    out = []

    for i in sort_imports(tree["imports"]):
        out.append(f'local {i} = require "{i}"\n')
    out.append("\n\n")

    for v in tree["functions"].values():
        out.extend(scribe_helper(v, indent=0))

    out = "".join(out)
    out = out.strip("\n") + "\n"
    return out
