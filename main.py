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

#Obtener usuarios
def obtener_registro ():
        cursor.execute("SELECT id, nombre, email FROM usuarios")
        usuarios = cursor.fetchall()
        
        for usuario in usuarios:
            print(usuario)

        return usuario
#Obtener usuario por id
def obtener_usuario(id)->int:
        cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id=?", (id,))
        usuario = cursor.fetchone()

        if(usuario):
               return usuario
        return"Usuario no encontrado"

#Actualizar usuario
def actualizar_usuario (id, nombre,email):
       cursor.execute("UPDATE usuarios SET nombre = ?, email= ? WHERE id = ?", (nombre,email,id))
       conn.commit()

       return "Usuario Actualizado"

#Eliminar Usuario
def eliminar_usuario(id):
       cursor.execute("DELETE usuario FROM usuarios WHERE id = ?", (id,))
       conn.commit()
    
       return "Usuario eliminado"