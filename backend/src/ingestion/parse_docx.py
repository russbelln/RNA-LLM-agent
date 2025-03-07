import docx

def parse_docx(file_path: str) -> str:
    """
    Lee y extrae el texto de un archivo DOCX,
    retornando una cadena de texto.
    """
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)
