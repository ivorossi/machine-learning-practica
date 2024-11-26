
from src.main.python.gesturedetector.config.configurations import Config
import os
from src.main.python.gesturedetector.repository.databse import SQLiteConnection

if __name__ == '__main__':
    resources_path = Config.get_config().get('resources_path_dir')
    db_name = Config.get_config().get('db_name')
    db_path = os.path.join(resources_path, db_name)
    db = SQLiteConnection(db_path)

schema = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
"""
db.initialize_schema(schema)

# Ejecutar una consulta
db.execute_non_query("INSERT INTO users (name, email) VALUES (?, ?)", ("Ivo2", "ivo2@example.com"))
result = db.execute_query("SELECT * FROM users")
print(result)


