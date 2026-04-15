from typing import List
from src.parser.ast_nodes import ModuleNode, AssignmentNode, IfStatementNode, WhileLoopNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class FlagVariableNames(BaseRule):
    """
    Правило VAR-05: Переменные-флаги должны называться по истинному значению
    Пример: ЕстьОшибки, ЭтоТоварТара, НужноОбновить
    """

    def __init__(self):
        self.code = "VAR-05"
        self.name = "Имена для переменных-флагов"
        self.description = (
            "Переменные-флаги должны называться по истинному значению "
            "(ЕстьОшибки, ЭтоТоварТара, НужноОбновить)"
        )
        self.severity = "INFO"

        # Хорошие префиксы для флагов
        self.good_prefixes = [
            "Есть", "Нет", "Можно", "Нельзя", "Нужно",
            "Требуется", "Разрешено", "Запрещено",
            "ЭтоАктивно", "ЭтоВыбрано", "ЭтоЗавершено",
            "Признак", "Флаг", "Состояние"
        ]

        # Плохие имена для флагов (только если переменная ТОЧНО флаг)
        self.bad_flag_names = [
            "флаг", "признак", "состояние", "режим", "тип",
            "value", "flag", "status", "mode", "type"
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # Проверяем переменные в модуле, процедурах и функциях
        for var, context_name, context_type in self._iter_variables(module):
            if self._is_used_as_boolean(var, module):
                if not self._is_good_flag_name(var.name):
                    line = var.range.start.line if var.range else 0
                    col = var.range.start.column if var.range else 0
                    
                    context_info = f"в {context_type} '{context_name}'" if context_name else ""
                    violations.append(
                        Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=line,
                            column=col,
                            message=f"Переменная-флаг '{var.name}' {context_info} должна называться по истинному значению (например: ЕстьОшибки, ЭтоТоварТара)",
                        )
                    )

        return violations

    def _iter_variables(self, module):
        """Итерирует по всем переменным в модуле"""
        # Глобальные переменные
        for var in module.variables:
            yield var, None, None
        
        # Переменные в процедурах
        for proc in module.procedures:
            for var in proc.local_vars:
                yield var, proc.name, "процедуре"
        
        # Переменные в функциях
        for func in module.functions:
            for var in func.local_vars:
                yield var, func.name, "функции"

    def _is_used_as_boolean(self, var, module) -> bool:
        """
        🔥 КЛЮЧЕВОЙ МЕТОД: проверяет, используется ли переменная как булева (флаг)
        """
        var_name = var.name
        
        # Проверяем все процедуры и функции
        for proc in module.procedures:
            if self._check_boolean_usage_in_body(var_name, proc.body):
                return True
        
        for func in module.functions:
            if self._check_boolean_usage_in_body(var_name, func.body):
                return True
        
        # Проверяем тело модуля (глобальный код)
        if hasattr(module, 'body'):
            if self._check_boolean_usage_in_body(var_name, module.body):
                return True
        
        return False

    def _check_boolean_usage_in_body(self, var_name: str, body: List) -> bool:
        """Проверяет, используется ли переменная как булева в теле"""
        for node in body:
            # 1. Проверка присваивания Истина/Ложь
            if isinstance(node, AssignmentNode):
                if self._is_assigned_boolean(var_name, node):
                    return True
            
            # 2. Проверка использования в условии (Если, ИначеЕсли, Пока)
            if self._is_in_condition(var_name, node):
                return True
            
            # 3. Рекурсивный обход вложенных конструкций
            if hasattr(node, 'body') and isinstance(node.body, list):
                if self._check_boolean_usage_in_body(var_name, node.body):
                    return True
            
            if hasattr(node, 'then_branch') and isinstance(node.then_branch, list):
                if self._check_boolean_usage_in_body(var_name, node.then_branch):
                    return True
            
            if hasattr(node, 'else_branch') and isinstance(node.else_branch, list):
                if self._check_boolean_usage_in_body(var_name, node.else_branch):
                    return True
        
        return False

    def _is_assigned_boolean(self, var_name: str, node: AssignmentNode) -> bool:
        """Проверяет, присваивается ли переменной булево значение (Истина/Ложь)"""
        if hasattr(node.left, 'name') and node.left.name == var_name:
            # Проверяем правую часть
            if hasattr(node.right, 'literal_type') and node.right.literal_type == 'boolean':
                return True
            # Если справа переменная, которая может быть булевой - не проверяем
        return False

    def _is_in_condition(self, var_name: str, node) -> bool:
        """Проверяет, используется ли переменная в условии"""
        # Проверка условия в IfStatementNode
        if isinstance(node, IfStatementNode) and hasattr(node, 'condition'):
            if self._var_in_expression(var_name, node.condition):
                return True
        
        # Проверка условия в WhileLoopNode
        if isinstance(node, WhileLoopNode) and hasattr(node, 'condition'):
            if self._var_in_expression(var_name, node.condition):
                return True
        
        return False

    def _var_in_expression(self, var_name: str, expr) -> bool:
        """Проверяет, присутствует ли переменная в выражении"""
        if expr is None:
            return False
        
        # Если это переменная
        if hasattr(expr, 'name') and expr.name == var_name:
            return True
        
        # Если это бинарная операция
        if hasattr(expr, 'left') and hasattr(expr, 'right'):
            return (self._var_in_expression(var_name, expr.left) or 
                    self._var_in_expression(var_name, expr.right))
        
        return False

    def _is_good_flag_name(self, name: str) -> bool:
        """Проверяет, хорошее ли имя для флага"""
        for prefix in self.good_prefixes:
            if name.startswith(prefix):
                return True
        return False