"""models for User"""
from pydantic import BaseModel

from id_base_model.schemas import IDBaseModel


class User(IDBaseModel):
    """
    Pydantic model for User
    """

    first_name: str
    last_name: str

    class Config:
        # TODO: should this be moved to IDBaseModel
        orm_mode = True


class UserCreate(BaseModel):
    first_name: str
    last_name: str
