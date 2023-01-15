"""Unit tests for /rankings routing handler"""
from fastapi.testclient import TestClient

from ranking.handler import ROUTER


class TestHandler:
    """Unit tests for /rankings routing handler"""

    @staticmethod
    def test_get_all():
        """
        GIVEN: a GET request to /rankings
        THEN: a list of rankings is returned
        """
        with TestClient(ROUTER) as client:
            response = client.get("/")
        assert response.status_code == 200
        assert response.json() == [
            {
                "identifier": "00000000-0000-0000-0000-000000000000",
                "author": {
                    "identifier": "00000000-0000-0000-0000-000000000000",
                    "first_name": "John",
                    "last_name": "Smith",
                },
                "name": "fake-name",
                "ratings": [],
            }
        ]
