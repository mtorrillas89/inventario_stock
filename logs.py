import logging
import os

LOG_FILE = "logs/app.log"


def configurar_logger():
    """
    Configura el sistema de logging del programa.
    """
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def registrar_log(mensaje):
    """
    Registra un mensaje en el archivo de log.

    Args:
        mensaje (str): Mensaje a registrar.
    """
    logging.info(mensaje)