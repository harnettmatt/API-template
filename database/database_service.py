"""Module containing all database setup"""
from typing import List, Optional, Type
from uuid import UUID

from sqlalchemy.orm import Session

from persistable.models import Persistable
from uuid_base_model.schemas import UUIDBaseModel


class DatabaseService:
    """
    Service that interacts with the db layer
    """

    session: Session

    def __init__(self, session: Session):
        self.session = session

    def get(
        self, identifier: UUID, model_type: Type[Persistable]
    ) -> Optional[Persistable]:
        """
        Gets instance from db for a given model and identifier
        """
        return self.session.query(model_type).filter_by(identifier=identifier).first()

    def all(
        self, model_type: Type[Persistable], skip: int = 0, limit: int = 100
    ) -> List[Persistable]:
        """
        Gets all instances from db for a given model and optional limiting
        """
        return self.session.query(model_type).offset(skip).limit(limit).all()

    def create(self, input_schema: UUIDBaseModel, model_type: Type[Persistable]):
        """
        Creates instance in db for a given pydantic input schema and model
        """
        model_instance = model_type(**input_schema.dict())
        self.session.add(model_instance)
        self.session.commit()
        self.session.refresh(model_instance)
        return model_instance

    def delete(self, identifier: UUID, model_type: Type[Persistable]):
        """
        Deletes instance from db for a given model and identifier
        """
        self.session.query(model_type).filter_by(identifier=identifier).delete()
        self.session.commit()

    def update(self, input_schema: UUIDBaseModel, model_type: Type[Persistable]):
        """
        Gets instance from db, merges input_schema with db instance, update db instance
        """
        update_dict = input_schema.dict(exclude_none=True)
        self.session.query(model_type).filter_by(
            identifier=input_schema.identifier
        ).update(update_dict)
        self.session.commit()
