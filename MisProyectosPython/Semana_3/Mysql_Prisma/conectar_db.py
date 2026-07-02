# conectar_db.py
# La conexion MAS SIMPLE posible a la base de datos MySQL con Prisma.
# Se conecta, lee las transacciones guardadas y las muestra.
#
# Ejecutar (parado dentro de la carpeta Mysql_Prisma):  python conectar_db.py

import os

from dotenv import load_dotenv

# Cargamos el .env (DATABASE_URL) antes de conectar.
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

from prisma import Prisma

# 1) Creamos el cliente y nos conectamos a MySQL
db = Prisma()
db.connect()

# 2) Pedimos TODAS las transacciones de la tabla
transacciones = db.transaccion.find_many()

# 3) Las mostramos en pantalla
print(f"\nHay {len(transacciones)} transacciones en la base de datos:\n")
for t in transacciones:
    print(f"  {t.codigo} | {t.tipo} | ${t.monto} -> impacto: {t.impacto}")

# 4) Cerramos la conexion (buena practica)
db.disconnect()
