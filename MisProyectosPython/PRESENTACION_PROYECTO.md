# 🎤 Guía para presentar el proyecto — Quantum Core (Estación final)

> 🎯 **La meta es que el proyecto se vea CORRIENDO en un equipo.** Las diapositivas y los
> diagramas suman, pero lo que se evalúa es el **sistema funcionando de principio a fin**.

El proyecto es la carpeta **[`Proyecto_Completo/`](./Proyecto_Completo/README.md)**: una
aplicación full-stack de tres capas independientes.

```
FRONTEND (React, :5173)  ⇄ HTTP/JSON ⇄  BACKEND (Flask, :5000)  ⇄ Prisma ⇄  MySQL (Docker, :3306)
```

👉 Los pasos técnicos para levantarlo están en
[`Proyecto_Completo/README.md`](./Proyecto_Completo/README.md). Esta guía es para **explicarlo**.

---

## 0. Cómo se entrega

**Se entregan dos cosas:**

| Entregable | Dónde | Qué debe tener |
|---|---|---|
| 📦 **El repositorio** | Enlace a GitHub | Todo el código del proyecto (BACKEND + FRONTEND) y el historial de commits. |
| 📄 **Documento del sistema** | Se sube en **Canvas** | Descripción del sistema, su arquitectura y cómo ejecutarlo. |

**Y se sustenta:** la presentación es de **formato libre** — como más les guste y mejor cuente su
trabajo:

- 🖥️ Diapositivas
- 💻 Explicando el código en vivo
- 🎥 Un video
- 📐 Diagramas (UML, arquitectura)
- …o una mezcla de todo

> ⚠️ Lo único **imprescindible** es que al final el **sistema esté funcionando**.

---

## 1. Antes de presentar (checklist de 5 minutos)

- [ ] Docker Desktop **abierto** y contenedor encendido: `docker start empresa`.
- [ ] Backend corriendo (`python app.py`) y respondiendo en `http://localhost:5000/api/transacciones/`.
- [ ] Frontend corriendo (`npm run dev`) en `http://localhost:5173`.
- [ ] Tres terminales abiertas y visibles (base de datos, backend, frontend).
- [ ] El repositorio de GitHub abierto en una pestaña.

> 💡 Ensaya el arranque **una vez** antes. Si algo falla en vivo, saber dónde mirar
> (¿está el contenedor arriba? ¿corriste `prisma db push`?) es parte de ser ingeniero.

---

## 2. Guion sugerido (5–8 minutos)

| Momento | Qué muestras | Qué dices |
|---|---|---|
| **Intro (30 s)** | El diagrama de arquitectura | "Quantum Core es un sistema de transacciones de 3 capas: una interfaz en React, una API en Flask y una base de datos MySQL en Docker. Son tres procesos independientes." |
| **Base de datos** | La terminal con `docker start empresa` | "La base de datos corre **en un contenedor Docker local**, no está instalada en mi equipo. El volumen conserva los datos aunque borre el contenedor." |
| **Backend** | `http://localhost:5000/api/transacciones/` | "Esta es la API REST. Responde en **JSON** (Semana 4). Está organizada en capas: *routes* recibe la petición, *controllers* valida y decide, *models* habla con la base de datos. Cada capa tiene **una sola responsabilidad** (SRP)." |
| **Validación** | Intenta crear una transacción con monto negativo | "El sistema **la rechaza**: es el mismo encapsulamiento del *setter* de la Semana 3, ahora en el controller, con `try/except` para no caerse (Semana 4)." |
| **Frontend** | El CRUD en el navegador | "Desde aquí creo, edito y elimino. El navegador nunca habla con la base de datos: solo con la API." |
| **Persistencia** | Recarga la página / consulta MySQL | "Los datos siguen ahí: eso es **persistencia real**, no memoria." |
| **Cierre** | El repositorio en GitHub | "Todo está versionado con Git (Semana 5) y el diseño documentado con UML (Semana 6)." |

---

## 3. Qué del núcleo demuestras (y dónde señalarlo)

| Concepto | Dónde está en el proyecto |
|---|---|
| POO y **encapsulamiento** | `controllers/transaccion_controller.py` — valida que el monto no sea negativo |
| **Persistencia** (Prisma + MySQL en Docker) | `BACKEND/schema.prisma` y `models/transaccion_model.py` |
| **try/except** (robustez) | Cada función del controller responde 400/404 en vez de caerse |
| **JSON** (serialización) | Toda respuesta del backend; el frontend la consume con `fetch()` |
| **Git / GitHub** | Historial de commits y ramas del repositorio |
| **Arquitectura en capas / SRP + UML** | `routes → controllers → models` y el diagrama de clases |

---

## 4. Preguntas que te pueden hacer

- **¿Por qué separar frontend y backend?** Para que cada uno evolucione sin romper al otro; lo
  único que los une es el contrato de la API. Si mañana hacemos una app móvil, el backend no cambia.
- **¿Por qué Docker para la base de datos?** Para levantar MySQL en segundos, igual en cualquier
  equipo, sin instalarlo en el sistema operativo. El volumen guarda los datos.
- **¿Qué pasa si llega un dato inválido?** El controller lo valida y responde un error claro
  (400) sin tumbar el servidor.
- **¿Dónde está la POO?** En la validación y en el modelado de la entidad `Transaccion`; el UML
  documenta esa estructura.
- **Si se cae la base de datos, ¿qué pasa?** El backend responde con un error controlado; la app
  no revienta.

---

## 5. 💼 Valor adicional: tu portafolio

Este proyecto es la primera pieza seria de tu portafolio profesional:

- Súbelo a **GitHub** con un README claro: arquitectura, cómo ejecutarlo y **capturas**.
- **Fija (pin)** el repositorio en tu perfil.
- Es evidencia real de: POO · manejo de errores · JSON · MySQL · Docker · API REST · React · Git.
- En una entrevista podrás decir *"construí una app full-stack con API REST y MySQL sobre
  Docker"* — **y mostrarla funcionando**.
