from functools import wraps
from sqlalchemy.orm import sessionmaker

# src
from src.global_logger.logger_config import get_logger
from src.database_manager.db_config import engine

logger = get_logger(__name__)

SessionLocal = sessionmaker(bind=engine)


def with_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = SessionLocal()
        try:
            result = func(session, *args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            logger.error(f"SQL Error occurred: {e}")
            raise e
        finally:
            session.close()

    return wrapper
