"""Module containing IDBaseModel intended for extension"""

from pydantic import BaseModel


class IDBaseModel(BaseModel):
    """
    Pydantic model with id field
    """

    id: int
