"""models for User"""
from pydantic import BaseModel

from uuid_base_model.schemas import UUIDBaseModel


class User(UUIDBaseModel):
    """
    Pydantic model for User
    """

    first_name: str
    last_name: str


class UserCreate(BaseModel):
    first_name: str
    last_name: str
