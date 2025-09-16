from datetime import datetime
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_time_returns_200():
    """Test that GET /time returns 200 status code."""
    response = client.get("/time")
    assert response.status_code == 200


def test_get_time_response_structure():
    """Test that GET /time returns expected JSON structure."""
    response = client.get("/time")
    json_response = response.json()

    assert "local_time" in json_response
    assert isinstance(json_response["local_time"], str)


def test_get_time_returns_valid_iso_format():
    """Test that GET /time returns time in valid ISO format."""
    response = client.get("/time")
    json_response = response.json()

    try:
        parsed_time = datetime.fromisoformat(json_response["local_time"])
        assert parsed_time is not None
    except ValueError:
        pytest.fail("local_time is not in valid ISO format")


def test_get_time_returns_recent_time():
    """Test that GET /time returns a time close to current time."""
    before_request = datetime.now()
    response = client.get("/time")
    after_request = datetime.now()

    json_response = response.json()
    response_time = datetime.fromisoformat(json_response["local_time"])

    assert before_request <= response_time <= after_request