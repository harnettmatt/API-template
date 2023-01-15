"""Module containing all database setup"""
from typing import Type
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.orm import Session

from persistable.models import Persistable


class DatabaseService:
    """
    Service that interacts with the db layer
    """

    database: Session

    def __init__(self, database: Session):
        self.database = database

    def get(self, identifier: UUID, model_type: Type[Persistable]):
        """
        Gets object from db for a given model and identifier
        """
        return self.database.query(model_type).filter_by(identifier=identifier).first()

    def all(self, model_type: Type[Persistable], skip: int = 0, limit: int = 100):
        """
        Gets all objects from db for a given model and optional limiting
        """
        return self.database.query(model_type).offset(skip).limit(limit).all()

    def create(self, input_schema: BaseModel, model_type: Type[Persistable]):
        """
        Creates object in db for a given pydantic input schema and model
        """
        model_instance = model_type(**input_schema.dict())
        self.database.add(model_instance)
        self.database.commit()
        self.database.refresh(model_instance)
        return model_instance

    def delete(self, identifier: UUID, model_type: Type[Persistable]):
        """
        Deletes object from db for a given model and identifier
        """
        self.database.query(model_type).filter_by(identifier=identifier).delete()
        self.database.commit()
