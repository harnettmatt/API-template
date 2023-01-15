"""Tests for database"""

import pytest

from database.database import get_db
from database.database_service import DatabaseService
from database.tests.fixtures import MockAPIInput, MockPersistable


@pytest.fixture(name="mock_api_input")
def fixture_mock_api_input():
    return MockAPIInput(foo="bar")


@pytest.fixture(name="mock_db_service")
def fixture_mock_db_service():
    return DatabaseService(next(get_db()))


class TestDatabase:
    @staticmethod
    @pytest.mark.integtest
    def test_create_get(mock_db_service: DatabaseService, mock_api_input: MockAPIInput):
        # TODO: requires truncation of table before each run
        expected_persistable = MockPersistable(**mock_api_input.dict())

        # CREATE
        response = mock_db_service.create(mock_api_input, MockPersistable)
        assert response == expected_persistable

        # GET
        response = mock_db_service.get(
            identifier=mock_api_input.identifier, model=expected_persistable
        )
        assert response == expected_persistable

        # ALL
        response = mock_db_service.all(MockPersistable)
        assert response == [expected_persistable]
