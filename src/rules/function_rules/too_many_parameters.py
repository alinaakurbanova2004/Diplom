from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class TooManyParameters(BaseRule):
    """
    Правило FUN-04: Проверка количества параметров в функциях/процедурах
    """

    def __init__(self):
        self.code = "FUN-04"
        self.name = "Слишком много параметров"
        self.max_total_params = 7   # значение по умолчанию
        self.max_default_params = 3 # значение по умолчанию
        self._update_description()
        self.severity = "WARNING"

    def _update_description(self):
        """Обновляет описание с текущими значениями параметров"""
        self.description = (
            f"Функция/процедура должна иметь не более {self.max_total_params} параметров, "
            f"из них не более {self.max_default_params} со значениями по умолчанию."
        )

    def set_parameter(self, name: str, value):
        """Устанавливает параметр и обновляет описание"""
        if name == 'max_total_params':
            self.max_total_params = int(value)
        elif name == 'max_default_params':
            self.max_default_params = int(value)
        self._update_description()

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        for func in module.functions:
            violations.extend(self._check_parameters(func, module))

        for proc in module.procedures:
            violations.extend(self._check_parameters(proc, module))

        return violations

    def _check_parameters(self, node, module: ModuleNode) -> List[Violation]:
        violations = []
        total_params = len(node.parameters)
        default_params = sum(1 for p in node.parameters if p.has_default_value)
        messages = []

        if total_params > self.max_total_params:
            messages.append(f"всего параметров {total_params} (макс. {self.max_total_params})")

        if default_params > self.max_default_params:
            messages.append(f"параметров с умолчанием {default_params} (макс. {self.max_default_params})")

        if not self._are_defaults_at_end(node.parameters):
            messages.append("параметры с умолчанием не в конце")

        if messages:
            node_type = "Процедура" if node.__class__.__name__ == "ProcedureNode" else "Функция"
            message_text = f"{node_type} '{node.name}': " + "; ".join(messages) + "."
            
            violations.append(Violation(
                rule_code=self.code,
                rule_name=self.name,
                severity=self.severity,
                module_name=module.name,
                line=node.range.start.line if node.range else 0,
                column=node.range.start.column if node.range else 0,
                message=message_text
            ))

        return violations

    def _are_defaults_at_end(self, parameters: list) -> bool:
        found_default = False
        for param in parameters:
            if param.has_default_value:
                found_default = True
            else:
                if found_default:
                    return False
        return True