# entornos_proyecto

Proyecto de prácticas con Python: incluye ejemplos de entrada y salida, operaciones
matemáticas y scraping de una página de demostración.

## Contenido

- `first_script.py`: imprime un mensaje inicial y contiene notas sobre la práctica de
  entornos virtuales y librerías.
- `saludo.py`: solicita el nombre, muestra un saludo y usa NumPy para imprimir un
  arreglo de diez ceros.
- `calculadora.py`: recibe dos números y una operación (`+`, `-`, `*` o `/`), muestra
  el resultado y maneja entradas numéricas inválidas, operadores no válidos y la
  división por cero.
- `scraping.py`: descarga la página configurada, analiza su HTML con Beautiful Soup
  e imprime las citas y sus autores. Informa errores HTTP o de conexión y avisa si no
  encuentra citas.
- `config_reader.py`: lee y valida la configuración del scraper y del administrador
  de estudiantes desde `config.json`.
- `config.json`: define la URL utilizada por el scraper y la configuración de
  estudiantes: archivo Excel, columnas, cursos permitidos y rango de notas.
- `estudiantes.py`: permite crear, consultar, buscar y actualizar notas de estudiantes
  en un archivo Excel usando pandas. El archivo `estudiantes.xlsx` se crea
  automáticamente junto al script si aún no existe.

El scraper busca elementos HTML con los selectores `.quote`, `.text` y `.author`, por
lo que su extracción está pensada para el sitio de demostración indicado.

## Requisitos

- Python 3.9 o posterior.
- `numpy`, utilizado por `saludo.py`.
- `pandas` y `openpyxl`, utilizados para administrar el archivo Excel de estudiantes.
- `beautifulsoup4`, utilizado por `scraping.py`.

## Instalación

Desde la carpeta del proyecto, crea y activa un entorno virtual e instala las
dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy pandas openpyxl beautifulsoup4
```

En Windows PowerShell, activa el entorno con:

```powershell
.venv\Scripts\Activate.ps1
```

## Ejecución

Con el entorno virtual activado, ejecuta cualquiera de los ejemplos:

```bash
python first_script.py
python saludo.py
python calculadora.py
python scraping.py
python estudiantes.py
```

El administrador de estudiantes ofrece opciones para ver la tabla, agregar un
estudiante, buscar por ID y actualizar su nota. Los cursos permitidos y el rango de
notas se leen de `config.json`; los cambios se guardan en el archivo Excel indicado
allí.

Para cambiar el sitio que consulta el scraper, modifica el valor de `url` en
`config.json`. La página debe ofrecer contenido compatible con los selectores que usa
`scraping.py`.
