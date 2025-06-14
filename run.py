from faker import Faker

# src
from src.global_logger.logger_config import get_logger
from src.database_manager.db_config import engine, Base
from src.database_manager.session_handler import with_session
from src.database_manager.models import User
from src.service.multi_threading_service import run_update
from src.utils.time_calculation import execution_timer
from src.utils.constants import FAKE_USER_COUNT

logger = get_logger(__name__)


def init_db():
    Base.metadata.create_all(engine)
    fake = Faker()

    @execution_timer
    @with_session
    def add_fake_users(session):
        for _ in range(FAKE_USER_COUNT):
            session.add(User(name=fake.name()))

    logger.info("Faker started creating fake users...")
    add_fake_users()


if __name__ == "__main__":
    init_db()
    run_update(threaded=True)
