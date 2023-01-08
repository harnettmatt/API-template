"""Module containing helpful object constructors for mocking purposes"""
from uuid import UUID

from user.schemas import User
from utilities.fixtures import get_mock_uuid


def get_mock_user(identifier: UUID = get_mock_uuid()) -> User:
    """
    returns a mock User
    @param identifier: specify an identifier to use for User object
    @return: User
    """
    return User(identifier=identifier, first_name="John", last_name="Smith")
