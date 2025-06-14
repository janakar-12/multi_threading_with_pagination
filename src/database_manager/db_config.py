from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
DB_FILE_PATH = "src/user_database/users.db"
engine = create_engine(f"sqlite:///{DB_FILE_PATH}", echo=False)
