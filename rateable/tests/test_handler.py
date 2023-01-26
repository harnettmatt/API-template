"""Unit tests for /rateables routing handler"""
import pytest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.database import get_session
from database.database_service import DatabaseService
from main import APP
from persistable.models import Base
from rateable import models, schemas

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


def create_rateable() -> models.Rateable:
    rateable_input = schemas.RateableCreate(name="Minca")
    return DatabaseService(next(override_get_session())).create(
        input_schema=rateable_input, model_type=models.Rateable
    )


class TestHandler:
    """Unit tests for /rateables routing handler"""

    @staticmethod
    @pytest.mark.integtest
    def test_get_all(test_client):
        """
        GIVEN: a GET request to /rateables
        THEN: a list of Rateables is returned
        """
        rateable_model = create_rateable()
        response = test_client.get("/rateables/")

        expected_rateable = schemas.Rateable(**jsonable_encoder(rateable_model))
        assert response.status_code == 200
        assert expected_rateable in response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_get(test_client):
        """
        GIVEN: a GET request to /rateables/{id}
        THEN: the corresponding rateable is returned
        """
        rateable_model = create_rateable()

        # unit under test
        response = test_client.get(f"/rateables/{rateable_model.id}")

        expected_rateable = schemas.Rateable(**jsonable_encoder(rateable_model))
        assert response.status_code == 200
        assert expected_rateable == response.json()

    @staticmethod
    @pytest.mark.integtest
    def test_create(test_client):
        """
        GIVEN: a POST request to /rateables with a request body
        THEN: a Rateable is created and returned
        """
        request_body = {"name": "Minca"}

        # unit under test
        response = test_client.post("/rateables/", json=request_body)

        assert response.status_code == 200
        response_dict = response.json()
        assert "id" in response_dict
        del response_dict["id"]
        assert response_dict == {"name": "Minca"}

    @staticmethod
    @pytest.mark.integtest
    def test_patch(test_client):
        """
        GIVEN: a PATCH request to /rateables with a request body
        THEN: a Rateable is updated and returned
        """

        rateable_model = create_rateable()
        request_body = {"name": "New Name"}
        expected_rateable = schemas.Rateable(id=rateable_model.id, **request_body)

        # unit under test
        response = test_client.patch(
            f"/rateables/{rateable_model.id}", json=request_body
        )

        assert response.status_code == 200
        assert response.json() == expected_rateable

        response = test_client.get(f"/rateables/{expected_rateable.id}")

        assert response.status_code == 200
        assert response.json() == expected_rateable

    @staticmethod
    @pytest.mark.integtest
    def test_delete(test_client):
        """
        GIVEN: a DELETE request to /rateables/{id}
        THEN: the corresponding rateable is returned
        """
        rateable_model = create_rateable()
        expected_rateable = schemas.Rateable(**jsonable_encoder(rateable_model))

        # unit under test
        response = test_client.delete(f"/rateables/{rateable_model.id}")

        assert response.status_code == 200
        assert expected_rateable == response.json()

        response = test_client.get(f"rateables/{rateable_model.id}")

        assert response.status_code == 404
