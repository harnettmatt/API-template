"""models for Rateable"""

from typing import Optional

from pydantic import BaseModel

from id_base_model.schemas import IDBaseModel


class Rateable(IDBaseModel):
    """
    Pydantic model for Rateable
    """

    name: str

    class Config:
        orm_mode = True


class RateableCreate(BaseModel):
    name: str


class RateableUpdate(BaseModel):
    name: Optional[str]
