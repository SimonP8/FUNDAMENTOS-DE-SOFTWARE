# robustez_try_except.py
# Semana 4 - Gestion de errores y excepciones (try/except)
# Un archivo con datos corruptos NO detiene el programa: los registros validos
# se procesan igual, y los invalidos se REGISTRAN (log) y se saltan.
# Cada linea de transacciones_corruptas.txt tiene:  cliente_id, tipo, monto
# Para ejecutar:  python robustez_try_except.py


# 1) La clase con el monto ENCAPSULADO y VALIDADO (como en la Semana 3)
class Transaccion:
    """Transaccion que se protege a si misma: rechaza montos invalidos."""

    def __init__(self, cliente_id, tipo, monto):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = monto            # usa el SETTER (valida)

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, valor):
        # int(valor) lanza ValueError si 'valor' es texto ("cien"); y si es
        # negativo, lanzamos nosotros el ValueError (validacion de la Semana 3).
        if int(valor) < 0:
            raise ValueError("el monto no puede ser negativo")
        self._monto = int(valor)

    def __str__(self):
        return f"{self.cliente_id} | {self.tipo} | ${self.monto}"


# 2) Lectura TOLERANTE A FALLOS: un try/except por cada linea
def cargar_transacciones(nombre_archivo):
    """Lee el archivo; si una linea falla, la registra (log) y CONTINUA con la siguiente."""
    transacciones = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, start=1):
            linea = linea.strip()
            if not linea:
                continue  # ignora lineas en blanco
            try:
                partes = linea.split(",")
                # Si faltan datos (solo 2 columnas), el CONSTRUCTOR lanza TypeError.
                # Si el monto es "texto" o negativo, el SETTER lanza ValueError.
                transacciones.append(Transaccion(*partes))
            except ValueError as error:
                print(f"  [Linea {numero}] ValueError: {error}  ->  se ignora: {linea}")
            except TypeError:
                print(f"  [Linea {numero}] TypeError: datos insuficientes  ->  se ignora: {linea}")
    return transacciones


# 3) Programa principal
def ejecutar_sistema():
    transacciones = cargar_transacciones("transacciones_corruptas.txt")

    print()
    print(f"Se procesaron {len(transacciones)} transacciones validas:")
    for t in transacciones:
        print("  ", t)



if __name__ == "__main__":
    ejecutar_sistema()
