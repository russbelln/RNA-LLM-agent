from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from ingestion.parse_course import parse_course_file, extract_course_structure
from agent.llm_agent import LLMAgent
from utils.logger import setup_logger
import logging
import shutil
import os

logger = setup_logger(__name__, level=logging.DEBUG)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:7000",
    "http://75.101.241.138:7000"  # Add your frontend URL here
    # Add other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-materials/")
def generate_materials(
    use_gemini: bool = Form(True),
    gemini_api_key: str = Form(None),
    file: UploadFile = File(...)
):
    try:
        # Guardar el archivo subido temporalmente
        temp_file_path = f"/tmp/{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 1) Parsear y extraer la estructura del curso
        raw_text = parse_course_file(temp_file_path)
        course_data = extract_course_structure(raw_text)
        logger.info(f"Nombre del Curso: {course_data['nombre_curso']}")

        # 2) Inicializar el agente
        agent = LLMAgent(use_gemini=use_gemini, gemini_api_key=gemini_api_key)

        # 3) Para cada tema, generar materiales
        materials = {}
        for topic in course_data["temas"]:
            topic_name = topic
            logger.info(f"Generando materiales para: {topic_name}")
            notes = agent.generate_notes(topic_name)
            exercises = agent.generate_exercises(topic_name)
            discussion = agent.generate_discussion_questions(topic_name)
            objectives = agent.generate_learning_objectives(topic_name)
            resources = agent.generate_resources(topic_name)

            materials[topic_name] = {
                "notes": notes,
                "exercises": exercises,
                "discussion": discussion,
                "objectives": objectives,
                "resources": resources
            }
            logger.info("Materiales generados correctamente")

        return {"course_name": course_data['nombre_curso'], "materials": materials}
    except Exception as e:
        logger.error(f"Error al generar materiales: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        try:
            os.remove(temp_file_path)
        except Exception as e:
            logger.error(f"Error al eliminar el archivo temporal: {e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
