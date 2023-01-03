"""Unit tests for /rankings routing handler"""
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
                "author": "fake-author",
                "identifier": "fake-identifier",
                "notes": None,
                "rating": 1.0,
                "recipient": "fake-recipient",
            }
        ]
