"""
procesador_ventas.py
Semana 2 - Actividad 1, Paso 1: Analisis de fragilidad.

Este es el "ANTES": la misma logica de la Semana 1, en Programacion
Estructurada (PE). La dejamos intacta a proposito para poder comparar, linea
por linea, contra la version POO de transaccion_poo_v1.py.

Fijate en el patron que se repite en las 3 funciones de abajo:
    - Los DATOS viven en un diccionario suelto: venta["valor"], venta["categoria"]...
    - La LOGICA vive en funciones aparte, que reciben ese diccionario "a ciegas"
      y confian en que tenga las claves correctas.

Ese es justo el problema que resolvemos con POO (ver transaccion_poo_v1.py):
aqui nada impide que un diccionario venga incompleto o con una clave mal
escrita, y si eso pasa, el error aparece LEJOS de donde realmente esta la
falla (el riesgo de debugging del que habla la Actividad 1).

Cada linea de ventas.txt tiene: ProductoID, Categoria, Valor
Para ejecutar:  python procesador_ventas.py
"""


# 1) Leer el archivo y guardar cada venta como un DICCIONARIO suelto.
#    El "molde" de la venta (que datos tiene) no esta definido en ningun
#    lado: cada funcion que reciba este diccionario debe "adivinar" que
#    claves esperar y confiar en que esten bien escritas.
def cargar_ventas(nombre_archivo):
    lista_ventas = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")   # separar por comas
            venta = {
                "producto_id": partes[0],
                "categoria": partes[1],
                "valor": int(partes[2]),        # convertir el valor a numero
            }
            lista_ventas.append(venta)
    return lista_ventas


# 2) Sumar el valor de todas las ventas (la LOGICA vive separada de los DATOS).
#    OJO: esta funcion no valida nada. Revisa ventas.txt: el producto P010
#    tiene un valor de -1. Aqui esa venta invalida entra igual a la suma y
#    baja el total sin que nada te avise. Ese es el "riesgo de debugging":
#    el numero final se ve raro, pero el error esta escondido en el archivo
#    de datos, no en esta funcion.
def calcular_valor_total(lista_ventas):
    total = 0
    for venta in lista_ventas:
        total = total + venta["valor"]
    return total


# 3) Dejar solo las ventas de una categoria.
#    Misma historia: depende de que el diccionario SIEMPRE tenga la clave
#    "categoria" escrita exactamente asi. Si mañana esa clave cambia de
#    nombre, hay que salir a corregir esta funcion Y todas las que dependan
#    de "categoria" en el resto del programa.
def filtrar_por_categoria(lista_ventas, categoria):
    lista_filtrada = []
    for venta in lista_ventas:
        if venta["categoria"] == categoria:
            lista_filtrada.append(venta)
    return lista_filtrada


# 4) Funcion principal que orquesta todo el flujo de PE.
def ejecutar_sistema():
    ventas = cargar_ventas("ventas.txt")

    total = calcular_valor_total(ventas)
    print("Valor total de las ventas:", total)

    electronica = filtrar_por_categoria(ventas, "ELECTRONICA")
    print("Ventas de ELECTRONICA:")
    for venta in electronica:
        print(venta)   # se imprime el diccionario "crudo": {'producto_id': ...}


# Iniciar el programa
ejecutar_sistema()
