import nltk

# Asegúrate de descargar los datos de nltk al inicio del proyecto:
# nltk.download('punkt')
# nltk.download('stopwords')

def evaluate_relevance(generated_text: str, keywords: list) -> float:
    """
    Calcula la relevancia del texto en función de la
    cantidad de palabras clave encontradas.
    Retorna un porcentaje [0-1].
    """
    text_lower = generated_text.lower()
    total_keywords = len(keywords)
    if total_keywords == 0:
        return 0.0

    found = 0
    for kw in keywords:
        if kw.lower() in text_lower:
            found += 1

    return found / total_keywords

def evaluate_readability(text: str) -> float:
    """
    Calcula el índice de Flesch (por ejemplo) para medir legibilidad.
    A mayor puntaje, más sencillo de leer.
    """
    # Heurística simple
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    num_sentences = len(sentences)
    num_words = len(words)
    num_syllables = sum(count_syllables(word) for word in words)

    # Fórmula de Flesch simplificada en inglés (puede no ser exacta para español):
    # 206.835 - 1.015*(words/sentences) - 84.6*(syllables/words)
    if num_sentences == 0 or num_words == 0:
        return 0.0

    flesch_score = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (num_syllables / num_words)
    return flesch_score

def count_syllables(word: str) -> int:
    # Función simplificada, en la práctica, el conteo de sílabas en español
    # puede requerir un análisis más profundo.
    word = word.lower()
    return sum(letter in "aeiou" for letter in word)

def evaluate_consistency(texts: list) -> float:
    """
    Evalúa la consistencia entre varios textos,
    por ejemplo midiendo la similitud de contenido
    o detectando contradicciones.
    Aquí devolvemos un placeholder muy simplificado.
    """
    if not texts:
        return 0.0

    # Ejemplo: chequear si hay un texto que difiere demasiado en longitud
    lengths = [len(t) for t in texts]
    avg_length = sum(lengths) / len(lengths)
    diffs = [abs(l - avg_length) for l in lengths]
    max_diff = max(diffs)

    # Cuanto menor sea la desviación, más "consistentes" consideramos los textos
    if avg_length == 0:
        return 0.0

    consistency_score = 1.0 - (max_diff / avg_length)
    return max(0.0, consistency_score)
