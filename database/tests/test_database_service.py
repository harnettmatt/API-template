"""Tests for database"""

import pytest

from database.database import get_session
from database.database_service import DatabaseService
from database.tests.fixtures import (
    MockAPICreateInput,
    MockAPIUpdateInput,
    MockPersistable,
)


@pytest.fixture(name="mock_api_create_input")
def fixture_mock_api_create_input():
    return MockAPICreateInput(foo="bar")


@pytest.fixture(name="mock_db_service")
def fixture_mock_db_service():
    return DatabaseService(get_session())


class TestDatabase:
    @staticmethod
    @pytest.mark.integtest
    def test_flow(
        mock_db_service: DatabaseService, mock_api_create_input: MockAPICreateInput
    ):
        # TODO: requires truncation of table before each run
        expected_persistable = MockPersistable(**mock_api_create_input.dict())

        # CREATE
        response = mock_db_service.create(
            input_schema=mock_api_create_input, model_type=MockPersistable
        )
        assert response == expected_persistable

        # GET
        response = mock_db_service.get(
            identifier=mock_api_create_input.identifier, model_type=MockPersistable
        )
        assert response == expected_persistable

        # ALL
        response = mock_db_service.all(model_type=MockPersistable)
        assert response == [expected_persistable]

        # UPDATE
        mock_api_update_input = MockAPIUpdateInput(**mock_api_create_input.dict())
        mock_api_update_input.foo = "new_value"
        expected_updated_persistable = MockPersistable(**mock_api_update_input.dict())
        response = mock_db_service.update(
            input_schema=mock_api_update_input, model_type=MockPersistable
        )
        response = mock_db_service.get(
            identifier=mock_api_update_input.identifier, model_type=MockPersistable
        )
        assert response == expected_updated_persistable

        # DELETE
        response = mock_db_service.delete(
            identifier=mock_api_create_input.identifier, model_type=MockPersistable
        )
