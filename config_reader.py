import json
from pathlib import Path
from typing import TypedDict


class StudentConfig(TypedDict):
    file: str
    columns: list[str]
    courses: list[str]
    grade_min: float
    grade_max: float


def _read_config() -> dict:
    config_path = Path(__file__).with_name("config.json")
    with config_path.open(encoding="utf-8") as config_file:
        config = json.load(config_file)

    if not isinstance(config, dict):
        raise ValueError("La configuración debe ser un objeto JSON.")
    return config


def load_config() -> dict[str, str]:
    config = _read_config()

    url = config.get("url")
    if not isinstance(url, str) or not url.strip():
        raise ValueError("La configuración debe incluir una URL válida.")

    return {"url": url}


def load_student_config() -> StudentConfig:
    config = _read_config().get("students")
    if not isinstance(config, dict):
        raise ValueError("La configuración debe incluir la sección 'students'.")

    file = config.get("file")
    columns = config.get("columns")
    courses = config.get("courses")
    grade_min = config.get("grade_min")
    grade_max = config.get("grade_max")

    if not isinstance(file, str) or not file.strip():
        raise ValueError("La configuración de estudiantes debe incluir un archivo.")
    if not isinstance(columns, list) or not all(isinstance(column, str) for column in columns):
        raise ValueError("Las columnas de estudiantes deben ser una lista de textos.")
    required_columns = {"id", "nombre", "edad", "curso", "nota"}
    if not required_columns.issubset(columns):
        raise ValueError("Las columnas deben incluir id, nombre, edad, curso y nota.")
    if not isinstance(courses, list) or not courses or not all(
        isinstance(course, str) and course.strip() for course in courses
    ):
        raise ValueError("Los cursos deben ser una lista no vacía de textos.")
    if (
        isinstance(grade_min, bool)
        or isinstance(grade_max, bool)
        or not isinstance(grade_min, (int, float))
        or not isinstance(grade_max, (int, float))
        or grade_min > grade_max
    ):
        raise ValueError("El rango de notas configurado no es válido.")

    return {
        "file": file,
        "columns": columns,
        "courses": courses,
        "grade_min": float(grade_min),
        "grade_max": float(grade_max),
    }
