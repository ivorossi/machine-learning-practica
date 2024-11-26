from databse import SQLiteConnection

db = SQLiteConnection("mi_base_de_datos.db")


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


