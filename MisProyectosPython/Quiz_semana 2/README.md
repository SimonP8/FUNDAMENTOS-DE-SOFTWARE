# Quiz 1 — Fundamentos de Software 🧩

¡Hora de poner en práctica lo aprendido! En este quiz vas a demostrar que dominas lo visto
hasta ahora: **Programación Estructurada** (funciones y lectura de archivos de texto) y los
fundamentos de **Programación Orientada a Objetos** (clase, objeto, constructor `__init__`,
`self`, atributos, métodos y listas de objetos).

---

## 🎯 El reto

Una cámara de comercio necesita un pequeño programa para analizar la información de varias
**empresas**. Cada empresa tiene estos datos:

| Atributo           | Ejemplo        |
|--------------------|----------------|
| nombre             | TechNova       |
| sector             | TECNOLOGIA     |
| num_empleados      | 150            |
| ingresos_anuales   | 500000000      |

Los registros están en el archivo **`empresas.txt`** (una empresa por línea):

```
TechNova,TECNOLOGIA,150,500000000
CasaBella,HOGAR,45,120000000
...
```

> ⚠️ **Ojo:** hay un registro "trampa" con `num_empleados` inválido (negativo). Tu programa
> debe **ignorar** las empresas con `num_empleados` menor o igual a 0 al leer el archivo.

---

## 🛠️ Qué debes implementar

Abre el archivo **`quiz_empresas.py`** y completa **todos los bloques marcados con `# TODO`**.
No necesitas crear nada desde cero: la estructura ya está, solo te falta la lógica.

### La clase `Empresa`
1. **`__init__(self, nombre, sector, num_empleados, ingresos_anuales)`** — guarda cada dato como
   atributo del objeto (`self.nombre = nombre`, etc.). Convierte `num_empleados` e
   `ingresos_anuales` a número con `int()`.
2. **`obtener_informacion(self)`** — devuelve un texto legible, por ejemplo:
   `TechNova | TECNOLOGIA | 150 empleados | $500000000`.

### Las funciones
3. **`leer_empresas(nombre_archivo)`** — lee el archivo y devuelve una **lista de objetos
   `Empresa`** (ignorando los registros inválidos).
4. **`calcular_total_ingresos(empresas)`** — devuelve la suma de los ingresos de todas las empresas.
5. **`filtrar_por_sector(empresas, sector)`** — devuelve una lista solo con las empresas de ese sector.
6. **`empresa_con_mas_empleados(empresas)`** — devuelve el objeto `Empresa` con más empleados.
7. **`promedio_empleados(empresas)`** — devuelve el promedio de empleados (cuidado con dividir entre cero).

---

## ✅ Salida esperada

Cuando completes todo y ejecutes `python quiz_empresas.py`, deberías ver algo así
(el registro inválido `EmpresaFantasma` **no** aparece):

```
--- Empresas registradas ---
TechNova | TECNOLOGIA | 150 empleados | $500000000
CasaBella | HOGAR | 45 empleados | $120000000
JugueLandia | JUGUETERIA | 30 empleados | $80000000
DataCorp | TECNOLOGIA | 320 empleados | $1200000000
MueblesSur | HOGAR | 80 empleados | $210000000
ElectroMax | TECNOLOGIA | 210 empleados | $750000000
ToyWorld | JUGUETERIA | 60 empleados | $150000000

Total de ingresos: 3010000000

--- Empresas del sector TECNOLOGIA ---
TechNova | TECNOLOGIA | 150 empleados | $500000000
DataCorp | TECNOLOGIA | 320 empleados | $1200000000
ElectroMax | TECNOLOGIA | 210 empleados | $750000000

Empresa con mas empleados: DataCorp | TECNOLOGIA | 320 empleados | $1200000000

Promedio de empleados: 127.86
```

---

## 📤 ¿Cómo entregar?

> 🎯 **La entrega es un repositorio PÚBLICO en GitHub.** No tienes que agregarme como
> colaborador ni subir archivos a Canvas: en Canvas solo pegas el **enlace** de tu repo.

### Paso 1 — Descarga el quiz
Clona el repositorio del curso y entra a la carpeta del quiz:

```bash
git clone https://github.com/SimonP8/FUNDAMENTOS-DE-SOFTWARE.git
cd "FUNDAMENTOS-DE-SOFTWARE/MisProyectosPython/Quiz_semana 2"
```

> 💡 También puedes hacerlo desde **VS Code**: pestaña *Source Control* → *Clone Repository*.

### Paso 2 — Resuelve
Completa los `# TODO` en `quiz_empresas.py` y ejecútalo hasta que la salida coincida con la
esperada. Documenta tu código con comentarios y docstrings.

### Paso 3 — Crea TU repositorio público
En GitHub crea un repositorio **nuevo** llamado **`quiz_semana2`** y marca la opción
**Public** (público). No agregues README ni .gitignore desde GitHub, para evitar conflictos.

Luego, desde la carpeta con tu solución:

```bash
git init
git add quiz_empresas.py empresas.txt
git commit -m "Quiz Semana 2 resuelto"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/quiz_semana2.git
git push -u origin main
```

> 💡 En VS Code: *Source Control* → **Publish to GitHub** → elige **Public repository**.

### Paso 4 — Verifica que sea público
Abre el enlace de tu repositorio en una **ventana de incógnito**. Si el código se ve sin
iniciar sesión, está público y listo para calificar. Si pide contraseña o dice *404*, aún
está privado: ve a **Settings → General → Danger Zone → Change visibility → Make public**.

### Paso 5 — Entrega en Canvas
En la tarea de Canvas pega el **enlace de tu repositorio público**, por ejemplo:

```
https://github.com/TU_USUARIO/quiz_semana2
```

Eso es todo: **el enlace es la entrega**.

---

## 📊 ¿Qué se evalúa?

- [ ] El **constructor** guarda correctamente los atributos (con `int()` donde corresponde).
- [ ] `leer_empresas` crea una **lista de objetos** e **ignora** el registro inválido.
- [ ] Las **funciones** devuelven los resultados correctos.
- [ ] El método `obtener_informacion` muestra los datos de forma clara.
- [ ] El código tiene **comentarios y docstrings** que explican tu solución.

¡Mucho éxito! Recuerda: ve de a un `# TODO` a la vez. 💪
