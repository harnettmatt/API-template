"""Unit tests for /rankings routing handler"""
import pytest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.database import get_session
from database.database_service import DatabaseService
from main import APP
from persistable.models import Base
from ranking import models, schemas

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


def create_ranking() -> models.Item:
    ranking_input = schemas.RankingCreate(name="Ramen")
    return DatabaseService(next(override_get_session())).create(
        input_schema=ranking_input, model_type=models.Item
    )


class TestHandler:
    """Unit tests for /rankings routing handler"""

    @staticmethod
    @pytest.mark.integtest
    def test_get_all(test_client):
        """
        GIVEN: a GET request to /rankings
        THEN: a list of Rankings is returned
        """
        ranking_model = create_ranking()
        response = test_client.get("/rankings/")

        expected_ranking = schemas.Ranking(**jsonable_encoder(ranking_model))
        assert response.status_code == 200
        assert expected_ranking in response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_get(test_client):
        """
        GIVEN: a GET request to /rankings/{id}
        THEN: the corresponding ranking is returned
        """
        ranking_model = create_ranking()

        # unit under test
        response = test_client.get(f"/rankings/{ranking_model.id}")

        expected_ranking = schemas.Ranking(**jsonable_encoder(ranking_model))
        assert response.status_code == 200
        assert expected_ranking == response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_create(test_client):
        """
        GIVEN: a POST request to /rankings with a request body
        THEN: a Ranking is created and returned
        """
        request_body = {"name": "Ramen"}

        # unit under test
        response = test_client.post("/rankings/", json=request_body)

        assert response.status_code == 200
        response_dict = response.json()
        assert "id" in response_dict
        del response_dict["id"]
        assert response_dict == {"name": "Ramen", "items": []}

    @staticmethod
    @pytest.mark.integtest
    def test_patch(test_client):
        """
        GIVEN: a PATCH request to /rankings with a request body
        THEN: a Ranking is updated and returned
        """

        ranking_model = create_ranking()
        request_body = {"name": "NY Ramen"}
        expected_ranking = schemas.Ranking(id=ranking_model.id, **request_body)

        # unit under test
        response = test_client.patch(f"/rankings/{ranking_model.id}", json=request_body)

        assert response.status_code == 200
        assert response.json() == expected_ranking

        response = test_client.get(f"/rankings/{expected_ranking.id}")

        assert response.status_code == 200
        assert response.json() == expected_ranking

    @staticmethod
    @pytest.mark.integtest
    def test_delete(test_client):
        """
        GIVEN: a DELETE request to /rankings/{id}
        THEN: the corresponding ranking is returned
        """
        ranking_model = create_ranking()
        expected_ranking = schemas.Ranking(**jsonable_encoder(ranking_model))

        # unit under test
        response = test_client.delete(f"/rankings/{ranking_model.id}")

        assert response.status_code == 200
        assert expected_ranking == response.json()

        response = test_client.get(f"rankings/{ranking_model.id}")

        assert response.status_code == 404
