import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT,
email, TEXT
)
"""
               )

conn.commit()

#Crear usuario
def crear_usuario (nombre:str, email:str)-> str:
        cursor.execute("INSERT INTO usuarios (nombre,email) VALUES (?,?)",(nombre,email))
        conn.commit()
        return "USUARIO AGREGADO"


def obtener_registro ():
        cursor.execute("SELECT id, nombre, email FROM usuarios")
        usuarios = cursor.fetchall()
        
        for usuario in usuarios:
            print(usuario)

        return usuario

def obtener_usuario(id)->int:
        cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id=?", (id,))
        usuario = cursor.fetchone()

        if(usuario):
               return usuario
        return"Usuario no encontrado"

