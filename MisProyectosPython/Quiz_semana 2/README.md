# Quiz 1 — Fundamentos de Programación 🧩

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

### Paso 3 — Sube tu solución
Tal como practicamos en clase, crea **tu propio repositorio privado** en GitHub y sube tu
carpeta resuelta.

### Paso 4 — Dame acceso para revisar
Como tu repositorio es **privado**, agrégame como colaborador para poder calificarlo:
- En tu repo: **Settings → Collaborators → Add people**
- Usuario de GitHub: **`SimonP8`** · o invítame al correo **`Simonpelaez.loaiza@gmail.com`**

### Paso 5 - Entrega del quiz en canvas
En la plataforma canvas sube un documento donde se evidencia el 
---

## 📊 ¿Qué se evalúa?

- [ ] El **constructor** guarda correctamente los atributos (con `int()` donde corresponde).
- [ ] `leer_empresas` crea una **lista de objetos** e **ignora** el registro inválido.
- [ ] Las **funciones** devuelven los resultados correctos.
- [ ] El método `obtener_informacion` muestra los datos de forma clara.
- [ ] El código tiene **comentarios y docstrings** que explican tu solución.

¡Mucho éxito! Recuerda: ve de a un `# TODO` a la vez. 💪
