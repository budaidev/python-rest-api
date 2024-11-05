"""Test module for the Flask REST API routes."""

import pytest

from app import app
from app.routes import items


@pytest.fixture
def client():
    """Create client for each test."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        items.clear()
        yield client


def test_health_check(client):
    """Test health check enpoint to return 200."""
    response = client.get("api/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
