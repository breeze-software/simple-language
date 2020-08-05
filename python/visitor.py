from parsimonious.nodes import NodeVisitor


class SourceVisitor(NodeVisitor):
    def visit_source(self, node, visited_children):
        v = visited_children
        return [v[1][0][0]] + [e[1] for e in v[1][0][1]]

    def visit_func_def(self, node, visited_children):
        return {
            "node": "function",
            "name": visited_children[2],
            "args": visited_children[5],
            "body": visited_children[11],
        }

    def visit_line(self, node, visited_children):
        return visited_children[0]

    def visit_return(self, node, visited_children):
        return {"node": "return", "from": visited_children[2][0]}

    def visit_assign(self, node, visited_children):
        return {
            "node": "assign",
            "to": visited_children[0],
            "from": visited_children[4][0],
        }

    def visit_for(self, node, visited_children):
        return {
            "node": "for",
            "var": visited_children[2],
            "iterator": visited_children[6],
            "body": visited_children[12],
        }

    def visit_list_contents(self, node, visited_children):
        """ Returns the overall output. """
        v = visited_children
        return [v[0][0]] + v[0][1]

    def visit_var(self, node, visited_children):
        return {"node": "variable", "name": node.text}

    def visit_int_literal(self, node, visited_children):
        return {"node": "literal", "value": int(node.text)}

    def visit_comma(self, node, visited_children):
        return node.text

    def visit_whitespace(self, node, visited_children):
        return node.text

    def visit_tail_arg(self, node, visited_children):
        return visited_children[2][0]

    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        if visited_children:
            return visited_children
        return node
