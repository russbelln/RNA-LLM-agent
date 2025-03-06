import os
# Si usas archivo .env para variables de entorno
from dotenv import load_dotenv
import google.generativeai as genai
from main import logger

load_dotenv()

class LLMAgent:
    def __init__(self, use_gemini=True, gemini_api_key=None, model="gemini-2.0-flash-001"):
        """
        use_gemini: booleano que indica si se usará la API de Gemini.
        gemini_api_key: clave de API para Gemini.
        """
        self.use_gemini= use_gemini
        self.api_key = gemini_api_key or os.environ["GOOGLE_API_KEY"]
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model)


    def generate_text_gemini(self, prompt: str) -> str:
        """
        Genera texto utilizando la API de gemini.
        """
        response = self.model.generate_content(prompt)

        if response.finish_reason == 4:
            logger.warning("El modelo estaba recitando material con derechos de autor.")
            return ""


        return response.text

    def generate_notes(self, topic: str) -> str:
        """
        Genera notas de clase para un tema en específico.
        """
        prompt = (
            f"Genera notas de clase detalladas sobre el tema: '{topic}'. "
            "Incluye explicaciones, ejemplos y consejos prácticos. "
            "Usa un estilo claro y conciso."
        )

        if self.use_gemini:
            return self.generate_text_gemini(prompt)

    def generate_exercises(self, topic: str, num_exercises: int = 3) -> str:
        """
        Genera problemas de práctica (ejercicios) para un tema.
        """
        prompt = (
            f"Genera {num_exercises} problemas de práctica sobre el tema: '{topic}', "
            "con soluciones detalladas paso a paso."
        )
        if self.use_gemini:
            return self.generate_text_gemini(prompt)

    def generate_discussion_questions(self, topic: str, num_questions: int = 3) -> str:
        """
        Genera preguntas de discusión abiertas.
        """
        prompt = (
            f"Genera {num_questions} preguntas de discusión abiertas sobre el tema '{topic}'. "
            "Las preguntas deben invitar a la reflexión y el debate."
        )
        if self.use_gemini:
            return self.generate_text_gemini(prompt)

    def generate_learning_objectives(self, topic: str) -> str:
        """
        Genera objetivos de aprendizaje para un tema.
        """
        prompt = (
            f"Genera objetivos de aprendizaje claros para el tema '{topic}'. "
            "Cada objetivo debe ser medible y específico."
        )
        if self.use_gemini:
            return self.generate_text_gemini(prompt)


    def generate_resources(self, topic: str) -> str:
        """
        Sugiere lecturas o recursos adicionales.
        """
        prompt = (
            f"Sugiere lecturas, recursos en línea y referencias bibliográficas "
            f"para complementar el tema '{topic}'."
        )
        if self.use_gemini:
            return self.generate_text_gemini(prompt)

