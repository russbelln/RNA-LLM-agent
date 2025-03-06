import os
from ingestion.parse_pdf import parse_pdf
from ingestion.parse_docx import parse_docx
from ingestion.parse_txt import parse_txt
from main import logger

def parse_course_file(file_path: str) -> str:
    """
    Detecta la extensión del archivo y llama
    al parser correspondiente.
    """
    _, ext = os.path.splitext(file_path.lower())
    if ext == ".pdf":
        return parse_pdf(file_path)
    elif ext == ".docx":
        return parse_docx(file_path)
    elif ext == ".txt":
        return parse_txt(file_path)
    else:
        raise ValueError(f"Formato de archivo no soportado: {ext}")


def extract_course_structure(raw_text: str) -> dict:
    """
    Dada la cadena completa del programa de curso,
    parsea y retorna una estructura con:
      - nombre del curso
      - objetivos
      - lista de temas
      - bibliografía
    Esta función puede usar heurísticas, expresiones regulares
    o técnicas NLP para identificar secciones.
    """
    # Ejemplo simple (heurístico). Ajusta según tu documento.
    lines = raw_text.split("\n")
    course_name = lines[0] if lines else "Curso Desconocido"

    # Búsqueda de secciones (muy simplificado)
    # En la práctica, puedes usar expresiones regulares o NLP más robusto.
    objectives = []
    topics = []
    bibliography = []

    # Lógica de ejemplo
    for line in lines:
        line_lower = line.lower()
        if "objetivo" in line_lower:
            objectives.append(line)
        elif "tema" in line_lower:
            topics.append(line)
        elif "bibliografía" in line_lower or "referencia" in line_lower:
            bibliography.append(line)

    return {
        "nombre_curso": course_name.strip(),
        "objetivos": objectives,
        "temas": topics,
        "bibliografia": bibliography
    }
