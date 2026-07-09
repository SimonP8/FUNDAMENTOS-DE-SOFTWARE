# Proyecto Completo — CRUD de Transacciones (Backend + Frontend + Base de Datos)

Después de tres semanas construyendo piezas sueltas (POO, persistencia con Prisma, manejo de
errores y JSON), aquí las juntamos todas en un **proyecto real de tres capas que se comunican por
red**, tal como funciona una aplicación web de verdad:

```
┌─────────────────┐        HTTP / JSON        ┌───────────────────────┐        Prisma        ┌──────────────────┐
│   FRONTEND       │  ───────────────────────► │   BACKEND              │ ───────────────────► │  BASE DE DATOS     │
│ React + Vite     │  ◄─────────────────────── │ Flask (routes →        │ ◄─────────────────── │  MySQL (Docker)    │
│ + Tailwind CSS   │       fetch()             │ controllers → models)  │                       │  contenedor        │
│ puerto 5173      │                            │ puerto 5000            │                       │  "empresa"         │
└─────────────────┘                            └───────────────────────┘                       └──────────────────┘
```

**Punto clave: son tres procesos completamente independientes.** No es un monolito: cada uno se
enciende, se apaga y se revisa por separado, en su propia terminal.

- **`BACKEND/`** — servidor Flask con arquitectura en capas (`routes` → `controllers` →
  `models`) que expone la tabla `Transaccion` como una API REST. Ver
  [`BACKEND/README.md`](BACKEND/README.md).
- **`FRONTEND/`** — aplicación React (Vite + Tailwind) que consume esa API y permite hacer el
  CRUD completo desde el navegador. Ver [`FRONTEND/README.md`](FRONTEND/README.md).
- **Base de datos** — la misma base MySQL creada en la
  [Semana 3 (`Mysql_Prisma`)](../Semana_3/Mysql_Prisma/README.md): mismo contenedor Docker
  `empresa`, misma base `empresa_db`, mismas 4 transacciones ya migradas (`T001`–`T004`). No se
  crea nada nuevo: este proyecto **reutiliza** esa base de datos.

---

## El hilo pedagógico

| Semana | Qué aprendimos | Dónde vive aquí |
|---|---|---|
| Semana 3 | POO: encapsulamiento, herencia, polimorfismo | La validación de `monto` en `controllers/transaccion_controller.py` es el mismo blindaje |
| Semana 3 | Persistencia con Prisma (SQLite y MySQL en Docker) | `BACKEND/schema.prisma` reutiliza literalmente la base de MySQL |
| Semana 4 | `try/except` para tolerar errores | Cada función de `controllers/` atrapa errores y responde con un mensaje claro |
| Semana 4 | Serialización a JSON | Cada respuesta del backend es JSON; el frontend la consume con `fetch` |
| **Ahora** | **Arquitectura en capas + integración full-stack** | Todo `Proyecto_Completo/` |

---

## Prerrequisitos (instalar una sola vez)

| Herramienta | Para qué | Descarga | Verificar instalación |
|---|---|---|---|
| **Python 3** | Correr el backend (Flask) | <https://www.python.org/downloads/> | `python --version` |
| **Node.js (LTS)** | Correr el frontend (React + Vite) | <https://nodejs.org/> | `node -v` y `npm -v` |
| **Docker Desktop** | Correr la base de datos MySQL | <https://www.docker.com/products/docker-desktop/> | `docker -v` |

> El contenedor `empresa` ya se creó en la Semana 3. Si es la primera vez que trabajas en esta
> máquina, sigue primero el [README de `Mysql_Prisma`](../Semana_3/Mysql_Prisma/README.md) para
> crearlo.

---

## Cómo encender todo (en este orden, cada uno en su propia terminal)

### 1. Base de datos

```powershell
docker start empresa
```

Espera unos 10-20 segundos a que MySQL esté listo.

### 2. Backend (terminal aparte)

```powershell
cd "MisProyectosPython\Proyecto_Completo\BACKEND"
pip install -r requirements.txt
prisma db push
python app.py
```

Déjalo corriendo. Verifica en el navegador o con `curl`: <http://localhost:5000/api/transacciones/>

### 3. Frontend (otra terminal aparte)

```powershell
cd "MisProyectosPython\Proyecto_Completo\FRONTEND"
npm install
npm run dev
```

Abre <http://localhost:5173> — ahí verás la tabla con las transacciones y el formulario para
crear, editar y eliminar.

---

## ¿Por qué separarlo así y no todo junto?

Es la forma en que se construyen las aplicaciones web reales: el equipo de backend puede cambiar
de Flask a otra cosa sin tocar una sola línea de React, y el equipo de frontend puede cambiar
todo el diseño sin tocar una sola línea de Python. Lo único que los conecta es el **contrato**: la
lista de endpoints REST documentada en [`BACKEND/README.md`](BACKEND/README.md). Si mañana se
reemplaza el frontend por una app de celular, el backend no se entera ni cambia.

---

## Resumen ultra-rápido (3 terminales, copiar y pegar)

```powershell
# Terminal 1
docker start empresa

# Terminal 2
cd "MisProyectosPython\Proyecto_Completo\BACKEND"
pip install -r requirements.txt
prisma db push
python app.py

# Terminal 3
cd "MisProyectosPython\Proyecto_Completo\FRONTEND"
npm install
npm run dev
```

Luego abre <http://localhost:5173> en el navegador. 🎉
