from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="Order Service", version="1.0.0")

orders_db = {
    1: {"id": 1, "user_id": 1, "item": "Laptop",   "amount": 75000.00, "status": "delivered"},
    2: {"id": 2, "user_id": 1, "item": "Mouse",     "amount": 1200.00,  "status": "shipped"},
    3: {"id": 3, "user_id": 2, "item": "Keyboard",  "amount": 2500.00,  "status": "pending"},
}


class Order(BaseModel):
    user_id: int
    item: str
    amount: float


class OrderResponse(BaseModel):
    id: int
    user_id: int
    item: str
    amount: float
    status: str


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "order-service"}


@app.get("/orders", response_model=List[OrderResponse])
def get_orders():
    return list(orders_db.values())


@app.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(order_id: int):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders_db[order_id]


@app.get("/orders/user/{user_id}", response_model=List[OrderResponse])
def get_orders_by_user(user_id: int):
    return [o for o in orders_db.values() if o["user_id"] == user_id]


@app.post("/orders", response_model=OrderResponse, status_code=201)
def create_order(order: Order):
    new_id = max(orders_db.keys()) + 1
    orders_db[new_id] = {"id": new_id, "status": "pending", **order.model_dump()}
    return orders_db[new_id]


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)
