"""Module containing UUIDBaseModel intended for extension"""
from uuid import UUID

from pydantic import BaseModel, Field

from utilities.utilities import Utilities


class UUIDBaseModel(BaseModel):
    """
    Pydantic model with autogenerating uuid capabilities
    """

    identifier: UUID = Field(default_factory=Utilities.generate_uuid)
