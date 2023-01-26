"""Unit tests for /items routing handler"""
import pytest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.database import get_session
from database.database_service import DatabaseService
from item import models, schemas
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


def create_item() -> models.Item:
    item_input = schemas.ItemCreate(name="Minca")
    return DatabaseService(next(override_get_session())).create(
        input_schema=item_input, model_type=models.Item
    )


class TestHandler:
    """Unit tests for /items routing handler"""

    @staticmethod
    @pytest.mark.integtest
    def test_get_all(test_client):
        """
        GIVEN: a GET request to /items
        THEN: a list of Items is returned
        """
        item_model = create_item()
        response = test_client.get("/items/")

        expected_item = schemas.Item(**jsonable_encoder(item_model))
        assert response.status_code == 200
        assert expected_item in response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_get(test_client):
        """
        GIVEN: a GET request to /items/{id}
        THEN: the corresponding item is returned
        """
        item_model = create_item()

        # unit under test
        response = test_client.get(f"/items/{item_model.id}")

        expected_item = schemas.Item(**jsonable_encoder(item_model))
        assert response.status_code == 200
        assert expected_item == response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_create(test_client):
        """
        GIVEN: a POST request to /items with a request body
        THEN: a Item is created and returned
        """
        request_body = {"name": "Minca"}

        # unit under test
        response = test_client.post("/items/", json=request_body)

        assert response.status_code == 200
        response_dict = response.json()
        assert "id" in response_dict
        del response_dict["id"]
        assert response_dict == {"name": "Minca"}

    @staticmethod
    @pytest.mark.integtest
    def test_patch(test_client):
        """
        GIVEN: a PATCH request to /items with a request body
        THEN: a Item is updated and returned
        """

        item_model = create_item()
        request_body = {"name": "New Name"}
        expected_item = schemas.Item(id=item_model.id, **request_body)

        # unit under test
        response = test_client.patch(f"/items/{item_model.id}", json=request_body)

        assert response.status_code == 200
        assert response.json() == expected_item

        response = test_client.get(f"/items/{expected_item.id}")

        assert response.status_code == 200
        assert response.json() == expected_item

    @staticmethod
    @pytest.mark.integtest
    def test_delete(test_client):
        """
        GIVEN: a DELETE request to /items/{id}
        THEN: the corresponding item is returned
        """
        item_model = create_item()
        expected_item = schemas.Item(**jsonable_encoder(item_model))

        # unit under test
        response = test_client.delete(f"/items/{item_model.id}")

        assert response.status_code == 200
        assert expected_item == response.json()

        response = test_client.get(f"items/{item_model.id}")

        assert response.status_code == 404
