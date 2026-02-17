from typing import List
from Diplom.src.parser.ast_nodes import ModuleNode
from Diplom.src.rules.basic_rule import BaseRule
from Diplom.src.rules.violation import Violation


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
            "из них не более 3 со значениями по умолчанию"
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

        if total_params > self.max_total_params:
            violations.append(
                self._create_violation(
                    node=node,
                    module=module,
                    message=(
                        f"{node.__class__.__name__} '{node.name}' имеет "
                        f"{total_params} параметров. "
                        f"Рекомендуется не более {self.max_total_params}"
                    ),
                )
            )

        elif default_params > self.max_default_params:
            violations.append(
                self._create_violation(
                    node=node,
                    module=module,
                    message=(
                        f"{node.__class__.__name__} '{node.name}' имеет "
                        f"{default_params} параметров"
                        f"со значениями по умолчанию. "
                        f"Рекомендуется не более {self.max_default_params}"
                    ),
                )
            )

        if not self._are_defaults_at_end(node.parameters):
            violations.append(
                self._create_violation(
                    node=node,
                    module=module,
                    message=(
                        f"{node.__class__.__name__} '{node.name}': "
                        f"параметры со значениями по умолчанию должны быть "
                        f"в конце списка параметров"
                    ),
                )
            )

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
            message=message,
        )
