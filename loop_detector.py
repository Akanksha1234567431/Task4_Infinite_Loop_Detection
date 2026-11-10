import ast

class InfiniteLoopDetector(ast.NodeVisitor):

    def __init__(self):
        self.results = []

    def visit_While(self, node):
        condition = ast.unparse(node.test)

        if isinstance(node.test, ast.Constant) and node.test.value is True:
            self.results.append({
                "type": "WHILE LOOP",
                "condition": condition,
                "status": "POSSIBLE INFINITE LOOP",
                "line": node.lineno
            })
        else:
            self.results.append({
                "type": "WHILE LOOP",
                "condition": condition,
                "status": "CONDITION-DEPENDENT LOOP",
                "line": node.lineno
            })

        self.generic_visit(node)

    def visit_For(self, node):
        self.results.append({
            "type": "FOR LOOP",
            "condition": ast.unparse(node.iter),
            "status": "ITERABLE-BASED LOOP",
            "line": node.lineno
        })

        self.generic_visit(node)


def analyze_code(code):
    try:
        tree = ast.parse(code)
        detector = InfiniteLoopDetector()
        detector.visit(tree)
        return detector.results

    except SyntaxError as error:
        return [{
            "type": "ERROR",
            "condition": str(error),
            "status": "INVALID PYTHON CODE",
            "line": error.lineno
        }]