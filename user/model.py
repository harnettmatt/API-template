"""models for User"""
from pydantic import BaseModel


class User(BaseModel):
    """
    Pydantic model for User
    """

    identifier: str  # TODO: uuid
    first_name: str
    last_name: str
