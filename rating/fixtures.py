"""Module containing helpful object constructors for mocking purposes"""
from uuid import UUID

from rating.model import Rating
from utilities.fixtures import get_mock_uuid


def get_mock_rating(identifier: UUID = get_mock_uuid()) -> Rating:
    """
    returns a mock Rating
    @param identifier: specify an identifier to use for Rating object
    @return: Rating
    """
    return Rating(
        identifier=identifier,
        author="fake-author",
        recipient="fake-recipient",
        rating=1,
    )
