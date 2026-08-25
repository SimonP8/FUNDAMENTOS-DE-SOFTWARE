# comienzos_python.py
# Primeros pasos en Python: tipos de variables, condicionales y nombres.
# Para ejecutar:  python comienzos_python.py


# 1) TIPOS DE VARIABLES
# En Python no se declara el tipo, Python lo deduce del valor.

edad = 25            # int   -> numero entero
estatura = 1.75      # float -> numero con decimales
nombre = "Ana"       # str   -> texto
es_estudiante = True # bool  -> True o False
notas = [4.5, 3.8, 5.0]               # list -> varios valores
estudiante = {"nombre": "Ana", "edad": 25}  # dict -> clave: valor

print("Edad:", edad)
print("Estatura:", estatura)
print("Nombre:", nombre)
print("Es estudiante:", es_estudiante)
print("Notas:", notas)
print("Estudiante:", estudiante)

print()  # linea en blanco


# 2) CONDICIONALES (if / elif / else)
# El programa decide segun se cumpla o no una condicion.

nota = 2.9

if nota >= 4.5:
    print("Excelente")
elif nota >= 3.0:
    print("Aprobado")
else:
    print("Reprobado")

print()


# 3) NOMBRES DE VARIABLES
# - usa nombres claros y en minusculas
# - no pueden empezar por numero ni llevar espacios
# - Python diferencia mayusculas de minusculas (edad no es lo mismo que Edad)

nombre_completo = "Ana Perez"   # bien: descriptivo
monto_total = 150000            # bien: se entiende que guarda

print("Nombre completo:", nombre_completo)
print("Monto total:", monto_total)

print()


# 4) FUNCIONES (def)
# Una funcion es un bloque de codigo con nombre que se puede reutilizar.
# - se define con  def  seguido del nombre y parentesis
# - dentro de los parentesis van los parametros (datos que recibe)
# - return  devuelve un resultado a quien la llamo

def saludar(nombre):           # recibe un parametro: nombre
    return "Hola, " + nombre   # devuelve un texto

def sumar(a, b):               # recibe dos parametros
    return a + b               # devuelve la suma

# Para usar una funcion se la "llama" con sus datos:
print(saludar("Simon"))          # Hola, Simon
print("Suma:", sumar(3, 5))    # Suma: 8

print()


# 5) BUCLE FOR
# Repite un bloque una vez por cada elemento de una coleccion (lista, texto...).

notas = [4.5, 3.8, 5.0, 2.9]  # lista de notas
for nota in notas:             # 'nota' toma cada valor de la lista
    print("Nota:", nota)

# range(1, 4) genera 1, 2, 3  (el final no se incluye)
for numero in range(1, 10):
    print("Numero:", numero)

print()


# 6) BUCLE WHILE
# Repite MIENTRAS se cumpla una condicion.
# Hay que cambiar la condicion dentro del bucle para que algun dia termine.

contador = 1
while contador < 3:           # mientras contador sea 1, 2 o 3
    print("Contador:", contador)
    contador = contador + 1    # si no aumentamos, seria un bucle infinito

print()


# 7) DO-WHILE (no existe en Python, se imita)
# Un do-while ejecuta el codigo AL MENOS UNA VEZ y luego revisa la condicion.
# En Python se logra con  while True  +  break  (break corta el bucle).

numero = 0
while True:                    # se ejecuta siempre la primera vez
    print("Valor:", numero)
    numero = numero + 1
    if numero >= 3:            # condicion de salida
        break                  # rompe el bucle
