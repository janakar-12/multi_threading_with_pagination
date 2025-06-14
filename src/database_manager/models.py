from sqlalchemy import Column, Integer, String

# src
from src.database_manager.db_config import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
