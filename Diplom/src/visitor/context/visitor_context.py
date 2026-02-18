from Diplom.src.parser.ast_nodes import FunctionNode, WhileLoopNode
from Diplom.src.visitor.base_visitor import ASTVisitor


class VisitorContext:
    """Контекст для передачи данных между Visitor'ами"""

    def __init__(self):
        self.module_name = ""
        self.current_function = None
        self.current_procedure = None
        self.in_loop = False
        self.in_condition = False
        self.scope_stack = ["global"]
        self.data = {}  # для пользовательских данных

    def enter_scope(self, name: str):
        self.scope_stack.append(name)

    def exit_scope(self):
        self.scope_stack.pop()

    def current_scope(self) -> str:
        return ".".join(self.scope_stack)

    def set(self, key: str, value):
        self.data[key] = value

    def get(self, key: str, default=None):
        return self.data.get(key, default)


class ContextAwareVisitor(ASTVisitor):
    """Базовый класс для Visitor'ов с контекстом"""

    def __init__(self, context: VisitorContext = None):
        self.context = context or VisitorContext()

    def visit_function(self, node: FunctionNode):
        old_function = self.context.current_function
        self.context.current_function = node
        self.context.enter_scope(f"func:{node.name}")
        super().visit_function(node)
        self.context.exit_scope()
        self.context.current_function = old_function

    def visit_while_loop(self, node: WhileLoopNode):
        old_in_loop = self.context.in_loop
        self.context.in_loop = True
        super().visit_while_loop(node)
        self.context.in_loop = old_in_loop
