"""Module containing all database setup"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import base  # noqa
from persistable.models import Base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@0.0.0.0:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine)


def get_db():
    """
    Helper function responsible for creating and closing a db session
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
