from math import ceil
from concurrent.futures import ThreadPoolExecutor

# src
from src.service.pagination_service import process_page
from src.database_manager.models import User
from src.database_manager.session_handler import with_session
from src.global_logger.logger_config import get_logger
from src.utils.constants import PAGE_SIZE, MAX_WORKERS
from src.utils.time_calculation import execution_timer

logger = get_logger(__name__)


@with_session
def get_total_users(session):
    return session.query(User).count()


def run_update(threaded=True):
    total_users = get_total_users()
    total_pages = ceil(total_users / PAGE_SIZE)

    if threaded:
        logger.info("Running threaded update...")
        initiate_multi_threading(total_pages)
    else:
        logger.info("Running Single threaded update")
        initiate_single_threading(total_pages)


@execution_timer
def initiate_multi_threading(total_pages):
    with ThreadPoolExecutor(
        max_workers=MAX_WORKERS, thread_name_prefix="PageWorker_Thread"
    ) as executor:
        executor.map(process_page, range(1, total_pages + 1))


@execution_timer
def initiate_single_threading(total_pages):
    for page in range(1, total_pages + 1):
        process_page(page)
