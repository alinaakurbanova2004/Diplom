from typing import List
from Diplom.src.parser.ast_nodes import ModuleNode, ProcedureNode, VariableNode
from Diplom.src.rules.basic_rule import BaseRule
from Diplom.src.rules.violation import Violation


class VariableMinLength(BaseRule):
    """
    Правило 4: Имена переменных не должны состоять из одного символа
    Исключение: счетчики циклов
    """

    def __init__(self):
        self.code = "VAR-04"
        self.name = "Минимальная длина имени"
        self.description = "Имена переменных должны"
        "быть длиннее одного символа (исключение: счетчики циклов)"
        self.severity = "WARNING"

        # Допустимые односимвольные имена для счетчиков
        self.loop_counters = ["i", "j", "k", "n", "m"]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # Проверяем переменные модуля
        for var in module.variables:
            if len(var.name) == 1 and var.name not in self.loop_counters:
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=var.range.start.line if var.range else 0,
                        column=var.range.start.column if var.range else 0,
                        message=f"Переменная '{var.name}' состоит"
                        f"из одного символа. Дайте ей осмысленное имя.",
                    )
                )

        # Проверяем локальные переменные в циклах
        for proc in module.procedures:
            for node in proc.body:
                if isinstance(node, VariableNode) and len(node.name) == 1:
                    # Проверяем, не является ли это счетчиком цикла
                    if not self._is_in_loop(node, proc):
                        violations.append(Violation(...))

        return violations

    def _is_in_loop(self, var_node: VariableNode, proc: ProcedureNode) -> bool:
        if not var_node.range:
            return False

        counter_names = ["i", "j", "k", "n", "m", "idx", "index", "счетчик"]

        if var_node.name.lower() not in counter_names:
            return False

        for node in proc.body:
            if self._is_loop_node(node):
                # Проверяем, находится ли переменная в области цикла
                if node.range and self._is_within_range(
                    var_node.range.start.line, node.range
                ):
                    return True

        return False
