# configurar_db.py
# Semana 7 - Crea la base de datos quantum_wallet.db (SQLite) a partir del
# diseno UML de la Semana 6: dos tablas vinculadas (usuarios y wallets) con
# llave primaria (PK), llave foranea (FK) y tipos de datos coherentes.
# Ejecutar:  python configurar_db.py

import sqlite3

# 1) CONEXION: crea (o abre) el archivo quantum_wallet.db
conexion = sqlite3.connect("quantum_wallet.db")
cursor = conexion.cursor()

# En SQLite hay que activar el respeto por las llaves foraneas
cursor.execute("PRAGMA foreign_keys = ON;")

# 2) TABLA usuarios  (donde vive la identidad)
#    id_usuario = PK: numero unico e irrepetible para cada fila
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre     TEXT NOT NULL,
    email      TEXT,
    nit        TEXT
);
""")

# 3) TABLA wallets  (donde vive el dinero)
#    saldo = REAL porque tiene decimales (centavos)
#    id_propietario = FK que apunta al id_usuario de la tabla usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS wallets (
    id_wallet      INTEGER PRIMARY KEY AUTOINCREMENT,
    saldo          REAL NOT NULL DEFAULT 0,
    id_propietario INTEGER,
    FOREIGN KEY (id_propietario) REFERENCES usuarios(id_usuario)
);
""")

# 4) INSERCION de prueba (empezamos limpio para poder repetir el script)
#    Primero se borran las tablas HIJAS (las que tienen FK hacia usuarios) y
#    al final la tabla PADRE; si no, la FK impide borrar los usuarios.
#    'contactos' la crea practica_crud.py y se vuelve a crear al ejecutarlo.
cursor.execute("DROP TABLE IF EXISTS contactos;")
cursor.execute("DELETE FROM wallets;")
cursor.execute("DELETE FROM usuarios;")
# DELETE no reinicia el AUTOINCREMENT: lo reiniciamos para que los ids vuelvan a empezar en 1
cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('usuarios', 'wallets');")

cursor.execute(
    "INSERT INTO usuarios (nombre, email, nit) VALUES (?, ?, ?);",
    ("Ana Torres", "ana@quantum.com", None),
)
id_ana = cursor.lastrowid   # el id que le asigno la base de datos

cursor.execute(
    "INSERT INTO usuarios (nombre, email, nit) VALUES (?, ?, ?);",
    ("Bancolombia", "contacto@bancolombia.com", "900123456-7"),
)
id_empresa = cursor.lastrowid

# Cada usuario tiene su wallet: la FK id_propietario los vincula
cursor.execute("INSERT INTO wallets (saldo, id_propietario) VALUES (?, ?);", (150000.50, id_ana))
cursor.execute("INSERT INTO wallets (saldo, id_propietario) VALUES (?, ?);", (5000000.0, id_empresa))

# 5) GUARDAR cambios
conexion.commit()

# 6) VERIFICACION: unimos las dos tablas por la FK para probar la relacion
print("Base de datos 'quantum_wallet.db' creada y verificada:")
consulta = """
    SELECT u.id_usuario, u.nombre, w.saldo
    FROM usuarios u
    JOIN wallets w ON w.id_propietario = u.id_usuario;
"""
for id_usuario, nombre, saldo in cursor.execute(consulta):
    print(f"   Usuario {id_usuario}: {nombre}  ->  saldo ${saldo}")

# 7) CERRAR la conexion (buena practica)
conexion.close()
