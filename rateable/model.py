"""models for Rateable"""
from uuid_base_model.model import UUIDBaseModel


class Rateable(UUIDBaseModel):
    """
    Pydantic model for Rateable
    """

    name: str
