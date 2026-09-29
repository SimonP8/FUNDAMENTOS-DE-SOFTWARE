# Proyecto Completo — CRUD de Transacciones (Frontend + Backend + Base de Datos)

Aquí se juntan todas las piezas del núcleo en **un proyecto real de tres capas que se comunican
por red**, tal como funciona una aplicación web de verdad:

```
┌──────────────────┐      HTTP / JSON      ┌────────────────────────┐        Prisma        ┌────────────────────┐
│    FRONTEND      │ ────────────────────► │        BACKEND         │ ───────────────────► │   BASE DE DATOS    │
│  React + Vite    │ ◄──────────────────── │  Flask (routes →       │ ◄─────────────────── │   MySQL en Docker  │
│  + Tailwind CSS  │       fetch()         │  controllers → models) │                      │  contenedor        │
│   puerto 5173    │                       │      puerto 5000       │                      │  "empresa" · 3306  │
└──────────────────┘                       └────────────────────────┘                      └────────────────────┘
```

**Punto clave: son tres procesos independientes.** No es un monolito: cada uno se enciende, se
apaga y se revisa por separado, **en su propia terminal**. Vas a necesitar **3 terminales
abiertas al mismo tiempo**.

---

## Antes de empezar (instalar una sola vez)

| Herramienta | Para qué | Descarga | Comprobar que quedó bien |
|---|---|---|---|
| **Docker Desktop** | La base de datos MySQL | <https://www.docker.com/products/docker-desktop/> | `docker -v` |
| **Python 3** | El backend (Flask) | <https://www.python.org/downloads/> | `python --version` |
| **Node.js (LTS)** | El frontend (React + Vite) | <https://nodejs.org/> | `node -v` y `npm -v` |

> **Docker Desktop tiene que estar ABIERTO**, no solo instalado. Si la ballena del icono no está,
> los comandos `docker` van a fallar con *"error during connect"*.

---

# Paso 1 · Base de datos (Terminal 1)

## 1.1 — La primera vez: CREAR el contenedor

Este comando descarga MySQL, crea el contenedor `empresa` y **crea la base `empresa_db` vacía**.
Cópialo completo, en una sola línea:

```powershell
docker run --name empresa -e MYSQL_ROOT_PASSWORD=12345 -e MYSQL_DATABASE=empresa_db -p 3306:3306 -v mysql_datos:/var/lib/mysql -d mysql:8
```

Qué hace cada parte:

| Parte | Para qué sirve |
|---|---|
| `--name empresa` | El nombre del contenedor. Así lo prendes y apagas después. |
| `-e MYSQL_ROOT_PASSWORD=12345` | Usuario **root** con contraseña **12345**. |
| `-e MYSQL_DATABASE=empresa_db` | **Crea la base de datos automáticamente** al arrancar. |
| `-p 3306:3306` | Publica el puerto para que tu PC pueda conectarse. |
| `-v mysql_datos:/var/lib/mysql` | **Persistencia**: los datos viven en un volumen y sobreviven aunque borres el contenedor. |
| `-d mysql:8` | Lo deja corriendo en segundo plano, con la imagen MySQL 8. |

> La primera vez tarda unos minutos porque descarga la imagen de MySQL (~600 MB).

## 1.2 — Las siguientes veces: solo ENCENDERLO

**No repitas el `docker run`.** Si lo haces, dará error `name is already in use`. A partir de
ahora solo:

```powershell
docker start empresa     # encender
docker stop empresa      # apagar al terminar
```

## 1.3 — Comprobar que quedó lista

MySQL tarda unos segundos en arrancar aunque el contenedor ya aparezca "Up". Espera y verifica:

```powershell
docker ps
```

Debe aparecer `empresa` con estado `Up` y el puerto `0.0.0.0:3306->3306/tcp`.

Para estar seguro de que MySQL ya acepta conexiones:

```powershell
docker exec empresa mysqladmin ping -uroot -p12345
```

Cuando responda **`mysqld is alive`**, puedes seguir. (Suele tardar entre 5 y 30 segundos.)

---

# Paso 2 · Backend (Terminal 2 — nueva terminal)

```powershell
cd "MisProyectosPython\Proyecto_Completo\BACKEND"
pip install -r requirements.txt
prisma db push
python app.py
```

Qué hace cada comando:

1. **`pip install -r requirements.txt`** — instala Flask, flask-cors, prisma y python-dotenv.
2. **`prisma db push`** — lee `schema.prisma`, crea las tablas `Transaccion` y `Usuario` dentro
   de `empresa_db`, y genera el cliente de Prisma que usa Python.
3. **`python app.py`** — levanta la API en el puerto 5000. **Deja esta terminal abierta**: si la
   cierras, el backend se apaga.

### Comprobar que quedó bien

Debes ver en la terminal:

```
 * Running on http://127.0.0.1:5000
```

Y al abrir <http://localhost:5000/api/transacciones/> en el navegador debe responder **JSON**
(`[]` si la base está vacía, o la lista de transacciones).

> **Si `prisma` no funciona** (`'prisma' no se reconoce como un comando`), usa la forma larga,
> que siempre sirve:
> ```powershell
> python -m prisma db push
> ```

---

# Paso 3 · Frontend (Terminal 3 — otra terminal más)

```powershell
cd "MisProyectosPython\Proyecto_Completo\FRONTEND"
npm install
npm run dev
```

### Comprobar que quedó bien

Vite te va a mostrar algo así:

```
  VITE v8.1.4  ready in 622 ms

  ➜  Local:   http://localhost:5173/
```

Abre ese enlace. Deberías ver el título **"CRUD de Transacciones"**, el formulario y la tabla con
los datos que vienen de MySQL.

> **Ojo con el puerto.** Si el 5173 ya está ocupado por otra cosa, Vite **se cambia solo** a 5174
> y lo avisa con *"Port 5173 is in use, trying another one..."*. Usa **siempre el enlace que
> aparece en tu terminal**, no el que dice este README.

---

## Resumen para copiar y pegar (3 terminales)

```powershell
# ── Terminal 1: base de datos ──
docker start empresa
# (la PRIMERA vez de todas, en vez del start, usa el docker run del Paso 1.1)

# ── Terminal 2: backend ──
cd "MisProyectosPython\Proyecto_Completo\BACKEND"
pip install -r requirements.txt
prisma db push
python app.py

# ── Terminal 3: frontend ──
cd "MisProyectosPython\Proyecto_Completo\FRONTEND"
npm install
npm run dev
```

Luego abre <http://localhost:5173> 🎉

**El orden importa:** primero la base de datos, después el backend, y de último el frontend. Si
levantas el backend sin la base encendida, no podrá conectarse.

---

## Si algo falla

| Lo que ves | Qué pasó | Cómo se arregla |
|---|---|---|
| `error during connect` / `docker daemon is not running` | Docker Desktop está cerrado | Ábrelo y espera a que el icono deje de moverse |
| `The container name "/empresa" is already in use` | Ya lo creaste antes | Usa `docker start empresa` en vez del `docker run` |
| `port is already allocated` (3306) | Tienes otro MySQL corriendo en el PC | Apaga el otro MySQL, o cambia el puerto a `-p 3307:3306` (y ajusta el `.env`) |
| `Can't connect to MySQL server` al hacer `prisma db push` | MySQL todavía está arrancando | Espera y verifica con `docker exec empresa mysqladmin ping -uroot -p12345` |
| `'prisma' no se reconoce como un comando` | La carpeta de scripts de Python no está en el PATH | Usa `python -m prisma db push` |
| La página carga pero la tabla sale vacía y hay error en consola | El backend no está corriendo | Revisa la Terminal 2; prueba <http://localhost:5000/api/transacciones/> |
| `Failed to fetch` en el navegador | El backend se cayó o se cerró la terminal | Vuelve a ejecutar `python app.py` |
| Vite abrió en 5174 y no en 5173 | El 5173 estaba ocupado | Usa el enlace que dice tu terminal |
| `No se puede enlazar el parámetro 'Headers'` al usar curl | En PowerShell `curl` es un alias de `Invoke-WebRequest` | Usa `Invoke-RestMethod` (ver sección de la API) |

### Para ver los datos por dentro de MySQL

Útil para mostrar que el dato **sí quedó guardado**:

```powershell
docker exec empresa mysql -uroot -p12345 empresa_db -e "SELECT * FROM Transaccion;"
```

---

## La API del backend (el "contrato" con el frontend)

| Método | Ruta | Qué hace | Respuesta |
|---|---|---|---|
| GET | `/api/transacciones/` | Lista todas | `200` |
| GET | `/api/transacciones/<id>` | Obtiene una | `200` · `404` si no existe |
| POST | `/api/transacciones/` | Crea una | `201` · `400` si el monto es negativo |
| PUT | `/api/transacciones/<id>` | Actualiza | `200` · `400` si el monto es negativo |
| DELETE | `/api/transacciones/<id>` | Elimina | `200` |

El cuerpo (body) en JSON para crear o actualizar:

```json
{ "codigo": "T010", "tipo": "CREDITO", "monto": 500000, "impacto": 10000 }
```

### Probar la API sin el frontend

> **Importante:** en PowerShell, `curl` **no es el curl de verdad**: es un alias de
> `Invoke-WebRequest`, así que `curl -X POST -H ... -d ...` **falla**. Usa los comandos nativos
> de PowerShell que están abajo. (En Git Bash o CMD sí funciona el `curl` normal.)

```powershell
# Listar todas
Invoke-RestMethod -Uri http://localhost:5000/api/transacciones/

# Crear una
Invoke-RestMethod -Uri http://localhost:5000/api/transacciones/ -Method Post `
  -ContentType "application/json" `
  -Body '{"codigo":"T010","tipo":"CREDITO","monto":500000,"impacto":10000}'

# Eliminar la número 3
Invoke-RestMethod -Uri http://localhost:5000/api/transacciones/3 -Method Delete
```

**La validación en acción** (monto negativo). Como PowerShell corta la ejecución con los
errores HTTP, envuélvelo en `try/catch` para ver el mensaje:

```powershell
try {
  Invoke-RestMethod -Uri http://localhost:5000/api/transacciones/ -Method Post `
    -ContentType "application/json" `
    -Body '{"codigo":"MALO","tipo":"CREDITO","monto":-500,"impacto":0}'
} catch {
  $_.ErrorDetails.Message
}
```

Responde `{"error": "El monto no puede ser negativo"}` con código **HTTP 400** — es **el mismo
blindaje del setter de la Semana 3**, ahora hablando HTTP.

> La forma más fácil de mostrar esto en clase es desde el propio frontend: escribe un monto
> negativo en el formulario y mira la respuesta.

---

## Qué del núcleo vive en este proyecto

| Semana | Qué aprendimos | Dónde está aquí |
|---|---|---|
| Semana 2 | Clases y objetos | Cada transacción es un objeto con sus atributos |
| Semana 3 | Encapsulamiento y validación | `controllers/transaccion_controller.py` rechaza el monto negativo |
| Semana 3 | SRP (responsabilidad única) | Las carpetas `routes/`, `controllers/` y `models/` |
| Semana 4 | `try/except` | Cada función del controlador atrapa el error y responde el código correcto |
| Semana 4 | Serialización JSON | Toda respuesta del backend es JSON; el frontend la lee con `fetch()` |
| Semana 5 | Git y GitHub | El repositorio con su historial de commits |
| Semana 6 | UML | El diagrama de clases documenta esta arquitectura |
| Semana 7 | Base de datos y CRUD | `schema.prisma` define las tablas; `models/` hace el CRUD |

---

## Cómo está organizado

```
Proyecto_Completo/
├── BACKEND/                        La API en Python + Flask
│   ├── app.py                      Punto de entrada: arranca Flask y registra las rutas
│   ├── db.py                       Conexión única a la base de datos vía Prisma
│   ├── schema.prisma               El modelo de datos: se traduce a tablas MySQL
│   ├── .env                        DATABASE_URL (usuario, clave, puerto, base)
│   ├── routes/                     CAPA 1 · recibe la petición y la dirige
│   │   └── transaccion_routes.py
│   ├── controllers/                CAPA 2 · valida y aplica las reglas de negocio
│   │   └── transaccion_controller.py
│   └── models/                     CAPA 3 · lo único que le habla a la base de datos
│       └── transaccion_model.py
└── FRONTEND/                       La interfaz en React + Vite
    └── src/
        ├── pages/Transacciones.jsx La pantalla: formulario y tabla
        ├── api/transacciones.js    Todos los fetch() al backend, en un solo sitio
        └── App.jsx                 Arma la aplicación
```

Esas tres carpetas del backend (`routes`, `controllers`, `models`) no son una organización
caprichosa: son el **SRP de la Semana 3** aplicado a nivel de carpetas. Cada una tiene **una sola
razón para cambiar**.

---

## Al terminar la clase

```powershell
docker stop empresa
```

En las terminales del backend y del frontend, `Ctrl + C`.

Los datos **no se pierden**: viven en el volumen `mysql_datos`. La próxima vez, `docker start
empresa` y todo sigue ahí.
