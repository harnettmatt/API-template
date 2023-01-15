"""Unit tests for /ratings routing handler"""
from fastapi.testclient import TestClient

from rating.handler import ROUTER


class TestHandler:
    """Unit tests for /ratings routing handler"""

    @staticmethod
    def test_get_all():
        """
        GIVEN: a GET request to /ratings
        THEN: a list of ratings is returned
        """
        with TestClient(ROUTER) as client:
            response = client.get("/")
        assert response.status_code == 200
        assert response.json() == [
            {
                "author": {
                    "identifier": "00000000-0000-0000-0000-000000000000",
                    "first_name": "John",
                    "last_name": "Smith",
                },
                "identifier": "00000000-0000-0000-0000-000000000000",
                "notes": None,
                "rating": 1.0,
                "recipient": {
                    "identifier": "00000000-0000-0000-0000-000000000000",
                    "name": "fake-rateable",
                },
            }
        ]
