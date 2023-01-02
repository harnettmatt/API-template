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
        assert response.json() == []
