import threading

# src
from src.database_manager.models import User
from src.database_manager.session_handler import with_session
from src.global_logger.logger_config import get_logger
from src.utils.constants import PAGE_SIZE

logger = get_logger(__name__)


@with_session
def process_page(session, page):
    thread_name = threading.current_thread().name
    logger.info(f"{thread_name} is processing page {page}")

    offset = (page - 1) * PAGE_SIZE
    users = session.query(User).offset(offset).limit(PAGE_SIZE).all()
    for user in users:
        user.name += "_updated"

    logger.info(f"{thread_name} finished page {page}")
