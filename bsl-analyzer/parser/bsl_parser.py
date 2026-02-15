import subprocess
import json
import tempfile
import os
from pathlib import Path
from .ast_nodes import ModuleNode


class BSLParser:
    """Парсер для языка 1С"""

    def __init__(self, jar_path: str):
        self.jar_path = Path(jar_path)
        if not self.jar_path.exists():
            raise FileNotFoundError(f"JAR не найден: {jar_path}")

    def parse_string(
            self, code: str, module_name: str = "module.bsl") -> ModuleNode:
        """
        Парсит строку с кодом 1С
        """
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
                cmd, capture_output=True, text=True, timeout=30)

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
        return module
