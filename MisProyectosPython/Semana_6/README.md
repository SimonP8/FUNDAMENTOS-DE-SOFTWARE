# Semana 6 — Modelado de sistemas (UML y patrones de diseño)

Esta semana **no programamos algo nuevo**: aprendemos a hacer los **planos** de nuestro
software con **UML** (diagrama de clases) y aplicamos el patrón de diseño **Singleton**.

## Archivos

| Archivo | Actividad | Para qué sirve |
|---------|-----------|----------------|
| [`usuarios.py`](./usuarios.py) | **Actividad 1** | Código de la *Quantum Wallet* que vas a traducir a un diagrama UML. |
| [`banco_central.py`](./banco_central.py) | **Actividad 2** | Patrón **Singleton**: una única instancia del Banco Central. |

---

## Actividad 1 — Del código al plano (Quantum Wallet)

Traduce `usuarios.py` a un **diagrama de clases UML** (en Draw.io, Lucidchart, etc.).

**Mapa código → UML:**

| En el código | En el UML |
|--------------|-----------|
| `class Wallet`, `class Usuario`, `class UsuarioEmpresa` | 3 cajas (rectángulos) |
| `self.__saldo` (doble guion bajo) | atributo **privado** → `- saldo: float` |
| `self.nombre` (simple) | atributo **público** → `+ nombre: str` |
| `def consultar_saldo(self)` | método **público** → `+ consultar_saldo()` |
| `class UsuarioEmpresa(Usuario)` | **herencia**: flecha con **triángulo hueco △** apuntando a `Usuario` |
| `self.__wallet = Wallet()` dentro del `__init__` de `Usuario` | **composición**: línea con **rombo relleno ◆** en el extremo de `Usuario` |

> El rombo es relleno (composición, no agregación) porque la `Wallet` **se crea dentro** del
> `Usuario` y **no existe sin él**: si borras el `Usuario`, su `Wallet` desaparece.

Métodos que deben aparecer: `Wallet` → `+consultar_saldo()`, `+recargar()`; `Usuario` →
`+realizar_pago()`; `UsuarioEmpresa` → `+generar_factura()`.

---

## Actividad 2 — El patrón Singleton

Un **patrón de diseño** es una solución estándar a un problema común (una plantilla, no código
para copiar y pegar). El **Singleton** asegura que una clase tenga **una única instancia** y un
punto de acceso global a ella.

`banco_central.py` lo implementa con `__new__` (el método que **crea** el objeto, antes que
`__init__`). Al ejecutarlo verás con `id()` que dos variables distintas son **el mismo objeto**:

```bash
python banco_central.py
```

Salida esperada (los dos `id()` son iguales):
```
id(banco_a): 1990...
id(banco_b): 1990...
Son el mismo objeto?: True
El #100 es el mismo?: True
Reservas totales (compartidas): 1500
```

**Para el informe:** explica por qué en un sistema bancario es **peligroso NO** usar un Singleton
para el gestor de la base de datos o el emisor de moneda (pista: saldos inconsistentes, dinero
"duplicado", desperdicio de memoria).

---

## Cómo ejecutar
```bash
python usuarios.py         # ver la Quantum Wallet funcionando
python banco_central.py    # ver la única instancia del Singleton
```
