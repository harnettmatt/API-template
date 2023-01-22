"""Unit tests for /users routing handler"""
import pytest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

from user.handler import ROUTER
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

        assert response.status_code == 200
        assert jsonable_encoder(user_model) in response.json()

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
        assert "id" in response_dict
        del response_dict["id"]
        assert response_dict == {
            "first_name": "John",
            "last_name": "Smith",
        }
