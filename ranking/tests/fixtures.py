"""Module containing helpful object constructors for mocking purposes"""
from ranking.schemas import Ranking
from user.tests.fixtures import get_mock_user
from utilities.tests.fixtures import get_mock_id


def get_mock_ranking(id: int = get_mock_id()) -> Ranking:
    """
    returns a mock Ranking
    @param id: specify an id to use for User object
    @return: User
    """
    return Ranking(id=id, author=get_mock_user(), name="fake-name")
