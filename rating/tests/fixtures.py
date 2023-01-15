"""Module containing helpful object constructors for mocking purposes"""
from uuid import UUID

from rateable.tests.fixtures import get_mock_rateable
from rating.schemas import Rating
from user.tests.fixtures import get_mock_user
from utilities.tests.fixtures import get_mock_uuid


def get_mock_rating(identifier: UUID = get_mock_uuid()) -> Rating:
    """
    returns a mock Rating
    @param identifier: specify an identifier to use for Rating object
    @return: Rating
    """
    return Rating(
        identifier=identifier,
        author=get_mock_user(),
        recipient=get_mock_rateable(),
        rating=1,
    )
