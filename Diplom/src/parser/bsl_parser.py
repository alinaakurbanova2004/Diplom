import subprocess
import json
import tempfile
import os
from pathlib import Path
from .ast_nodes import (
    ModuleNode,
    FunctionNode,
    ProcedureNode,
    VariableNode,
    ParameterNode,
    ReturnStatementNode,
    IfStatementNode,
    WhileLoopNode,
    BinaryOperationNode,
    LiteralNode,
    ASTNode,
    NodeType,
)


class BSLParser:
    """Парсер для языка 1С"""

    def __init__(self, jar_path: str):
        self.jar_path = Path(jar_path)
        if not self.jar_path.exists():
            raise FileNotFoundError(f"JAR не найден: {jar_path}")

    def parse_string(self, code: str, 
                     module_name: str = "module.bsl") -> ModuleNode:
   
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".bsl", encoding="utf-8", delete=False
        ) as tmp:
            tmp.write(code)
            tmp_path = tmp.name

        try:
            # Запуск BSL Language Server
            cmd = [
                "java",
                "-jar",
                str(self.jar_path),
                "analyze",
                "--format",
                "json",
                tmp_path,
            ]

            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=30
                )

            # Парсинг JSON ответ
            if result.returncode == 0:
                ast_json = json.loads(result.stdout)
                return self._convert_to_ast(ast_json, module_name)
            else:
                raise Exception(f"Ошибка BSL LS: {result.stderr}")

        finally:
            # Удаление временного файла
            os.unlink(tmp_path)

    def parse_file(self, file_path: str) -> ModuleNode:
        """Парсит файл .bsl"""
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        return self.parse_string(code, file_path)

    def _convert_to_ast(self, bsl_json: dict, name: str) -> ModuleNode:
        """Преобразует JSON от BSL LS в наше AST"""
        module = ModuleNode(name)

        try:
            if not bsl_json or "module" not in bsl_json:
                print(f"Предупреждение: пустой JSON для модуля {name}")
                return module

            module_data = bsl_json["module"]

            # 1. ПАРСИМ ПЕРЕМЕННЫЕ
            if "variables" in module_data:
                for var_data in module_data["variables"]:
                    var = VariableNode(
                        name=var_data.get("name", ""),
                        is_export=var_data.get("export", False),
                    )
                    module.variables.append(var)

            # 2. ПАРСИМ ФУНКЦИИ
            if "functions" in module_data:
                for func_data in module_data["functions"]:
                    func = self._parse_function(func_data)
                    module.functions.append(func)

            # 3. ПАРСИМ ПРОЦЕДУРЫ
            if "procedures" in module_data:
                for proc_data in module_data["procedures"]:
                    proc = self._parse_procedure(proc_data)
                    module.procedures.append(proc)

            print(f"Распарсен модуль {name}:")
            print(f"   - Переменных: {len(module.variables)}")
            print(f"   - Функций: {len(module.functions)}")
            print(f"   - Процедур: {len(module.procedures)}")

        except Exception as e:
            print(f"Ошибка при парсинге AST: {e}")
            # Возвращаем хотя бы пустой модуль
            return ModuleNode(name)

        return module

    def _parse_function(self, func_data: dict) -> FunctionNode:
        """Парсит функцию из JSON"""
        func = FunctionNode(func_data.get("name", "unnamed"))

        # Парсим параметры
        if "parameters" in func_data:
            for param_data in func_data["parameters"]:
                param = ParameterNode(
                    name=param_data.get("name", ""),
                    by_value=param_data.get("byValue", False),
                )
                func.parameters.append(param)

        # Парсим тело функции
        if "body" in func_data:
            func.body = self._parse_statements(func_data["body"])

        return func

    def _parse_procedure(self, proc_data: dict) -> ProcedureNode:
        """Парсит процедуру из JSON"""
        proc = ProcedureNode(proc_data.get("name", "unnamed"))

        # Парсим параметры
        if "parameters" in proc_data:
            for param_data in proc_data["parameters"]:
                param = ParameterNode(
                    name=param_data.get("name", ""),
                    by_value=param_data.get("byValue", False),
                )
                proc.parameters.append(param)

        # Парсим тело процедуры
        if "body" in proc_data:
            proc.body = self._parse_statements(proc_data["body"])

        return proc

    def _parse_statements(self, statements_data: list) -> list:
        """Парсит список операторов"""
        statements = []

        for stmt_data in statements_data:
            stmt_type = stmt_data.get("type", "")

            if stmt_type == "returnStatement":
                stmt = self._parse_return_statement(stmt_data)
                statements.append(stmt)
            elif stmt_type == "ifStatement":
                stmt = self._parse_if_statement(stmt_data)
                statements.append(stmt)
            elif stmt_type == "whileStatement":
                stmt = self._parse_while_statement(stmt_data)
                statements.append(stmt)

        return statements

    def _parse_return_statement(self, stmt_data: dict) -> ReturnStatementNode:
        """Парсит оператор Возврат"""
        stmt = ReturnStatementNode()

        # Парсим выражение, если оно есть
        if "expression" in stmt_data:
            stmt.expression = self._parse_expression(stmt_data["expression"])

        return stmt

    def _parse_if_statement(self, stmt_data: dict) -> IfStatementNode:
        """Парсит оператор Если"""
        stmt = IfStatementNode()

        # Парсим условие
        if "condition" in stmt_data:
            stmt.condition = self._parse_expression(stmt_data["condition"])

        # Парсим ветку Тогда
        if "thenStatements" in stmt_data:
            stmt.then_branch = self._parse_statements(
                stmt_data["thenStatements"]
                )

        # Парсим ветки ИначеЕсли
        if "elseIfClauses" in stmt_data:
            for clause in stmt_data["elseIfClauses"]:
                condition = self._parse_expression(clause["condition"])
                statements = self._parse_statements(clause["statements"])
                stmt.elif_branches.append((condition, statements))

        # Парсим ветку Иначе
        if "elseStatements" in stmt_data:
            stmt.else_branch = self._parse_statements(
                stmt_data["elseStatements"])

        return stmt

    def _parse_while_statement(self, stmt_data: dict) -> WhileLoopNode:
        """Парсит цикл Пока"""
        stmt = WhileLoopNode()

        # Парсим условие
        if "condition" in stmt_data:
            stmt.condition = self._parse_expression(stmt_data["condition"])

        # Парсим тело цикла
        if "statements" in stmt_data:
            stmt.body = self._parse_statements(stmt_data["statements"])

        return stmt

    def _parse_expression(self, expr_data: dict) -> ASTNode:
    
        """Парсит выражение (рекурсивно!)"""
    
        expr_type = expr_data.get("type", "")

        if expr_type == "literal":
            # Литерал (число, строка, булево)
            return LiteralNode(
                value=expr_data.get("value"),
                literal_type=expr_data.get("literalType", "unknown"),
            )

        elif expr_type == "variable":
            # Переменная
            return VariableNode(
                name=expr_data.get("name", ""), is_export=expr_data.get(
                    "export", False)
            )

        elif expr_type == "binaryOperation":
            # Бинарная операция (a + b, a > b, ...)
            left = self._parse_expression(expr_data["left"])
            right = self._parse_expression(expr_data["right"])
            operator = expr_data.get("operator", "")
            return BinaryOperationNode(operator, left, right)
   
        else:
            print(f"Неизвестный тип выражения: {expr_type}")
            return ASTNode(NodeType.EXPRESSION)
