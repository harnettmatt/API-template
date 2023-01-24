"""Unit tests for /users routing handler"""
import pytest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.database import get_session
from database.database_service import DatabaseService
from main import APP
from persistable.models import Base
from user import models, schemas

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


def create_user() -> models.User:
    user_input = schemas.UserCreate(first_name="Matt", last_name="Harnett11")
    return DatabaseService(next(override_get_session())).create(
        input_schema=user_input, model_type=models.User
    )


class TestHandler:
    """Unit tests for /users routing handler"""

    @staticmethod
    @pytest.mark.integtest
    def test_get_all(test_client):
        """
        GIVEN: a GET request to /users
        THEN: a list of Users is returned
        """
        user_model = create_user()
        response = test_client.get("/users/")

        assert response.status_code == 200
        assert jsonable_encoder(user_model) in response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_get(test_client):
        """
        GIVEN: a GET request to /users/{id}
        THEN: the corresponding user is returned
        """
        user_model = create_user()

        # unit under test
        response = test_client.get(f"/users/{user_model.id}")

        assert response.status_code == 200
        assert jsonable_encoder(user_model) == response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_get_404(test_client):
        """
        GIVEN: a DELETE request to /users/{id}
        WHEN: the user does not exist
        THEN: a 404 error is returned
        """
        # unit under test
        response = test_client.get(f"/users/{9999999}")

        assert response.status_code == 404

    @staticmethod
    @pytest.mark.integtest
    def test_create(test_client):
        """
        GIVEN: a POST request to /users with a request body
        THEN: a User is created and returned
        """

        request_body = {"first_name": "John", "last_name": "Smith"}

        # unit under test
        response = test_client.post("/users/", json=request_body)

        assert response.status_code == 200
        response_dict = response.json()
        assert "id" in response_dict
        del response_dict["id"]
        assert response_dict == {
            "first_name": "John",
            "last_name": "Smith",
        }

    @staticmethod
    @pytest.mark.integtest
    def test_patch(test_client):
        """
        GIVEN: a PATCH request to /users with a request body
        THEN: a User is updated and returned
        """

        user_model = create_user()
        request_body = {"first_name": "Jane", "last_name": "Doe"}
        expected_user = models.User(id=user_model.id, **request_body)

        # unit under test
        response = test_client.patch(f"/users/{user_model.id}", json=request_body)

        assert response.status_code == 200
        assert response.json() == jsonable_encoder(expected_user)

        response = test_client.get(f"/users/{expected_user.id}")

        assert response.status_code == 200
        assert response.json() == jsonable_encoder(expected_user)

    @staticmethod
    @pytest.mark.integtest
    def test_patch_404(test_client):
        """
        GIVEN: a PATCH request to /users/{id}
        WHEN: the user does not exist
        THEN: a 404 error is returned
        """
        request_body = {"first_name": "Jane", "last_name": "Doe"}

        # unit under test
        response = test_client.patch(f"/users/{9999999}", json=request_body)

        assert response.status_code == 404

    @staticmethod
    @pytest.mark.integtest
    def test_delete(test_client):
        """
        GIVEN: a DELETE request to /users/{id}
        THEN: the corresponding user is returned
        """
        user_model = create_user()

        # unit under test
        response = test_client.delete(f"/users/{user_model.id}")

        assert response.status_code == 200
        assert jsonable_encoder(user_model) == response.json()

        response = test_client.get(f"users/{user_model.id}")

        assert response.status_code == 404

    @staticmethod
    @pytest.mark.integtest
    def test_delete_404(test_client):
        """
        GIVEN: a DELETE request to /users/{id}
        WHEN: the user does not exist
        THEN: a 404 error is returned
        """
        # unit under test
        response = test_client.delete(f"/users/{9999999}")

        assert response.status_code == 404
