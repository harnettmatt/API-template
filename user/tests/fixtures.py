"""Module containing helpful object constructors for mocking purposes"""
from utilities.tests.fixtures import get_mock_user_id

from user import schemas


def get_mock_user(id: str = get_mock_user_id()) -> schemas.User:
    """
    returns a mock User
    @param id: specify an id to use for User object
    @return: User
    """
    return schemas.User(id=id)
