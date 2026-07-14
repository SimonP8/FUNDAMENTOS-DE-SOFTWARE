# QuantumCore-Python 🧠

Sistema de **gestión de transacciones** desarrollado a lo largo del curso
*Fundamentos de Software*. El proyecto crece semana a semana, aplicando buenas
prácticas de ingeniería de software:

- **POO** — Encapsulamiento, Herencia y Polimorfismo (Semana 3).
- **Robustez** — manejo de errores con `try/except` y tolerancia a datos corruptos (Semana 4).
- **Interoperabilidad** — serialización y deserialización con **JSON** (Semana 4).
- **Control de versiones** — Git y GitHub para el trabajo colaborativo (Semana 5).

---

## 👥 Autores

> Reemplacen esta lista con los integrantes del equipo:

- Nombre Apellido — usuario de GitHub
- Nombre Apellido — usuario de GitHub
- Nombre Apellido — usuario de GitHub

**Docente:** Simón Peláez · **Curso:** Fundamentos de Software

---

## 📁 Estructura del proyecto

```
MisProyectosPython/
├── Semana_2/    POO: clases, objetos y constructores (Venta / Transaccion)
├── Semana_3/    Pilares de POO (encapsulamiento, herencia, polimorfismo) + BD
├── Semana_4/    Robustez (try/except) y serialización JSON
├── Quiz_semana 2/ , Quiz_semana 3/   Retos evaluados
└── README.md    (este archivo)
```

---

## ▶️ Cómo ejecutar los ejemplos

Cada carpeta de semana tiene sus propios archivos `.py` y un archivo de datos `.txt`.
Por ejemplo, para la Semana 4:

```bash
cd Semana_4
python robustez_try_except.py     # lectura tolerante a fallos
python serializacion_json.py      # objeto <-> JSON
```

Algunos ejemplos requieren librerías; instálalas con:

```bash
pip install pandas openpyxl
```

---

## 🔧 Flujo de trabajo con Git (Semana 5)

Cada vez que avancemos en el proyecto:

```bash
git add .
git commit -m "Mensaje de lo que hicimos"
git push
```

> Este repositorio es **público** para poder ser evaluado. No subimos contraseñas ni
> archivos sensibles (ver `.gitignore`).
