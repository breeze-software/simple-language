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


def scribe_if(tree, indent):
    yield " " * indent
    yield "if"
    yield " "
    yield from scribe_helper(tree["condition"], indent)
    yield " "
    yield "then"
    yield "\n"

    yield from scribe_helper(tree["body"], indent + 4)

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
    yield tree["name"]["name"]
    yield "("
    # for arg in tree["args"]:
    #    yield from scribe_helper(arg)
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

    if tree["node"] == "if":
        yield from scribe_if(tree, indent)
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

    yield f"ERROR: {tree['node']}\n"


def scribe(tree):
    out = list(scribe_helper(tree, indent=0))
    return "".join(out)
