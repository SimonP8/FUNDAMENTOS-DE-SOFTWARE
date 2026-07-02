# Semana 3 — De un `.txt` a MySQL en Docker (con Prisma)

En la carpeta `BaseDeDatos` guardamos las transacciones en **SQLite** (un solo archivo).
**Ahora subimos de nivel:** las guardaremos en un **servidor MySQL real** que corre dentro de
**Docker**, reutilizando **las mismas clases POO** de [`diseno_pilares_poo.py`](../diseno_pilares_poo.py).

---

## ⚠️ Concepto clave

A diferencia de SQLite, **MySQL SÍ es un servidor**: tiene que estar "prendido" para poder
conectarte. Lo levantamos como un **contenedor de Docker**. Nuestro programa de Python se
conecta a ese servidor por el puerto **3306**, usando los datos del archivo **`.env`**.

---

## Requisitos previos

1. **Docker Desktop** instalado y abierto — <https://www.docker.com/products/docker-desktop/>
2. **Python 3** — <https://www.python.org/downloads/>

---

## Paso 0 — Levanta el contenedor de MySQL

La **primera vez**, crea el contenedor con este comando (ejecútalo una sola vez):

```powershell
docker run --name empresa -e MYSQL_ROOT_PASSWORD=12345 -p 3306:3306 -v mysql_datos:/var/lib/mysql -d mysql:8
```

- `--name empresa` → nombre del contenedor.
- `-e MYSQL_ROOT_PASSWORD=12345` → usuario **root** con contraseña **12345**.
- `-p 3306:3306` → publica el puerto para conectarte desde tu PC.
- `-v mysql_datos:/var/lib/mysql` → **persistencia**: los datos viven en el volumen `mysql_datos`
  y sobreviven aunque borres el contenedor.

> Las siguientes veces **no** repitas el `docker run`. Solo enciéndelo/ apágalo:
> ```powershell
> docker start empresa    # encender
> docker stop empresa     # apagar
> ```
> Espera unos 10-20 segundos tras encenderlo: MySQL tarda un poquito en estar listo.

---

## El archivo `.env` (¡clave para que funcione!)

[`.env`](./.env) le dice a Prisma **a dónde** conectarse. Ya viene listo:

```env
DATABASE_URL="mysql://root:12345@localhost:3306/empresa_db"
```

> 🔎 Ojo con los nombres: **`empresa`** es el *contenedor* de Docker; **`empresa_db`** es la
> *base de datos* que Prisma creará dentro de MySQL. No son lo mismo.

> 🔐 En un proyecto real, el `.env` **no** se sube a GitHub (lleva contraseñas). Aquí lo dejamos
> versionado a propósito porque es una base local de práctica.

---

## Requisitos de Python

Parado **dentro de la carpeta `Mysql_Prisma`**:

```powershell
cd "MisProyectosPython\Semana_3\Mysql_Prisma"
pip install -r requirements.txt
```

> Instala `prisma` (trae el comando `prisma`, no necesitas Node.js) y `python-dotenv`
> (carga el `.env` cuando corres los scripts).
>
> 🛟 ¿`prisma` "no se reconoce" o error de permisos al instalar? Mira **Problemas comunes** al final.

---

## Paso 1 — Mira el plano (`schema.prisma`)

[`schema.prisma`](./schema.prisma) define el motor (MySQL) y la forma de la tabla:

```prisma
datasource db {
  provider = "mysql"
  url      = env("DATABASE_URL")   // lee la conexion del .env
}

model Transaccion {
  id      Int    @id @default(autoincrement())
  codigo  String @unique
  tipo    String
  monto   Int
  impacto Float
}
```

---

## Paso 2 — Crea la base de datos y la tabla

Con el contenedor **encendido**, ejecuta:

```powershell
prisma db push
```

Esto se conecta a MySQL, **crea la base `empresa_db`** (si no existe), crea la tabla
`Transaccion` y genera el cliente de Prisma para Python. Al terminar verás
*"Your database is now in sync with your schema"*. ✅

---

## Paso 3 — Migra el `.txt` a MySQL

[`migrar_transacciones.py`](./migrar_transacciones.py) reutiliza **las mismas clases POO** de la
Semana 3 y, en vez de imprimir el impacto, lo **guarda** en MySQL:

```powershell
python migrar_transacciones.py
```

Salida esperada:

```
  [Aviso] Se ignoro T005: El monto no puede ser negativo.

--- Guardando transacciones en MySQL ---
  Guardado T001 | CREDITO | $500000 -> impacto: 10000.0
  Guardado T002 | DEBITO | $80000 -> impacto: 1500.0
  Guardado T003 | CREDITO | $1200000 -> impacto: 24000.0
  Guardado T004 | DEBITO | $45000 -> impacto: 1500.0

Listo. La base de datos ahora tiene 4 transacciones.
```

> 🔎 ¿Por qué solo 4 y no 5? Porque `T005` tiene monto negativo: el **encapsulamiento**
> (el *setter* que valida) lo rechaza. El blindaje de POO protege lo que entra a la base. 💪

---

## Paso 4 — Lee la base de datos desde Python

```powershell
python conectar_db.py
```

---

## Paso 5 — Velo por dentro (opcional)

Puedes inspeccionar la tabla directamente desde el contenedor:

```powershell
docker exec -it empresa mysql -u root -p12345 -e "SELECT * FROM empresa_db.Transaccion;"
```

O con un visor gráfico como  **MySQL Workbench** conectándote a
`localhost:3306`, usuario `root`, contraseña `12345`.

---

## Resumen rápido (copiar y pegar)

```powershell
docker start empresa                 # enciende MySQL (o el docker run la 1a vez)
cd "MisProyectosPython\Semana_3\Mysql_Prisma"
pip install -r requirements.txt
prisma db push                       # crea empresa_db + la tabla + el cliente
python migrar_transacciones.py       # txt -> MySQL (usando las clases POO)
python conectar_db.py                # leer y mostrar
```

---

## Archivos de esta carpeta

| Archivo | Para qué sirve |
|---------|----------------|
| [`.env`](./.env) | Datos de conexión a MySQL (`DATABASE_URL`). |
| [`schema.prisma`](./schema.prisma) | Define el motor (MySQL) y la tabla `Transaccion`. |
| [`migrar_transacciones.py`](./migrar_transacciones.py) | Lee `../transacciones.txt` con las **clases POO** y lo guarda en MySQL. |
| [`conectar_db.py`](./conectar_db.py) | Conexión más simple posible: lee y muestra lo guardado. |
| [`requirements.txt`](./requirements.txt) | Dependencias: `prisma` y `python-dotenv`. |

---

## Problemas comunes

- **`Can't reach database server at localhost:3306` / Connection refused:** el contenedor no está
  corriendo o aún no terminó de arrancar. Ejecuta `docker start empresa` y espera ~15 segundos.

- **`Unknown database 'empresa_db'`:** te saltaste el **Paso 2** (`prisma db push`), que es quien
  crea la base. Si aun así falla, créala a mano:
  ```powershell
  docker exec -it empresa mysql -u root -p12345 -e "CREATE DATABASE IF NOT EXISTS empresa_db;"
  ```

- **`Environment variable not found: DATABASE_URL`:** corre los comandos **dentro** de la carpeta
  `Mysql_Prisma` (donde está el `.env`), o revisa que instalaste `python-dotenv`.

- **`prisma` no se reconoce / `spawn prisma-client-py ENOENT`:** el comando `prisma` quedó fuera
  del PATH. Encuentra su carpeta con:
  ```powershell
  python -c "import site, os; print(os.path.join(os.path.dirname(site.getusersitepackages()), 'Scripts'))"
  ```
  Agrégala al **Path** de tu usuario, cierra y reabre la terminal.

- **`pip install` falla por permisos (`Failed to write executable`):** instala a tu usuario:
  ```powershell
  pip install --user -r requirements.txt
  ```

- **Quiero empezar de cero (borrar TODO):**
  ```powershell
  docker rm -f empresa            # borra el contenedor
  docker volume rm mysql_datos    # borra los datos persistidos
  ```
  Luego repite desde el Paso 0.

---

## El hilo pedagógico

`transacciones.txt` → **mismas clases POO** (Encapsulamiento / Herencia / Polimorfismo) →
**Prisma** las guarda en un **servidor MySQL** que corre en **Docker** → las persistes en un
**volumen** y las consultas con SQL o un visor. El dato malo (`T005`) sigue siendo rechazado por
el encapsulamiento: ahora el blindaje de POO también protege una base de datos profesional.
