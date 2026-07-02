# Quiz Semana 3 — Pilares de POO (leyendo desde Excel) 🧩

En este quiz demuestras que dominas los **tres pilares de la POO** que vimos esta semana:
**Encapsulamiento** (getters/setters con validación), **Herencia** (clase base y clases hijas)
y **Polimorfismo** (un mismo método con comportamiento distinto).

**Novedad de este quiz:** los datos vienen de un **archivo de Excel** (`empleados.xlsx`) con
varias columnas. La **lectura del Excel ya está lista** (y es robusta): tú te concentras en la
POO y en un pequeño reto de creatividad. 🚀

> Este quiz es **solo de POO**. No incluye bases de datos: eso lo exploramos aparte.

---

## 🎯 El reto

Una empresa tiene su nómina en un Excel con estas columnas:

| id | nombre | tipo | salario_base | ciudad | departamento | fecha_ingreso | correo |
|----|--------|------|--------------|--------|--------------|---------------|--------|

Solo usaremos **nombre**, **tipo**, **salario_base** y **ciudad**; las demás columnas están
"por si acaso" (y para que veas que un buen lector **ignora lo que no necesita**).

Hay dos tipos de empleado y cada uno **cobra distinto** (polimorfismo):
- **PLANTA:** salario base **+ 30 %** de prestaciones.
- **CONTRATISTA:** **solo** su salario base.

> ⚠️ El Excel trae filas "trampa": una con salario **negativo** y otra **sin nombre**. La
> lectura ya las descarta sola (robustez con `try/except` y validación).

---

## 🛠️ Qué debes hacer

Instala primero las librerías para leer Excel (una sola vez):

```bash
pip install -r requirements.txt
```

Abre **`quiz_nomina.py`** y completa **todos los bloques `# TODO`**:

1. **Encapsulamiento** — en `EmpleadoBase`: guarda `_salario_base` (privado), crea el *getter*
   `@property` y el *setter* con validación (no permite negativos).
2. **Herencia** — `EmpleadoPlanta` y `EmpleadoContratista` heredan de `EmpleadoBase`.
3. **Polimorfismo** — sobreescribe `calcular_pago()` en cada clase hija.
4. Completa `crear_empleado()` y `obtener_informacion()`.

> 📌 **La función `leer_empleados_excel()` YA ESTÁ HECHA.** No la modifiques: es tu ejemplo de
> lectura robusta de un Excel.

### ✨ Reto extra (obligatorio): crea TU PROPIA función
Al final del archivo verás la función `mi_funcion(empleados)`. **Invéntate una función útil**
que trabaje con la lista de empleados. Algunas ideas (elige una o propón la tuya):
- `salario_promedio(empleados)` → promedio de salario base.
- `empleados_por_ciudad(empleados, ciudad)` → cuántos hay en esa ciudad.
- `empleado_mejor_pagado(empleados)` → el de mayor `calcular_pago()`.

Documéntala con un *docstring* y **llámala dentro de `ejecutar_quiz()`** para mostrar su resultado.

---

## ✅ Salida esperada (ejemplo)

Al ejecutar `python quiz_nomina.py` (con las clases completas) verás algo como esto — las filas
inválidas **no** aparecen:

```
  [Aviso] Se ignoro Sofia: El salario no puede ser negativo.
  [Aviso] Fila incompleta ignorada.
--- Nomina ---
Ana | EmpleadoPlanta | Medellin | base $3000000 -> pago: 3900000.0
Luis | EmpleadoContratista | Bogota | base $2500000 -> pago: 2500000
Marta | EmpleadoPlanta | Medellin | base $4200000 -> pago: 5460000.0
Carlos | EmpleadoContratista | Cali | base $1800000 -> pago: 1800000
Diego | EmpleadoPlanta | Medellin | base $3500000 -> pago: 4550000.0
Valentina | EmpleadoContratista | Bogota | base $2800000 -> pago: 2800000
```

(El resultado de tu función-reto dependerá de lo que decidas crear.)

---

## 📤 ¿Cómo entregar?

### Paso 1 — Actualiza el repositorio del curso
Ya tienes clonado el repo del curso. Tráete lo nuevo (esta carpeta del quiz):

```bash
git pull
cd "MisProyectosPython/Quiz_semana 3"
```

> 💡 En VS Code también puedes usar la pestaña *Source Control* → sincronizar (pull).

### Paso 2 — Resuelve
Instala las librerías, completa los `# TODO`, crea tu función y ejecuta hasta que la salida
coincida con la esperada. Documenta tu código con comentarios y docstrings.

### Paso 3 — Presenta tu solución en un repositorio APARTE
Crea un repositorio **nuevo** en GitHub llamado **`quiz_semana3`** y sube tu solución:

```bash
git init
git add quiz_nomina.py empleados.xlsx requirements.txt
git commit -m "Quiz Semana 3 resuelto"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/quiz_semana3.git
git push -u origin main
```

### Paso 4 — Dame acceso / comparte el enlace
- Si el repo es **privado**: **Settings → Collaborators → Add people** e invita a **`SimonP8`**
  (o a **`Simonpelaez.loaiza@gmail.com`**).
- Si es **público**: comparte el enlace del repositorio.

### Paso 5 — Entrega en Canvas
Sube en Canvas un documento con el **enlace a tu repositorio `quiz_semana3`** como evidencia.

---

## 📊 ¿Qué se evalúa?

- [ ] **Encapsulamiento:** atributo privado + getter `@property` + setter que valida.
- [ ] **Herencia:** las dos clases hijas heredan de `EmpleadoBase`.
- [ ] **Polimorfismo:** `calcular_pago()` da un resultado distinto por tipo.
- [ ] **Tu propia función:** creada, documentada y usada en `ejecutar_quiz()`.
- [ ] Código con **comentarios y docstrings** claros.

¡Éxitos! Recuerda: un `# TODO` a la vez. 💪
