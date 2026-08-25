# Semana 2 — Programación Orientada a Objetos: clases y objetos

## Paso 1: Análisis de fragilidad (Programación Estructurada)

En la Semana 1 resolvimos todo con **Programación Estructurada (PE)**: los **datos**
viven en diccionarios (`producto_id`, `categoria`, `valor`) y la **lógica** vive en
funciones sueltas (`calcular_valor_total`, `filtrar_por_categoria`). Funciona bien con
pocos casos, pero tiene problemas cuando el sistema crece.

### ¿Por qué la PE fallaría con 10 tipos de transacciones diferentes?

- **Funciones que se inflan:** cada nuevo tipo (venta, devolución, abono, cuota...)
  obliga a llenar las funciones de `if / elif / else`. Una sola función termina
  intentando hacer de todo y se vuelve enorme y difícil de leer.
- **Cambios regados por todos lados:** si agregas un dato nuevo (por ejemplo `impuesto`),
  tienes que tocar la lectura, el cálculo del total, el filtro... varios sitios a la vez.
  Es fácil olvidar uno.
- **No escala:** duplicas lógica parecida una y otra vez (copy–paste), y mantener todas
  esas copias sincronizadas es una fuente constante de bugs.

### ¿Por qué tener los datos (cliente_id, monto) separados de la lógica (calcular_total) crea un riesgo de debugging?

Porque **nada garantiza que los datos y la función "encajen"**. La función
`calcular_total` confía en que el diccionario tenga exactamente la clave `valor` y que sea
un número. Si alguien escribe `"Valor"` con mayúscula, olvida convertir a `int`, o le pasa
un diccionario incompleto, **el error no salta donde está el problema**, sino más adelante,
cuando la función intenta usar ese dato. Resultado: pasas horas buscando el fallo lejos de
su verdadero origen.

> En POO, los datos y su lógica viven **juntos** dentro del objeto. El objeto se construye
> con sus datos correctos desde el inicio (en el constructor `__init__`) y él mismo sabe
> calcularse. Eso reduce drásticamente este tipo de errores.

---

## Paso 2: El salto al Objeto — Refactorización

- Archivo de partida (PE, el "antes"): [`procesador_ventas.py`](./procesador_ventas.py)
- Archivo refactorizado (POO, el "después"): [`transaccion_poo_v1.py`](./transaccion_poo_v1.py)

En el "después":

1. Creamos la **Clase** `Venta`.
2. El **constructor** `__init__` encapsula los datos dispersos (`producto_id`, `categoria`,
   `valor`) como **atributos** del objeto.
3. La lógica de PE se convierte en **métodos** (cada objeto puede `obtener_informacion()`).
4. `leer_y_almacenar_datos` ahora crea y almacena **objetos** `Venta` en la lista
   principal, en lugar de diccionarios.

> **Nota sobre el nombre:** en el enunciado de Canvas la clase se llama `Transaccion`
> (con atributos `ID`, `Tipo`, `Monto`). Aquí la modelamos como `Venta` para mantener la
> continuidad con el código de ventas de la Semana 1. El concepto es **idéntico**: una
> entidad que reúne sus datos y su comportamiento. La equivalencia es:
> `ID → producto_id`, `Tipo → categoria`, `Monto → valor`.

## Cómo ejecutar

```bash
python procesador_ventas.py     # versión PE (antes)
python transaccion_poo_v1.py    # versión POO (después)
```
