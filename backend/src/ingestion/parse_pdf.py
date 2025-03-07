import pdfplumber

def parse_pdf(file_path: str) -> str:
    """
    Lee y extrae el texto de un archivo PDF, retornando
    una cadena de texto limpia.
    """
    text_content = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text_content.append(page.extract_text() or "")
    combined_text = "\n".join(text_content)
    return combined_text
