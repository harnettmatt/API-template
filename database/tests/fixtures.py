from typing import Optional

from sqlalchemy import Column, String

from persistable.models import Persistable
from uuid_base_model.schemas import UUIDBaseModel


class MockAPICreateInput(UUIDBaseModel):
    foo: str


class MockAPIUpdateInput(UUIDBaseModel):
    foo: Optional[str]


class MockPersistable(Persistable):
    __tablename__ = "mock_persistable"

    foo = Column(String)
