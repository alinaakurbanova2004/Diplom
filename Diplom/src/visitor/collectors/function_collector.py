from typing import List, Dict, Any
from src.visitor.base_visitor import ASTVisitor
from src.parser.ast_nodes import (
    ModuleNode,
    FunctionNode,
    ProcedureNode,
    ParameterNode,
    ReturnStatementNode,
)


class FunctionCollector(ASTVisitor):
    """
    Собирает информацию о всех функциях и процедурах в модуле
    """

    def __init__(self):
        self.functions: List[Dict[str, Any]] = []  # список функций
        self.procedures: List[Dict[str, Any]] = []  # список процедур
        self.current_function = None
        self.current_procedure = None
        self.call_graph: Dict[str, List[str]] = {}  # граф вызовов

    def visit_module(self, node: ModuleNode):
        """Начинаем сбор с модуля"""
        self.functions = []
        self.procedures = []
        self.call_graph = {}
        super().visit_module(node)

    def visit_function(self, node: FunctionNode):
        """Собирает информацию о функции"""
        func_info = {
            "name": node.name,
            "line": node.range.start.line if node.range else 0,
            "parameters": [],
            "return_statements": [],
            "calls": [],  # какие функции/процедуры вызывает
            "length": self._calculate_length(node),
            "has_return": False,
        }

        # Сохраняем текущую функцию для анализа вызовов
        self.current_function = node.name
        self.functions.append(func_info)

        # Обходим параметры
        for param in node.parameters:
            param.accept(self)

        # Обходим тело функции
        for stmt in node.body:
            stmt.accept(self)

        self.current_function = None

    def visit_procedure(self, node: ProcedureNode):
        """Собирает информацию о процедуре"""
        proc_info = {
            "name": node.name,
            "line": node.range.start.line if node.range else 0,
            "parameters": [],
            "calls": [],
            "length": self._calculate_length(node),
        }

        self.current_procedure = node.name
        self.procedures.append(proc_info)

        # Обходим параметры
        for param in node.parameters:
            param.accept(self)

        # Обходим тело процедуры
        for stmt in node.body:
            stmt.accept(self)

        self.current_procedure = None

    def visit_parameter(self, node: ParameterNode):
        """Собирает информацию о параметре"""
        param_info = {
            "name": node.name,
            "by_value": node.by_value,
            "has_default": node.has_default_value,
        }

        # Добавляем параметр к текущей функции или процедуре
        if self.current_function:
            for func in self.functions:
                if func["name"] == self.current_function:
                    func["parameters"].append(param_info)
                    break
        elif self.current_procedure:
            for proc in self.procedures:
                if proc["name"] == self.current_procedure:
                    proc["parameters"].append(param_info)
                    break

    def visit_return_statement(self, node: ReturnStatementNode):
        """Отмечает наличие return в функции"""
        if self.current_function:
            for func in self.functions:
                if func["name"] == self.current_function:
                    func["has_return"] = True
                    if node.expression:
                        # Здесь можно анализировать выражение return'а
                        func["return_statements"].append(
                            {
                                "line": node.range.start.line
                                if node.range else 0,
                                "has_value": True,
                            }
                        )
                    else:
                        func["return_statements"].append(
                            {
                                "line": node.range.start.line
                                if node.range else 0,
                                "has_value": False,
                            }
                        )
                    break

    def visit_function_call(self, node):
        """Регистрирует вызов функции (нужен соответствующий узел в AST)"""
        caller = self.current_function or self.current_procedure
        if caller and hasattr(node, "name"):
            if caller not in self.call_graph:
                self.call_graph[caller] = []
            if node.name not in self.call_graph[caller]:
                self.call_graph[caller].append(node.name)

    def _calculate_length(self, node) -> int:
        """Вычисляет длину функции/процедуры в строках"""
        if node.range:
            return node.range.end.line - node.range.start.line
        return 0

    def get_statistics(self) -> Dict[str, Any]:
        """Возвращает статистику по функциям и процедурам"""
        return {
            "total_functions": len(self.functions),
            "total_procedures": len(self.procedures),
            "functions_with_return": sum(1 for f in self.functions
                                         if f["has_return"]),
            "functions_without_return": sum(
                1 for f in self.functions if not f["has_return"]
            ),
            "avg_function_length": self._average([f["length"] for
                                                  f in self.functions]),
            "avg_procedure_length": self._average(
                [p["length"] for p in self.procedures]
            ),
            "most_called": self._get_most_called(),
            "call_graph": self.call_graph,
        }

    def _average(self, numbers: List[int]) -> float:
        """Вычисляет среднее арифметическое"""
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    def _get_most_called(self) -> Dict[str, int]:
        """Определяет самые вызываемые функции/процедуры"""
        call_count = {}
        for caller, callees in self.call_graph.items():
            for callee in callees:
                call_count[callee] = call_count.get(callee, 0) + 1
        return dict(
            sorted(call_count.items(), key=lambda x: x[1], reverse=True)[:5])

    def find_unused_functions(self) -> List[str]:
        """Находит функции, которые нигде не вызываются"""
        all_functions = [f["name"] for f in self.functions] + [
            p["name"] for p in self.procedures
        ]
        called_functions = set()

        for callees in self.call_graph.values():
            called_functions.update(callees)

        unused = [f for f in all_functions if f not in called_functions]
        return unused

    def get_recursive_functions(self) -> List[str]:
        """Находит рекурсивные функции (вызывающие сами себя)"""
        recursive = []
        for caller, callees in self.call_graph.items():
            if caller in callees:
                recursive.append(caller)
        return recursive
