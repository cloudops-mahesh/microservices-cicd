from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "user-service"

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) >= 2

def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404

def test_create_user():
    payload = {"name": "Charlie", "email": "charlie@example.com"}
    response = client.post("/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Charlie"