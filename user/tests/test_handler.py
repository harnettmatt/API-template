"""Unit tests for /users routing handler"""
import pytest
from fastapi.testclient import TestClient

from user.handler import ROUTER
from user.schemas import User as UserSchema
from user.tests.fixtures import create_user


class TestHandler:
    """Unit tests for /users routing handler"""

    @staticmethod
    @pytest.mark.integtest
    def test_get_all():
        """
        GIVEN: a GET request to /users
        THEN: a list of Users is returned
        """
        user_model = create_user()
        with TestClient(ROUTER) as client:
            response = client.get("/")

        user_schema_dict = UserSchema(**user_model.__dict__).dict()
        user_schema_dict["identifier"] = str(user_schema_dict["identifier"])
        assert response.status_code == 200
        response_dict = response.json()
        assert user_schema_dict in response_dict

    @staticmethod
    @pytest.mark.integtest
    def test_create():
        """
        GIVEN: a POST request to /users with a request body
        THEN: a User is created and returned
        """

        request_body = {"first_name": "John", "last_name": "Smith"}
        with TestClient(ROUTER) as client:
            response = client.post("/", json=request_body)
        assert response.status_code == 200
        response_dict = response.json()
        assert "identifier" in response_dict
        del response_dict["identifier"]
        assert response_dict == {
            "first_name": "John",
            "last_name": "Smith",
        }
