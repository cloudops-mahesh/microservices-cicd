from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "order-service"

def test_get_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    assert len(response.json()) >= 3

def test_get_order_by_id():
    response = client.get("/orders/1")
    assert response.status_code == 200
    assert response.json()["item"] == "Laptop"

def test_get_order_not_found():
    response = client.get("/orders/999")
    assert response.status_code == 404

def test_get_orders_by_user():
    response = client.get("/orders/user/1")
    assert response.status_code == 200
    assert all(o["user_id"] == 1 for o in response.json())

def test_create_order():
    payload = {"user_id": 2, "item": "Monitor", "amount": 15000.00}
    response = client.post("/orders", json=payload)
    assert response.status_code == 201
    assert response.json()["status"] == "pending"