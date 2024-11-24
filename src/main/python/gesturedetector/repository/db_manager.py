import sqlite3


conn = sqlite3.connect("src/main/resources/my_db.db")
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')



print("Base de datos y tabla creadas exitosamente.")

cursor.execute('''
INSERT INTO usuarios (nombre, edad, email)
VALUES (?, ?, ?)
''', ("Juan Pérez", 30, "juan.perez@example.com"))

conn.commit()


cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()  # Obtener todos los resultados
for usuario in usuarios:
    print(usuario)


# Cerrar el cursor y la conexión
cursor.close()
conn.close()
