"""Module containing helpful object constructors for mocking purposes"""
from uuid import UUID

from rateable.schemas import Rateable
from utilities.tests.fixtures import get_mock_uuid


def get_mock_rateable(identifier: UUID = get_mock_uuid()) -> Rateable:
    """
    returns a mock Rateable
    @param identifier: specify an identifier to use for Rateable object
    @return: Rateable
    """
    return Rateable(
        identifier=identifier,
        name="fake-rateable",
    )
