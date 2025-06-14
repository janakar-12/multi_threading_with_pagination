import time
from functools import wraps

# src
from src.global_logger.logger_config import get_logger

logger = get_logger(__name__)


def execution_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        duration = end_time - start_time
        logger.info(f"Finished '{func.__name__}' in {duration:.4f} seconds.")

        return result

    return wrapper
