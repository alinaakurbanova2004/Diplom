"""
Модуль для работы с базой данных PostgreSQL
"""

import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Dict, Any, Optional
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class DatabaseConnection:
    """Подключение к PostgreSQL"""
    
    def __init__(self, host: str, port: int, database: str, user: str, password: str):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conn = None
    
    def connect(self) -> bool:
        """Устанавливает соединение с БД"""
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print(f"✅ Подключение к БД {self.database} успешно")
            return True
        except Exception as e:
            print(f"❌ Ошибка подключения к БД: {e}")
            return False
    
    def disconnect(self):
        """Закрывает соединение"""
        if self.conn:
            self.conn.close()
            print("🔌 Соединение с БД закрыто")
    
    def execute_query(self, query: str, params: tuple = None) -> List[Dict]:
        """Выполняет SELECT и возвращает результат"""
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            return cur.fetchall()
    
    def execute_non_query(self, query: str, params: tuple = None) -> int:
        """Выполняет INSERT/UPDATE/DELETE, возвращает количество затронутых строк"""
        with self.conn.cursor() as cur:
            cur.execute(query, params)
            self.conn.commit()
            return cur.rowcount


class RuleRepository:
    """Работа с таблицей правил"""
    
    def __init__(self, db: DatabaseConnection):
        self.db = db
    
    def get_all_active_rules(self) -> List[Dict]:
        """Получает все активные правила из БД"""
        query = """
            SELECT id, code, name, description, severity, is_active, 
                   file_path, class_name
            FROM development_rule
            WHERE is_active = TRUE
            ORDER BY code
        """
        return self.db.execute_query(query)
    
    def get_rule_by_code(self, code: str) -> Optional[Dict]:
        """Получает правило по коду"""
        query = "SELECT * FROM development_rule WHERE code = %s"
        result = self.db.execute_query(query, (code,))
        return result[0] if result else None
    
    def get_parameters_for_rule(self, rule_id: int) -> List[Dict]:
        """Получает параметры для правила"""
        query = """
            SELECT param_name, param_value, param_type
            FROM rule_parameter
            WHERE rule_id = %s AND is_active = TRUE
        """
        return self.db.execute_query(query, (rule_id,))
    
    def get_regexps_for_rule(self, rule_id: int) -> List[Dict]:
        """Получает регулярные выражения для правила"""
        query = """
            SELECT pattern, flags, is_positive
            FROM regexp
            WHERE rule_id = %s
        """
        return self.db.execute_query(query, (rule_id,))


class ViolationRepository:
    """Сохранение нарушений в БД"""
    
    def __init__(self, db: DatabaseConnection):
        self.db = db

    
    def save_violation(self, violation: Violation, rule_id: int, module_id: int = None) -> int:
        """Сохраняет одно нарушение в БД"""
        query = """
            INSERT INTO violation (rule_id, module_id, line_number, column_number, message, snippet)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
        """
        params = (
            rule_id,
            module_id,
            violation.line,
            violation.column,
            violation.message,
            getattr(violation, 'code_snippet', '')
        )
    
        print(f"💾 SQL: {query % params}")
    
        try:
            # Используем execute_non_query для INSERT с RETURNING
            with self.db.conn.cursor() as cur:
                cur.execute(query, params)
                inserted_id = cur.fetchone()[0]
                self.db.conn.commit()  # ← ВАЖНО!
                print(f"   ✅ Вставлено, id={inserted_id}")
                return inserted_id
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            self.db.conn.rollback()
            return None

class ModuleRepository:
    """Работа с таблицей модулей"""
    
    def __init__(self, db: DatabaseConnection):
        self.db = db
    
    def save_module(self, name: str, path: str = None, hash_value: str = None) -> int:
        """Сохраняет модуль и возвращает его ID"""
        # Сначала проверяем, есть ли уже такой модуль
        existing = self.get_module_id(name)
        if existing:
            print(f"📁 Модуль уже существует: {name} (id={existing})")
            return existing
    
        # Если нет — вставляем
        query = """
            INSERT INTO module (name, path, hash)
            VALUES (%s, %s, %s)
            RETURNING id
        """
        params = (name, path, hash_value)
        result = self.db.execute_query(query, params)
        return result[0]['id'] if result else None
    
    def get_module_id(self, name: str) -> Optional[int]:
        """Получает ID модуля по имени"""
        query = "SELECT id FROM module WHERE name = %s"
        result = self.db.execute_query(query, (name,))
        return result[0]['id'] if result else None