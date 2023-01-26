"""Unit tests for /groups routing handler"""
import pytest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.database import get_session
from database.database_service import DatabaseService
from group import models, schemas
from main import APP
from persistable.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


APP.dependency_overrides[get_session] = override_get_session


@pytest.fixture(name="test_client")
def fixture_test_client():
    return TestClient(APP)


def create_group() -> models.Item:
    group_input = schemas.GroupCreate(name="Ramen")
    return DatabaseService(next(override_get_session())).create(
        input_schema=group_input, model_type=models.Item
    )


class TestHandler:
    """Unit tests for /groups routing handler"""

    @staticmethod
    @pytest.mark.integtest
    def test_get_all(test_client):
        """
        GIVEN: a GET request to /groups
        THEN: a list of Groups is returned
        """
        group_model = create_group()
        response = test_client.get("/groups/")

        expected_group = schemas.Group(**jsonable_encoder(group_model))
        assert response.status_code == 200
        assert expected_group in response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_get(test_client):
        """
        GIVEN: a GET request to /groups/{id}
        THEN: the corresponding group is returned
        """
        group_model = create_group()

        # unit under test
        response = test_client.get(f"/groups/{group_model.id}")

        expected_group = schemas.Group(**jsonable_encoder(group_model))
        assert response.status_code == 200
        assert expected_group == response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_create(test_client):
        """
        GIVEN: a POST request to /groups with a request body
        THEN: a Group is created and returned
        """
        request_body = {"name": "Ramen"}

        # unit under test
        response = test_client.post("/groups/", json=request_body)

        assert response.status_code == 200
        response_dict = response.json()
        assert "id" in response_dict
        del response_dict["id"]
        assert response_dict == {"name": "Ramen", "items": []}

    @staticmethod
    @pytest.mark.integtest
    def test_patch(test_client):
        """
        GIVEN: a PATCH request to /groups with a request body
        THEN: a Group is updated and returned
        """

        group_model = create_group()
        request_body = {"name": "NY Ramen"}
        expected_group = schemas.Group(id=group_model.id, **request_body)

        # unit under test
        response = test_client.patch(f"/groups/{group_model.id}", json=request_body)

        assert response.status_code == 200
        assert response.json() == expected_group

        response = test_client.get(f"/groups/{expected_group.id}")

        assert response.status_code == 200
        assert response.json() == expected_group

    @staticmethod
    @pytest.mark.integtest
    def test_delete(test_client):
        """
        GIVEN: a DELETE request to /groups/{id}
        THEN: the corresponding group is returned
        """
        group_model = create_group()
        expected_group = schemas.Group(**jsonable_encoder(group_model))

        # unit under test
        response = test_client.delete(f"/groups/{group_model.id}")

        assert response.status_code == 200
        assert expected_group == response.json()

        response = test_client.get(f"groups/{group_model.id}")

        assert response.status_code == 404
