"""
serializacion_json.py
Semana 4 - Actividad 2: Serializacion y persistencia (JSON).

EL PROBLEMA QUE RESOLVEMOS
--------------------------
Tus objetos viven en la MEMORIA de Python: existen mientras el programa corre y
desaparecen cuando termina. Para guardarlos en un disco, meterlos en una base de
datos o enviarlos por internet, hay que convertirlos a un formato de texto que
cualquier sistema entienda. Ese formato universal es JSON.

LA ANALOGIA DEL VIAJE (la que pide el Paso 1 de la actividad)
--------------------------------------------------------------
Serializar es EMPACAR: no puedes enviar tu casa por correo, asi que metes su
contenido en una caja plana y etiquetada. El objeto se vuelve texto, y el texto
si cabe en un archivo o en una peticion HTTP.
Deserializar es DESEMPACAR al llegar: tomas la caja y vuelves a armar el objeto.

EL VIAJE COMPLETO, EN DOS ESCALAS
----------------------------------
    Objeto Python  ->  Diccionario  ->  Texto JSON      (serializar)
    Texto JSON     ->  Diccionario  ->  Objeto Python   (deserializar)

La escala del medio, el DICCIONARIO, no es opcional: el modulo json no sabe
traducir un objeto de una clase que tu inventaste, pero si sabe traducir un
diccionario. Por eso primero pasamos por ahi.

Que se pierde al serializar: los METODOS. El JSON guarda solo los DATOS
(cliente_id, tipo, monto). Al deserializar, los metodos vuelven porque se los
devuelve la clase cuando llamamos al constructor.

Para ejecutar:  python serializacion_json.py
"""

import json


# Clase base (la misma del enunciado de la actividad)
class Transaccion:
    def __init__(self, cliente_id, tipo, monto):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        return f"Transaccion [{self.tipo}] - ID: {self.cliente_id}, Monto: {self.monto}"


# ---------- SERIALIZACION:  Objeto -> Diccionario -> Texto JSON ----------
def objeto_a_json(transaccion):
    """Empaca el objeto para el viaje: primero diccionario, luego texto."""
    # Paso 1: el Objeto se convierte en un DICCIONARIO simple.
    # Leemos sus atributos uno por uno y los ponemos como claves.
    # Aqui es donde se "pierden" los metodos: solo copiamos DATOS.
    como_dict = {
        "cliente_id": transaccion.cliente_id,
        "tipo": transaccion.tipo,
        "monto": transaccion.monto,
    }

    # Paso 2: el Diccionario se convierte en una CADENA DE TEXTO JSON.
    # OJO: json.dumps NO devuelve un diccionario, devuelve un str. Ese detalle
    # es el que mas se pregunta en el quiz.
    return json.dumps(como_dict)


# ---------- DESERIALIZACION:  Texto JSON -> Diccionario -> Objeto ----------
def json_a_objeto(texto_json):
    """Desempaca al llegar: del texto al diccionario, y del diccionario al objeto."""
    # Paso 1: la cadena JSON se convierte de nuevo en un DICCIONARIO.
    # json.loads solo llega hasta aqui: NO sabe crear un objeto Transaccion,
    # porque esa clase la inventaste tu y el modulo json no la conoce.
    como_dict = json.loads(texto_json)

    # Paso 2: usamos las claves del diccionario para LLAMAR AL CONSTRUCTOR.
    # Este paso es manual y es el que devuelve al objeto sus metodos.
    return Transaccion(como_dict["cliente_id"], como_dict["tipo"], como_dict["monto"])


# ---------- Demostracion ----------
def ejecutar():
    original = Transaccion("C002", "CREDITO", 500000)
    print("1) Objeto original :", original)
    print("   Tipo de dato    :", type(original).__name__, "(vive en memoria, tiene metodos)")

    texto = objeto_a_json(original)
    print("2) Serializado     :", texto)
    print("   Tipo de dato    :", type(texto).__name__, "(es TEXTO: ya puede viajar o guardarse)")

    reconstruido = json_a_objeto(texto)
    print("3) Deserializado   :", reconstruido)
    print("   Tipo de dato    :", type(reconstruido).__name__, "(volvio a ser objeto, con sus metodos)")


if __name__ == "__main__":
    ejecutar()
