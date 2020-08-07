from parsimonious.nodes import NodeVisitor


class SourceVisitor(NodeVisitor):
    def visit_source(self, node, visited_children):
        v = visited_children
        return [v[1][0][0]] + [e[1] for e in v[1][0][1]]

    def visit_func_def(self, node, visited_children):
        out = visited_children[0]
        out["body"] = visited_children[4]
        return out

    def visit_func_signature(self, node, visited_children):
        return {
            "node": "function",
            "name": visited_children[2],
            "args": visited_children[5],
        }

    def visit_body(self, node, visited_children):
        return visited_children[0]

    def visit_block(self, _, visited_children):
        return visited_children[0]

    def visit_line(self, node, visited_children):
        return visited_children[0]

    def visit_stmt_return(self, node, visited_children):
        return {"node": "return", "from": visited_children[2][0]}

    def visit_stmt_assign(self, node, visited_children):
        return {
            "node": "assign",
            "to": visited_children[0],
            "from": visited_children[4][0][0],
        }

    def visit_for(self, node, visited_children):
        out = visited_children[0]
        out["body"] = visited_children[4]
        return out

    def visit_for_signature(self, node, visited_children):
        return {
            "node": "for",
            "var": visited_children[2],
            "iterator": visited_children[6],
        }

    def visit_if(self, node, visited_children):
        out = {
            "node": "conditional",
            "if": visited_children[0],
            "else if": [],
            "else": {"body": []},
        }
        out["if"].pop("node")

        children = []
        for e in visited_children[1:]:
            if isinstance(e, list):
                children.extend(e)

        for e in children:
            node = e.pop("node")
            if node == "else if":
                out["else if"].append(e)
            elif node == "else":
                out["else"] = e
        return out

    def visit_if_block(self, node, visited_children):
        out = visited_children[0]
        out["body"] = visited_children[4]
        return out

    def visit_if_signature(self, node, visited_children):
        return {"node": "if", "condition": visited_children[2][0][0]}

    def visit_elseif_block(self, node, visited_children):
        out = visited_children[0]
        out["body"] = visited_children[4]
        return out

    def visit_elseif_signature(self, node, visited_children):
        return {"node": "else if", "condition": visited_children[2][0][0]}

    def visit_else_block(self, node, visited_children):
        out = visited_children[0]
        out["body"] = visited_children[4]
        return out

    def visit_else_signature(self, node, visited_children):
        return {"node": "else"}

    def visit_func_args(self, node, visited_children):
        """ Returns the overall output. """
        v = visited_children
        if len(v) == 0:
            return []
        elif len(v[0]) == 1:
            return [v[0][0]]
        return [v[0][0]] + [e[2] for e in v[0][1]]

    def visit_list_contents(self, node, visited_children):
        """ Returns the overall output. """
        v = visited_children
        return [v[0][0]] + v[0][1]

    def visit_var(self, node, visited_children):
        return {"node": "variable", "name": node.text}

    def visit_int_literal(self, node, visited_children):
        return {"node": "literal", "value": int(node.text)}

    def visit_expr_add_sub(self, node, visited_children):
        return {
            "node": visited_children[2][0],
            "left": visited_children[0],
            "right": visited_children[4],
        }

    def visit_add(self, node, visited_children):
        return "+"

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
