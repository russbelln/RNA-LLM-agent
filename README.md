# RNA-LLM-agent
Universidad Nacional de Colombia - Sede Medellín Project

# Proyecto de Generación de Materiales Educativos con LLMs

Este proyecto implementa un agente inteligente que, a partir de un programa de curso (PDF, DOCX o TXT), genera:
- Notas de clase
- Problemas de práctica con soluciones
- Preguntas de discusión
- Objetivos de aprendizaje
- Recursos y lecturas sugeridas

## Requisitos

- Python 3.8+
- Recomendado crear un entorno virtual

## Instalación

```bash
git clone https://github.com/tu_usuario/mi_proyecto_llm.git
cd mi_proyecto_llm
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
python3 src/main.py --file pentesting.pdf --use_gemini --gemini_api_key API_KEY
```