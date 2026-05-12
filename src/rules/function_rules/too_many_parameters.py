from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class TooManyParameters(BaseRule):
    """
    Правило FUN-04: Проверка количества параметров в функциях/процедурах

    Ограничения:
    - Не более 7 параметров всего
    - Не более 3 параметров со значениями по умолчанию
    """

    def __init__(self):
        self.code = "FUN-04"
        self.name = "Слишком много параметров"
        self.description = (
            "Функция/процедура должна иметь не более 7 параметров, "
            "из них не более 3 со значениями по умолчанию."
        )
        self.severity = "WARNING"
        self.max_total_params = 7
        self.max_default_params = 3

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # Проверяем функции
        for func in module.functions:
            violations.extend(self._check_parameters(func, module))

        # Проверяем процедуры
        for proc in module.procedures:
            violations.extend(self._check_parameters(proc, module))

        return violations

    def _check_parameters(self, node, module: ModuleNode) -> List[Violation]:
        """Проверяет параметры одного узла (функции/процедуры)"""
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
            # Определяем тип узла
            if hasattr(node, 'is_procedure') and node.is_procedure:
                node_type = "Процедура"
            elif node.__class__.__name__ == "ProcedureNode":
                node_type = "Процедура"
            else:
                node_type = "Функция"
        
            # Добавляем точку в конце
            message_text = f"{node_type} '{node.name}': " + "; ".join(messages)
            if not message_text.endswith('.'):
                message_text += "."
        
            violations.append(self._create_violation(
                node, module,
                message_text
            ))
    
        return violations

    def _are_defaults_at_end(self, parameters: list) -> bool:
        """Проверяет, что все параметры
        с умолчаниями находятся в конце списка"""
        found_default = False

        for param in parameters:
            if param.has_default_value:
                found_default = True
            else:
                # Если нашли параметр без умолчания ПОСЛЕ того,
                # как уже были параметры с умолчанием - это ошибка
                if found_default:
                    return False

        return True

    def _create_violation(self, node, module: ModuleNode, message: str
                          ) -> Violation:
        return Violation(
            rule_code=self.code,
            rule_name=self.name,
            severity=self.severity,
            module_name=module.name,
            line=node.range.start.line if node.range else 0,
            column=node.range.start.column if node.range else 0,
            message=message
        )
