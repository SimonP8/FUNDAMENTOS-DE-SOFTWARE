"""
transaccion_poo_v1.py
Semana 2 - Actividad 1, Paso 2: El salto al Objeto (Refactorizacion).

Este es el "DESPUES": tomamos procesador_ventas.py y movemos esos mismos
datos y esa misma logica DENTRO de una Clase. Compara este archivo linea a
linea con el anterior: no inventamos nada nuevo, solo reorganizamos lo que
ya teniamos para que datos y logica vivan juntos.

Vocabulario (el mismo que ves en la plataforma, Semana 2):
    Clase       -> el "plano": Venta. Se define UNA sola vez en el codigo.
    Objeto      -> una "casa" construida con ese plano: cada venta concreta.
    Atributo    -> un dato que vive DENTRO del objeto (antes: una clave del dict).
    Constructor -> __init__, se ejecuta solo, una vez, al crear (instanciar) el objeto.
    self        -> como el objeto se refiere a si mismo ("esto es MIO, no de otro").
    Metodo      -> una accion que el objeto ya sabe hacer con SUS propios datos.

NOTA sobre el nombre: en el enunciado de Canvas la clase se llama Transaccion
(atributos ID, Tipo, Monto). Aqui la modelamos como Venta, por continuidad
con la Semana 1:
    ID -> producto_id     Tipo -> categoria     Monto -> valor
El concepto es exactamente el mismo.

Para ejecutar:  python transaccion_poo_v1.py
"""


# 1) La CLASE: el plano que une los DATOS y la LOGICA de una sola venta.
#    A partir de esta UNICA definicion podemos crear tantos objetos Venta
#    como necesitemos (ver leer_y_almacenar_datos mas abajo): un plano,
#    muchas casas distintas.
class Venta:
    """Representa UNA venta: encapsula sus datos (atributos) y su comportamiento (metodos)."""

    def __init__(self, producto_id, categoria, valor):
        """
        Constructor: Python lo ejecuta automaticamente, una sola vez, al
        instanciar un objeto -- por ejemplo con Venta("P001", "HOGAR", 120000).

        'self' es el objeto que se esta creando en ESE momento: cada linea
        de aqui abajo dice "guarda este dato como MIO", sin mezclarse con
        los datos de otro objeto Venta que exista en el programa.
        """
        self.producto_id = producto_id   # atributo (antes: venta["producto_id"])
        self.categoria = categoria       # atributo (antes: venta["categoria"])
        self.valor = int(valor)          # atributo (antes: venta["valor"])

    def obtener_informacion(self):
        """
        METODO: una accion que el objeto ejecuta usando SUS PROPIOS atributos
        (self.producto_id, self.categoria, self.valor), sin que se los tengan
        que pasar desde afuera como en la version de PE.
        """
        return f"{self.producto_id} | {self.categoria} | ${self.valor}"


# 2) Leer el archivo y crear una LISTA DE OBJETOS (ya no de diccionarios).
#    Esta es la refactorizacion clave de la Actividad 1: donde antes haciamos
#    lista_ventas.append(diccionario), ahora hacemos ventas.append(objeto).
def leer_y_almacenar_datos(nombre_archivo):
    """Lee cada linea del archivo y la convierte en un objeto Venta."""
    ventas = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            producto_id, categoria, valor = linea.strip().split(",")
            # Pequeña validacion de entrada: descarta valores invalidos (ver
            # el producto P010 en ventas.txt, que trae un valor de -1). En
            # procesador_ventas.py esa venta invalida SI entraba a la suma sin
            # avisar; aqui, al menos, no se llega a crear el objeto. Blindar
            # esto de verdad (con un setter que valide y lance un error) es
            # el Encapsulamiento que viene en la Semana 3.
            if int(valor) > 0:
                venta = Venta(producto_id, categoria, valor)   # se INSTANCIA un objeto
                ventas.append(venta)                            # se guarda el OBJETO, no un dict
    return ventas


# 3) Funciones de gestion que ahora trabajan sobre OBJETOS, no diccionarios.
#    Nota el cambio de sintaxis: venta["valor"] paso a ser venta.valor.
def calcular_valor_total(ventas):
    """Suma el atributo .valor de todos los objetos Venta de la lista."""
    total = 0
    for venta in ventas:
        total = total + venta.valor   # acceso por ATRIBUTO, no por clave de diccionario
    return total


def filtrar_por_categoria(ventas, categoria):
    """Devuelve solo los objetos cuyo atributo .categoria coincide."""
    return [venta for venta in ventas if venta.categoria == categoria]


# 4) Funcion principal: el flujo se ve casi igual al de PE, pero ahora cada
#    elemento de la lista "ventas" es un objeto que sabe describirse solo.
def ejecutar_sistema():
    ventas = leer_y_almacenar_datos("ventas.txt")

    print("--- Todas las ventas ---")
    for venta in ventas:
        print(venta.obtener_informacion())   # el objeto se describe a si mismo

    print("\nValor total de las ventas:", calcular_valor_total(ventas))

    print("\n--- Solo ELECTRONICA ---")
    for venta in filtrar_por_categoria(ventas, "ELECTRONICA"):
        print(venta.obtener_informacion())


# Iniciar el programa
ejecutar_sistema()
