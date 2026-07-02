# migrar_transacciones.py
# Lleva las transacciones de ../transacciones.txt hacia una base de datos MySQL
# (que corre en Docker, contenedor "empresa") usando Prisma.
#
# La idea clave (el "siguiente nivel"):
#   Reutilizamos EXACTAMENTE las mismas clases POO de diseno_pilares_poo.py
#   (Encapsulamiento, Herencia, Polimorfismo). La unica diferencia con la carpeta
#   BaseDeDatos es que ahora los datos se guardan en un SERVIDOR MySQL real
#   en vez de un archivo SQLite.
#
# Ejecutar (parado dentro de la carpeta Mysql_Prisma):  python migrar_transacciones.py

import os
import sys

from dotenv import load_dotenv

# 0) Cargamos las variables del .env (DATABASE_URL) para que Prisma sepa
#    a que MySQL conectarse. Con SQLite no hacia falta; con MySQL, si.
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

# --- Permitir importar el archivo de la Semana 3 (esta una carpeta mas arriba) ---
CARPETA_ACTUAL = os.path.dirname(os.path.abspath(__file__))
CARPETA_SEMANA3 = os.path.join(CARPETA_ACTUAL, "..")
sys.path.append(CARPETA_SEMANA3)

from diseno_pilares_poo import leer_transacciones   # <- MISMAS clases POO
from prisma import Prisma


def tipo_legible(transaccion):
    """TransaccionCredito -> 'CREDITO'   |   TransaccionDebito -> 'DEBITO'."""
    return type(transaccion).__name__.replace("Transaccion", "").upper()


def migrar():
    # 1) Leemos el .txt usando la MISMA funcion de la Semana 3.
    #    Los registros invalidos (como T005 con monto negativo) se ignoran solos.
    ruta_txt = os.path.join(CARPETA_SEMANA3, "transacciones.txt")
    transacciones = leer_transacciones(ruta_txt)

    # 2) Nos conectamos a la base de datos MySQL.
    db = Prisma()
    db.connect()

    # 3) Empezamos limpio para poder correr este script las veces que queramos.
    db.transaccion.delete_many()

    print("\n--- Guardando transacciones en MySQL ---")
    for t in transacciones:
        registro = db.transaccion.create(
            data={
                "codigo": t.id_transaccion,
                "tipo": tipo_legible(t),
                "monto": t.monto,                        # encapsulado y validado en la clase
                "impacto": float(t.calcular_impacto()),  # POLIMORFISMO: cada tipo calcula distinto
            }
        )
        print(f"  Guardado {registro.codigo} | {registro.tipo} | ${registro.monto} -> impacto: {registro.impacto}")

    total = db.transaccion.count()
    print(f"\nListo. La base de datos ahora tiene {total} transacciones.")
    db.disconnect()


if __name__ == "__main__":
    migrar()
