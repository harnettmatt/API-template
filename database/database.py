"""Module containing all database setup"""
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from persistable.models import Persistable

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# TODO: move over to real db at some point
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Helper function responsible for creating and closing a db session
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


class DatabaseService:
    """
    Service that interacts with the db layer
    """

    database: Session

    def __init__(self, database: Session):
        self.database = database

    # TODO: type "model" stricter
    def get(self, identifier: UUID, model: Persistable):
        """
        Gets object from db for a given model and identifier
        """
        return self.database.query(model).filter(model.identifier == identifier).first()

    def all(self, model: Persistable, skip: int = 0, limit: int = 100):
        """
        Gets all objects from db for a given model and optional limiting
        """
        return self.database.query(model).offset(skip).limit(limit).all()

    def create(self, input_schema: BaseModel, model: Persistable):
        """
        Creates object in db for a given pydantic input schema and model
        """
        model_instance = model(**input_schema.dict())
        self.database.add(model_instance)
        self.database.commit()
        self.database.refresh(model_instance)
        return model_instance
