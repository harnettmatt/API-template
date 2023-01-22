"""Module responsible for interacting with db via sqlalchemy"""
from typing import Optional, Type

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.database import get_session
from persistable.models import Persistable


class DatabaseService:
    """
    Service that interacts with the db
    """

    session: Session

    def __init__(self, session: Optional[Session] = None):
        self.session = session if session else get_session()

    def get(self, id: int, model_type: Type[Persistable]):
        """
        Gets instance from db for a given model and id
        """
        user = self.session.query(model_type).filter_by(id=id).first()
        self.session.close()

        return user

    def all(self, model_type: Type[Persistable], skip: int = 0, limit: int = 100):
        """
        Gets all instances from db for a given model and optional limiting
        """
        users = self.session.query(model_type).offset(skip).limit(limit).all()
        self.session.close()

        return users

    def create(self, input_schema: BaseModel, model_type: Type[Persistable]):
        """
        Creates instance in db for a given pydantic input schema and model
        """
        model_instance = model_type(**jsonable_encoder(input_schema))

        self.session.add(model_instance)
        self.session.commit()
        self.session.refresh(model_instance)
        self.session.close()

        return model_instance

    def delete(self, id: int, model_type: Type[Persistable]):
        """
        Deletes instance from db for a given model and id
        """
        model_instance = self.get(id=id, model_type=model_type)

        self.session.delete(model_instance)
        self.session.commit()
        self.session.close()

        return model_instance

    def update(self, id: int, input_schema: BaseModel, model_type: Type[Persistable]):
        """
        Gets instance from db, merges input_schema with db instance, update db instance
        """
        model_instance = self.get(id=id, model_type=model_type)
        updated_model_instance = self._update_model_instance_from_input(
            input=input_schema, model_instance=model_instance
        )

        self.session.add(updated_model_instance)
        self.session.commit()
        self.session.refresh(updated_model_instance)
        self.session.close()

        return updated_model_instance

    @classmethod
    def _update_model_instance_from_input(
        cls, input: BaseModel, model_instance: Persistable
    ) -> Persistable:
        """
        Converts input and model_instance to dicts and updates model_instance
        """
        update_dict = input.dict(exclude_none=True)
        model_instance_dict = jsonable_encoder(model_instance)

        for key, val in update_dict.items():
            if key in model_instance_dict:
                setattr(model_instance, key, val)

        return model_instance
