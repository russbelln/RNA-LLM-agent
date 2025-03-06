
import logging
import sys

def setup_logger(name: str, level=logging.INFO) -> logging.Logger:
    """
    Crea y configura un logger con un nivel determinado.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Evita agregar múltiples handlers si ya existen
    if not logger.handlers:
        # Crear un formateador
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Handler de consola
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)


    return logger



