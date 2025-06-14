from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///src/user_database/users.db", echo=False)
