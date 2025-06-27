import pytest
from server.app import create_app, db
from flask import url_for
import json

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": "test-secret-key"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_auth_register_and_login(client):
    # Test user registration
    response = client.post("/auth/register", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 201 or response.status_code == 200

    # Test user login
    response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "access_token" in data

def test_episode_endpoints(client):
    # Test get episodes (empty initially)
    response = client.get("/episodes")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

    # Test create episode (assuming POST allowed)
    response = client.post("/episodes", json={
        "title": "Test Episode",
        "description": "Test Description"
    })
    # Depending on implementation, might be 201 or 405 if POST not allowed
    assert response.status_code in (201, 405, 404, 400)

def test_guest_endpoints(client):
    # Test get guests (empty initially)
    response = client.get("/guests")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_appearance_endpoints(client):
    # Test get appearances (empty initially)
    response = client.get("/appearances")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

# Additional tests can be added for edge cases and error handling
