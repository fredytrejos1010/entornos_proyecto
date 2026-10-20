from pathlib import Path

import pandas as pd

from config_reader import load_student_config

CONFIG = load_student_config()
ARCHIVO = Path(__file__).with_name(CONFIG["file"])
COLUMNAS = CONFIG["columns"]
CURSOS = CONFIG["courses"]
NOTA_MIN = CONFIG["grade_min"]
NOTA_MAX = CONFIG["grade_max"]


def cargar_estudiantes() -> pd.DataFrame:
    if not ARCHIVO.exists():
        estudiantes = pd.DataFrame(columns=COLUMNAS)
        estudiantes.to_excel(ARCHIVO, index=False)
        return estudiantes

    estudiantes = pd.read_excel(ARCHIVO, dtype={"id": "string"})
    faltantes = set(COLUMNAS) - set(estudiantes.columns)
    if faltantes:
        raise ValueError(f"Al Excel le faltan estas columnas: {', '.join(sorted(faltantes))}")

    return estudiantes[COLUMNAS]


def guardar_estudiantes(estudiantes: pd.DataFrame) -> None:
    estudiantes.to_excel(ARCHIVO, index=False)


def mostrar_estudiantes(estudiantes: pd.DataFrame) -> None:
    if estudiantes.empty:
        print("Todavía no hay estudiantes registrados.")
    else:
        print(estudiantes.to_string(index=False))


def agregar_estudiante(estudiantes: pd.DataFrame) -> pd.DataFrame:
    identificacion = input("ID del estudiante: ").strip()
    if not identificacion:
        print("El ID no puede estar vacío.")
        return estudiantes
    if estudiantes["id"].astype("string").eq(identificacion).any():
        print("Ya existe un estudiante con ese ID.")
        return estudiantes

    nombre = input("Nombre: ").strip()
    print(f"Cursos disponibles: {', '.join(CURSOS)}")
    curso_ingresado = input("Curso: ").strip()
    curso = next((opcion for opcion in CURSOS if opcion.casefold() == curso_ingresado.casefold()), "")
    if not nombre or not curso:
        print("El nombre no puede estar vacío y el curso debe estar en la lista.")
        return estudiantes

    try:
        edad = int(input("Edad: "))
        nota = float(input(f"Nota (de {NOTA_MIN:g} a {NOTA_MAX:g}): "))
        if edad <= 0 or not NOTA_MIN <= nota <= NOTA_MAX:
            raise ValueError
    except ValueError:
        print(
            f"Edad o nota inválida. La edad debe ser positiva y la nota estar "
            f"entre {NOTA_MIN:g} y {NOTA_MAX:g}."
        )
        return estudiantes

    nuevo = pd.DataFrame(
        [{"id": identificacion, "nombre": nombre, "edad": edad, "curso": curso, "nota": nota}]
    )
    estudiantes = pd.concat([estudiantes, nuevo], ignore_index=True)
    guardar_estudiantes(estudiantes)
    print("Estudiante guardado.")
    return estudiantes


def buscar_estudiante(estudiantes: pd.DataFrame) -> None:
    identificacion = input("ID que deseas buscar: ").strip()
    resultado = estudiantes[estudiantes["id"].astype("string").eq(identificacion)]
    mostrar_estudiantes(resultado)


def actualizar_nota(estudiantes: pd.DataFrame) -> pd.DataFrame:
    identificacion = input("ID del estudiante: ").strip()
    filas = estudiantes.index[estudiantes["id"].astype("string").eq(identificacion)]
    if len(filas) == 0:
        print("No se encontró un estudiante con ese ID.")
        return estudiantes

    try:
        nota = float(input(f"Nueva nota (de {NOTA_MIN:g} a {NOTA_MAX:g}): "))
        if not NOTA_MIN <= nota <= NOTA_MAX:
            raise ValueError
    except ValueError:
        print(f"La nota debe ser un número entre {NOTA_MIN:g} y {NOTA_MAX:g}.")
        return estudiantes

    estudiantes.loc[filas[0], "nota"] = nota
    guardar_estudiantes(estudiantes)
    print("Nota actualizada.")
    return estudiantes


def main() -> None:
    estudiantes = cargar_estudiantes()
    print(f"Archivo de datos: {ARCHIVO.name}")

    while True:
        print("\n1. Ver estudiantes\n2. Agregar estudiante\n3. Buscar por ID")
        print("4. Actualizar nota\n5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_estudiantes(estudiantes)
        elif opcion == "2":
            estudiantes = agregar_estudiante(estudiantes)
        elif opcion == "3":
            buscar_estudiante(estudiantes)
        elif opcion == "4":
            estudiantes = actualizar_nota(estudiantes)
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
