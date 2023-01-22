from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, String

from persistable.models import Persistable


class MockAPICreateInput(BaseModel):
    foo: str


class MockAPIUpdateInput(BaseModel):
    foo: Optional[str]


class MockPersistable(Persistable):
    __tablename__ = "mock_persistable"

    foo = Column(String)
