"""Module containing helpful object constructors for mocking purposes"""
from uuid import UUID

from ranking.model import Ranking
from utilities.fixtures import get_mock_uuid


def get_mock_ranking(identifier: UUID = get_mock_uuid()) -> Ranking:
    """
    returns a mock Ranking
    @param identifier: specify an identifier to use for User object
    @return: User
    """
    return Ranking(identifier=identifier, name="fake-name")
