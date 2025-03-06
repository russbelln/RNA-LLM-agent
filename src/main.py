import argparse
from ingestion.parse_course import parse_course_file, extract_course_structure
from agent.llm_agent import LLMAgent
from markdown2 import markdown
from utils.logger import setup_logger
import logging


logger = setup_logger(__name__, level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser(description="Generar materiales educativos a partir de un programa de curso.")
    parser.add_argument("--file", type=str, required=True, help="Ruta del archivo de programa (PDF/DOCX/TXT).")
    parser.add_argument("--use_gemini", action="store_true", help="Usar gemini en lugar de un modelo local.")
    parser.add_argument("--gemini_api_key", type=str, help="Clave de API de Gemini.")
    args = parser.parse_args()

    # 1) Parsear y extraer la estructura del curso
    raw_text = parse_course_file(args.file)
    course_data = extract_course_structure(raw_text)
    print(f"Nombre del Curso: {course_data['nombre_curso']}")

    # 2) Inicializar el agente
    agent = LLMAgent(use_gemini=args.use_gemini, gemini_api_key=args.gemini_api_key)

    # 3) Para cada tema, generar materiales
    for topic in course_data["temas"]:
        topic_name = topic  # O extraer nombre más formal si parseaste en dict
        print(f"\n=== Generando materiales para: {topic_name} ===")
        notes = agent.generate_notes(topic_name)
        exercises = agent.generate_exercises(topic_name)
        discussion = agent.generate_discussion_questions(topic_name)
        objectives = agent.generate_learning_objectives(topic_name)
        resources = agent.generate_resources(topic_name)

        # 4) Mostrar o almacenar en archivos
        print("Notas de Clase:\n", notes)
        print("Ejercicios:\n", exercises)
        print("Preguntas de Discusión:\n", discussion)
        print("Objetivos de Aprendizaje:\n", objectives)
        print("Recursos Sugeridos:\n", resources)

if __name__ == "__main__":
    main()
