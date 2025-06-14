import os
from dotenv import load_dotenv
import logging

load_dotenv()

ENV = os.getenv("ENV")
LOG_LEVEL = logging.DEBUG if ENV == "DEV" else logging.INFO


def get_logger(name):
    """Adds the Filename to logger and returns the logger

    Args:
        name (str): __name__
    """
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(levelname)s] %(asctime)s - %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
