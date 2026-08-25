# practica_crud.py
# Semana 7 - Operaciones CRUD (Create, Read, Update, Delete) sobre una tercera
# tabla 'contactos', vinculada a los usuarios de quantum_wallet.db.
# Requiere haber ejecutado antes:  python configurar_db.py
# Ejecutar:  python practica_crud.py

import sqlite3

RUTA = "quantum_wallet.db"


def crear_tabla_contactos():
    """Crea la tabla contactos (si no existe), con FK al usuario dueno."""
    con = sqlite3.connect(RUTA)
    con.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
            apodo       TEXT NOT NULL,
            numero      TEXT,
            id_usuario  INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
        );
    """)
    con.commit()
    con.close()


# ---------- C : CREATE ----------
def crear_contactos():
    """Inserta 5 contactos para el usuario 1."""
    con = sqlite3.connect(RUTA)
    con.execute("DELETE FROM contactos;")   # limpio para poder repetir el ejercicio
    contactos = [
        ("Mama", "3001112233", 1),
        ("Casa", "6041234567", 1),
        ("Trabajo", "3009998877", 1),
        ("Mejor amigo", "3005556644", 1),
        ("Emergencias", "123", 1),
        ("Nubank", "3007778899", 2),
    ]
    # executemany inserta toda la lista de una vez, con parametros seguros (?)
    con.executemany(
        "INSERT INTO contactos (apodo, numero, id_usuario) VALUES (?, ?, ?);",
        contactos,
    )
    con.commit()
    con.close()
    print("C - Create: 6 contactos insertados para el usuario 1.")


# ---------- R : READ ----------
def leer_contactos(id_usuario):
    """Busca y muestra en consola todos los contactos de un usuario."""
    con = sqlite3.connect(RUTA)
    filas = con.execute(
        "SELECT id_contacto, apodo, numero FROM contactos WHERE id_usuario = ?;",
        (id_usuario,),
    ).fetchall()
    con.close()
    print(f"R - Read: contactos del usuario {id_usuario}:")
    for fila in filas:
        print("   ", fila)


# ---------- U : UPDATE ----------
def actualizar_apodo(id_contacto, nuevo_apodo):
    """Cambia el apodo de UN contacto. El WHERE evita cambiarlos todos."""
    con = sqlite3.connect(RUTA)
    con.execute(
        "UPDATE contactos SET apodo = ? WHERE id_contacto = ?;",
        (nuevo_apodo, id_contacto),
    )
    con.commit()
    con.close()
    print(f"U - Update: el contacto {id_contacto} ahora se llama '{nuevo_apodo}'.")


# ---------- D : DELETE ----------
def borrar_contacto(id_contacto):
    """Elimina UN contacto por su id (nunca toda la tabla)."""
    con = sqlite3.connect(RUTA)
    con.execute("DELETE FROM contactos WHERE id_contacto = ?;", (id_contacto,))
    con.commit()
    con.close()
    print(f"D - Delete: contacto {id_contacto} eliminado.")


if __name__ == "__main__":
    crear_tabla_contactos()
    crear_contactos()                  # C
    leer_contactos(1)                  # R
    actualizar_apodo(1, "Mamita")      # U
    borrar_contacto(2)                 # D
    print("\nEstado final de la tabla contactos:")
    leer_contactos(1)                  # R de nuevo, para ver el resultado
