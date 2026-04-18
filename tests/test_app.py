import pytest
import sys
import os

# Add app folder to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_status(client):
    """Test home route returns 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_home_has_message(client):
    """Test home route returns message"""
    response = client.get("/")
    data = response.get_json()
    assert "message" in data

def test_home_has_version(client):
    """Test home route returns version"""
    response = client.get("/")
    data = response.get_json()
    assert "version" in data

def test_health_check(client):
    """Test health route returns healthy"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"

def test_config_route(client):
    """Test config route returns config info"""
    response = client.get("/config")
    assert response.status_code == 200
    data = response.get_json()
    assert "version" in data
    assert "environment" in data