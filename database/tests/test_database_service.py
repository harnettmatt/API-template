"""Tests for database"""

import pytest
from fastapi.encoders import jsonable_encoder

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


@pytest.fixture(name="mock_api_update_input")
def fixture_mock_api_update_input():
    return MockAPIUpdateInput(foo="bar2")


@pytest.fixture(name="mock_db_service")
def fixture_mock_db_service():
    return DatabaseService(get_session())


class TestDatabase:
    @staticmethod
    @pytest.mark.integtest
    def test_flow(
        mock_db_service: DatabaseService,
        mock_api_create_input: MockAPICreateInput,
        mock_api_update_input: MockAPIUpdateInput,
    ):
        # CREATE
        response = mock_db_service.create(
            input_schema=mock_api_create_input, model_type=MockPersistable
        )
        id = response.id
        expected_create_persistable = MockPersistable(
            **jsonable_encoder(mock_api_create_input), id=id
        )
        assert response == expected_create_persistable

        # GET
        response = mock_db_service.get(id=id, model_type=MockPersistable)
        assert response == expected_create_persistable

        # ALL
        response = mock_db_service.all(model_type=MockPersistable)
        assert response == [expected_create_persistable]

        # UPDATE
        response = mock_db_service.update(
            id=id, input_schema=mock_api_update_input, model_type=MockPersistable
        )
        response = mock_db_service.get(id=id, model_type=MockPersistable)
        expected_update_persistable = MockPersistable(
            **jsonable_encoder(mock_api_update_input), id=id
        )
        assert response == expected_update_persistable

        # DELETE
        response = mock_db_service.delete(id=id, model_type=MockPersistable)
