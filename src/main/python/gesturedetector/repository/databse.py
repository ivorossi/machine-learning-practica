import sqlite3
from contextlib import closing
from threading import Lock


class SQLiteConnection:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SQLiteConnection, cls).__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self, db_path: str):
        if not self._initialized:
            self.db_path = db_path
            self._initialized = True

    def execute_query(self, query: str, params: tuple = ()) -> list:
        """
        Ejecuta una consulta SQL (SELECT).

        :param query: Consulta SQL a ejecutar.
        :param params: Parámetros para la consulta.
        :return: Lista de resultados.
        """
        with sqlite3.connect(self.db_path) as conn, closing(conn.cursor()) as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def execute_non_query(self, query: str, params: tuple = ()) -> None:
        """
        Ejecuta una consulta SQL (INSERT, UPDATE, DELETE).

        :param query: Consulta SQL a ejecutar.
        :param params: Parámetros para la consulta.
        """
        with sqlite3.connect(self.db_path) as conn, closing(conn.cursor()) as cursor:
            cursor.execute(query, params)
            conn.commit()

    def initialize_schema(self, schema_sql: str) -> None:
        """
        Inicializa la base de datos con un esquema SQL.

        :param schema_sql: Sentencia SQL para crear tablas.
        """
        with sqlite3.connect(self.db_path) as conn, closing(conn.cursor()) as cursor:
            cursor.executescript(schema_sql)
            conn.commit()
