"""Module containing helpful object constructors for mocking purposes"""
from rateable.schemas import Rateable
from utilities.tests.fixtures import get_mock_id


def get_mock_rateable(id: int = get_mock_id()) -> Rateable:
    """
    returns a mock Rateable
    @param id: specify an id to use for Rateable object
    @return: Rateable
    """
    return Rateable(
        id=id,
        name="fake-rateable",
    )
