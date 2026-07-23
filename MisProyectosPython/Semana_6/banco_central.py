# banco_central.py
# Semana 6 - Patron de diseno SINGLETON.
#
# Problema: en la Fintech Quantum Core NO queremos que se cree un "Banco Central"
# nuevo cada vez que alguien hace un pago (eso causaria caos con los saldos y
# gastaria memoria). Necesitamos UNA sola instancia en todo el sistema.
#
# Solucion: el patron Singleton garantiza una unica instancia y un punto de
# acceso global a ella.
#
# Para ejecutar:  python banco_central.py


class BancoCentral:
    """Singleton: por mas veces que lo crees, SIEMPRE es el mismo objeto."""

    # Atributo de CLASE (estatico): guarda la unica instancia.
    # En UML se dibuja SUBRAYADO por ser estatico.
    _instancia = None

    # __new__ se ejecuta ANTES que __init__ y es quien CREA el objeto.
    # Aqui interceptamos la creacion: si ya existe una instancia, la devolvemos;
    # si no, la creamos una sola vez.
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.reservas = 0   # se inicializa una unica vez
        return cls._instancia

    def emitir_moneda(self, cantidad):
        self.reservas += cantidad
        return self.reservas


# ============================================================
# Demostracion: aunque creemos "varios", es el MISMO objeto
# ============================================================
if __name__ == "__main__":
    banco_a = BancoCentral()
    banco_b = BancoCentral()

    print("id(banco_a):", id(banco_a))
    print("id(banco_b):", id(banco_b))
    print("Son el mismo objeto?:", banco_a is banco_b)   # True

    # Aunque intentemos crear 100 en un bucle, siempre es la misma instancia:
    ultimo = None
    for _ in range(100):
        ultimo = BancoCentral()
        print("id(ultimo):", id(ultimo))
    print("El #100 es el mismo?:", ultimo is banco_a)     # True


    banco_a.emitir_moneda(1000)
    banco_b.emitir_moneda(500)
    # Como son el mismo objeto, las reservas se comparten:
    print("Reservas totales (compartidas):", banco_b.reservas)   # 1500
