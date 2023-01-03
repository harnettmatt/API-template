"""models for Rateable"""
from pydantic import BaseModel


class Rateable(BaseModel):
    """
    Pydantic model for Rateable
    """

    identifier: str  # TODO: uuid
    name: str
