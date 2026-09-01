"""
diseno_pilares_poo.py
Semana 3 - Actividad 1: Robustez con Encapsulamiento, Herencia y Polimorfismo.

Este archivo es la evolucion de transaccion_poo_v1.py (Semana 2). Alli logramos
que el codigo FUNCIONARA con POO; aqui lo hacemos SEGURO y EXTENSIBLE.

Los tres pilares, y donde vive cada uno en este archivo:

    ENCAPSULAMIENTO -> el atributo pasa de self.monto a self._monto (privado por
                       convencion) y se accede mediante un getter (@property) y
                       un setter (@monto.setter) que VALIDA antes de guardar.
                       Ver la clase TransaccionBase, aqui abajo.

    HERENCIA        -> TransaccionCredito y TransaccionDebito NO repiten el
                       constructor ni los getters/setters: los heredan de
                       TransaccionBase escribiendo (TransaccionBase) al lado
                       del nombre de la clase.

    POLIMORFISMO    -> las dos hijas sobreescriben calcular_impacto() con su
                       propia formula. El bucle del final llama siempre al mismo
                       metodo y obtiene un resultado distinto segun el objeto.

Y los dos principios SOLID de esta semana:

    SRP (Responsabilidad Unica) -> cada funcion de este archivo hace UNA cosa:
        crear_transaccion() elige el tipo, leer_transacciones() lee el archivo,
        y cada clase se ocupa de su propio calculo. Compara esto con el archivo
        codigo_fragil_srp.py, donde un solo metodo hace las tres cosas a la vez.

    OCP (Abierto/Cerrado) -> para soportar un tipo nuevo (por ejemplo
        TransaccionEfectivo) solo agregas una clase hija y una linea en
        crear_transaccion(). NO tocas TransaccionBase ni el bucle principal.

Cada linea de transacciones.txt tiene:  ID, TIPO, MONTO
Para ejecutar:  python diseno_pilares_poo.py
"""


# =====================================================================
# 1) CLASE BASE (PADRE): datos comunes + ENCAPSULAMIENTO del monto
# =====================================================================
class TransaccionBase:
    """Clase base: encapsula el monto y define el comportamiento comun."""

    def __init__(self, id_transaccion, monto):
        self.id_transaccion = id_transaccion

        # IMPORTANTE: escribimos self.monto (SIN guion bajo), no self._monto.
        # Al hacerlo, Python NO asigna directamente: llama al SETTER de abajo,
        # que valida el dato. Asi ningun objeto puede nacer con un monto
        # invalido. Si aqui escribieras self._monto = monto te saltarias la
        # validacion y todo el blindaje dejaria de servir. Este es el error
        # mas comun de la actividad.
        self.monto = monto

    # -----------------------------------------------------------------
    # GETTER: el puente de LECTURA seguro hacia el atributo privado.
    # Gracias a @property, desde afuera se escribe t.monto (como si fuera
    # una variable normal), pero por dentro se ejecuta este metodo.
    # -----------------------------------------------------------------
    @property
    def monto(self):
        return self._monto

    # -----------------------------------------------------------------
    # SETTER: el puente de ESCRITURA. Aqui esta la clave del blindaje:
    # antes de guardar el dato lo VALIDAMOS y, si no cumple la regla,
    # lanzamos un ValueError. El dato malo se rechaza en el instante en
    # que alguien intenta asignarlo, no kilometros mas adelante.
    # -----------------------------------------------------------------
    @monto.setter
    def monto(self, nuevo_monto):
        if int(nuevo_monto) < 0:
            raise ValueError("El monto no puede ser negativo.")
        self._monto = int(nuevo_monto)

    # -----------------------------------------------------------------
    # Metodo "placeholder" (marcador de posicion): la clase base NO sabe
    # como calcular el impacto, porque depende del tipo de transaccion.
    # Al lanzar NotImplementedError obligamos a que cada clase hija defina
    # su propia version. Esto es lo que prepara el POLIMORFISMO.
    # -----------------------------------------------------------------
    def calcular_impacto(self):
        raise NotImplementedError("Cada tipo de transaccion define su impacto.")

    def obtener_informacion(self):
        # type(self).__name__ devuelve el nombre de la clase REAL del objeto
        # ("TransaccionCredito" o "TransaccionDebito"), no el de la base.
        return f"{self.id_transaccion} | {type(self).__name__} | ${self.monto}"


# =====================================================================
# 2) CLASES HIJAS (HERENCIA): reutilizan al padre y agregan lo suyo
# =====================================================================
# El (TransaccionBase) entre parentesis es la herencia: estas clases reciben
# gratis el __init__, el getter, el setter y obtener_informacion(). Solo
# escriben aquello que las hace diferentes.
class TransaccionCredito(TransaccionBase):
    def calcular_impacto(self):             # POLIMORFISMO: sobreescribe al padre
        return round(self.monto * 0.02, 2)  # tasa de interes del 2%


class TransaccionDebito(TransaccionBase):
    def calcular_impacto(self):             # POLIMORFISMO: sobreescribe al padre
        return 1500                         # comision fija


# =====================================================================
# 3) Crear el objeto correcto segun el TIPO (aqui se aplica el OCP)
# =====================================================================
def crear_transaccion(id_transaccion, tipo, monto):
    """
    Decide que clase instanciar segun el tipo leido del archivo.

    OCP en la practica: para soportar un tipo nuevo agregas su clase hija y
    un if aqui. El resto del programa (el bucle principal, el getter, el
    setter y las otras clases) no se toca.
    """
    if tipo == "CREDITO":
        return TransaccionCredito(id_transaccion, monto)
    if tipo == "DEBITO":
        return TransaccionDebito(id_transaccion, monto)
    raise ValueError(f"tipo desconocido '{tipo}'")


# =====================================================================
# 4) Leer el archivo con ROBUSTEZ (try/except)
# =====================================================================
def leer_transacciones(nombre_archivo):
    """
    Lee el archivo y crea los objetos, sin que un dato malo tumbe el programa.

    Como trabajan en equipo el encapsulamiento y el try/except:
        1. El SETTER detecta el monto invalido y lanza ValueError.
        2. El try/except de aqui abajo ATRAPA ese error.
        3. Mostramos un aviso, ignoramos esa linea y seguimos con las demas.

    Sin este try/except, la transaccion T005 (monto -1 en transacciones.txt)
    detendria el programa y perderias las 4 transacciones validas.
    """
    transacciones = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if not linea.strip():
                continue  # ignora lineas en blanco (por ejemplo el salto final)
            id_transaccion, tipo, monto = linea.strip().split(",")
            try:
                transacciones.append(crear_transaccion(id_transaccion, tipo, monto))
            except ValueError as error:
                # No se detiene el programa: se deja constancia y se continua.
                print(f"  [Aviso] Se ignoro {id_transaccion}: {error}")
    return transacciones


# =====================================================================
# 5) Funcion principal
# =====================================================================
def ejecutar_sistema():
    transacciones = leer_transacciones("transacciones.txt")

    print("\n--- Transacciones cargadas ---")
    for t in transacciones:
        # POLIMORFISMO en accion: fijate que este bucle NO tiene un solo if
        # para distinguir creditos de debitos. La misma llamada,
        # t.calcular_impacto(), ejecuta la formula que corresponde a cada
        # objeto. Si mañana agregas un tipo nuevo, esta linea no cambia.
        print(t.obtener_informacion(), "-> impacto:", t.calcular_impacto())


# Iniciar el programa SOLO cuando se ejecuta este archivo directamente.
# Asi, otros archivos (como la migracion a la base de datos) pueden IMPORTAR
# las clases y funciones sin que se ejecute toda la demo.
if __name__ == "__main__":
    ejecutar_sistema()
