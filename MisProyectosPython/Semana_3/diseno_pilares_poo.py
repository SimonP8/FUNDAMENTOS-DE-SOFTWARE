# diseno_pilares_poo.py
# Semana 3 - Pilares de POO: Encapsulamiento + Herencia + Polimorfismo
# Refactor robusto de transaccion_poo_v1.py (Semana 3).
# Cada linea de transacciones.txt tiene:  ID, TIPO, MONTO
# Para ejecutar:  python diseno_pilares_poo.py


# 1) CLASE BASE (PADRE): datos comunes + ENCAPSULAMIENTO del monto
class TransaccionBase:
    """Clase base: encapsula el monto y define el comportamiento comun."""

    def __init__(self, id_transaccion, monto):
        self.id_transaccion = id_transaccion
        self.monto = monto                 # usa el SETTER (valida el dato)

    # GETTER: puente de lectura seguro al atributo privado _monto
    @property
    def monto(self):
        return self._monto

    # SETTER: valida antes de guardar (aqui blindamos el dato)
    @monto.setter
    def monto(self, nuevo_monto):
        if int(nuevo_monto) < 0:
            raise ValueError("El monto no puede ser negativo.")
        self._monto = int(nuevo_monto)

    # Metodo "placeholder": cada hija lo sobreescribe (POLIMORFISMO)
    def calcular_impacto(self):
        raise NotImplementedError("Cada tipo de transaccion define su impacto.")

    def obtener_informacion(self):
        return f"{self.id_transaccion} | {type(self).__name__} | ${self.monto}"


# 2) CLASES HIJAS (HERENCIA): reutilizan al padre y agregan lo suyo
class TransaccionCredito(TransaccionBase):
    def calcular_impacto(self):             # POLIMORFISMO
        return round(self.monto * 0.02, 2)  # tasa de interes 2%


class TransaccionDebito(TransaccionBase):
    def calcular_impacto(self):             # POLIMORFISMO
        return 1500                        # comision fija


# 3) Crear el objeto correcto segun el TIPO (abierto a extension - OCP)
def crear_transaccion(id_transaccion, tipo, monto):
    if tipo == "CREDITO":
        return TransaccionCredito(id_transaccion, monto)
    if tipo == "DEBITO":
        return TransaccionDebito(id_transaccion, monto)
    raise ValueError(f"tipo desconocido '{tipo}'")


# 4) Leer el archivo con ROBUSTEZ (try/except): un dato malo no detiene todo
def leer_transacciones(nombre_archivo):
    transacciones = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if not linea.strip():
                continue  # ignora lineas en blanco (por ejemplo el salto final del archivo)
            id_transaccion, tipo, monto = linea.strip().split(",")
            try:
                transacciones.append(crear_transaccion(id_transaccion, tipo, monto))
            except ValueError as error:
                print(f"  [Aviso] Se ignoro {id_transaccion}: {error}")
    return transacciones


# 5) Funcion principal
def ejecutar_sistema():
    transacciones = leer_transacciones("transacciones.txt")

    print("\n--- Transacciones cargadas ---")
    for t in transacciones:
        # POLIMORFISMO: la misma llamada, distinto resultado segun el tipo
        print(t.obtener_informacion(), "-> impacto:", t.calcular_impacto())


# Iniciar el programa SOLO cuando se ejecuta este archivo directamente.
# Asi, otros archivos (como la migracion a la base de datos) pueden IMPORTAR
# las clases y funciones sin que se ejecute toda la demo.
if __name__ == "__main__":
    ejecutar_sistema()
