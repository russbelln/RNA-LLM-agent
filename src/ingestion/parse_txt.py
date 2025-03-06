def parse_txt(file_path: str) -> str:
    """
    Lee y extrae el texto de un archivo TXT.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    return data
