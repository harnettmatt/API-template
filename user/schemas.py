"""models for User"""
from typing import Optional

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


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
