from sqlalchemy import Column, String

from persistable.models import Persistable
from uuid_base_model.schemas import UUIDBaseModel


class MockAPIInput(UUIDBaseModel):
    foo: str


class MockPersistable(Persistable):
    __tablename__ = "mock_persistable"

    foo = Column(String)
