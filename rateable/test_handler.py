"""Unit tests for /rateables routing handler"""
from fastapi.testclient import TestClient

from rateable.handler import ROUTER


class TestHandler:
    """Unit tests for /rateables routing handler"""

    @staticmethod
    def test_get_all():
        """
        GIVEN: a GET request to /rateables
        THEN: a list of Rateables is returned
        """
        with TestClient(ROUTER) as client:
            response = client.get("/")
        assert response.status_code == 200
        assert response.json() == [
            {
                "identifier": "00000000-0000-0000-0000-000000000000",
                "name": "fake-rateable",
                "ranking_ids": [],
            }
        ]
