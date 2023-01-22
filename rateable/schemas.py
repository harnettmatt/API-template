"""models for Rateable"""

from id_base_model.schemas import IDBaseModel


class Rateable(IDBaseModel):
    """
    Pydantic model for Rateable
    """

    name: str
