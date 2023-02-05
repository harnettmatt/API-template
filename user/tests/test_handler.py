"""Unit tests for /users routing handler"""
import pytest
from fastapi.encoders import jsonable_encoder


class TestHandler:
    """Unit tests for /users routing handler"""

    @staticmethod
    @pytest.mark.integtest
    def test_get_all(test_client, mock_user):
        """
        GIVEN: a GET request to /users
        THEN: a list of Users is returned
        """
        response = test_client.get("/users/")

        assert response.status_code == 200
        assert jsonable_encoder(mock_user) in response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_get(test_client, mock_user):
        """
        GIVEN: a GET request to /users/{id}
        THEN: the corresponding user is returned
        """
        # unit under test
        response = test_client.get(f"/users/{mock_user.id}")

        assert response.status_code == 200
        assert jsonable_encoder(mock_user) == response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_get_404(test_client):
        """
        GIVEN: a GET request to /users/{id}
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

        response = test_client.post("/users/")

        assert response.status_code == 200
        assert "id" in response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_delete(test_client, mock_user):
        """
        GIVEN: a DELETE request to /users/{id}
        THEN: the corresponding user is returned
        """
        # unit under test
        response = test_client.delete(f"/users/{mock_user.id}")

        assert response.status_code == 200
        assert jsonable_encoder(mock_user) == response.json()

        response = test_client.get(f"users/{mock_user.id}")

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
