# Semana 7 — Arquitectura de bases de datos (SQLite)

Hasta ahora Quantum Core era **volátil**: al apagar el equipo se perdían los datos. Esta semana le
damos **memoria eterna** traduciendo el diseño UML de la Semana 6 a una **base de datos relacional
real** con **SQL y SQLite**.

## Archivos

| Archivo | Actividad | Qué hace |
|---------|-----------|----------|
| [`configurar_db.py`](./configurar_db.py) | **Actividad 1** | Crea `quantum_wallet.db` con las tablas `usuarios` y `wallets` (PK y FK). |
| [`practica_crud.py`](./practica_crud.py) | **Actividad 2** | CRUD completo sobre una tercera tabla `contactos`. |
| `quantum_wallet.db` | — | La base de datos que se genera al ejecutar `configurar_db.py`. |

---

## Actividad 1 — Del UML al esquema de base de datos

Cada clase principal del UML se vuelve una **tabla**:

| Clase (Semana 6) | Tabla | Campos | Tipos |
|------------------|-------|--------|-------|
| `Usuario` / `UsuarioEmpresa` | `usuarios` | id_usuario (**PK**), nombre, email, nit | INTEGER, TEXT, TEXT, TEXT |
| `Wallet` | `wallets` | id_wallet (**PK**), saldo, id_propietario (**FK**) | INTEGER, REAL, INTEGER |

- **PK (llave primaria):** `id_usuario`, número único e irrepetible por fila.
- **FK (llave foránea):** `wallets.id_propietario` apunta a `usuarios.id_usuario` → así el sistema
  sabe de quién es cada billetera.
- **Tipos:** `INTEGER` (enteros/IDs), `TEXT` (nombre, email), `REAL` (saldo, porque tiene centavos).

Verifica que SQLite esté disponible:
```bash
python -c "import sqlite3; print('SQLite esta listo para usarse')"
```
Crea la base:
```bash
python configurar_db.py
```

---

## Actividad 2 — CRUD sobre la tabla `contactos`

`practica_crud.py` demuestra las 4 operaciones (cada una en su función comentada):

- **C — Create:** inserta 6 contactos: 5 para el usuario 1 y 1 para el usuario 2.
- **R — Read:** muestra en consola los contactos del usuario 1.
- **U — Update:** cambia el apodo de un contacto (con `WHERE` para no tocar los demás).
- **D — Delete:** elimina el contacto con id 2.

```bash
python practica_crud.py
```

Salida esperada (resumida):
```
C - Create: 6 contactos insertados (5 del usuario 1 y 1 del usuario 2).
R - Read: contactos del usuario 1:
    (1, 'Mama', '3001112233')
    (2, 'Casa', '6041234567')
    ...
U - Update: el contacto 1 ahora se llama 'Mamita'.
D - Delete: contacto 2 eliminado.

Estado final de la tabla contactos:
    (1, 'Mamita', '3001112233')
    (3, 'Trabajo', '3009998877')
    ...
```

---

## Visualizar la base de datos

- **En VS Code:** instala la extensión **SQLite Viewer** (o *SQLite DB Viewer*), clic derecho sobre
  `quantum_wallet.db` → abrir con la extensión.
- **En el navegador:** sube el archivo a <https://inloop.github.io/sqlite-viewer/>.

Toma capturas del **antes y después** del Update para la evidencia.

---

## ⚠️ Seguridad: siempre parámetros `?`

Fíjate que las consultas usan `?` en vez de pegar los valores en el texto SQL:
```python
con.execute("SELECT * FROM contactos WHERE id_usuario = ?;", (id_usuario,))
```
Esto evita errores y **inyección SQL**. Es una práctica profesional obligatoria.
