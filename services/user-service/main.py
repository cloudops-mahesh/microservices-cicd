from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="User Service", version="1.0.0")

users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob",   "email": "bob@example.com"},
}


class User(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "user-service"}


@app.get("/users", response_model=List[UserResponse])
def get_users():
    return list(users_db.values())


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]


@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: User):
    new_id = max(users_db.keys()) + 1
    users_db[new_id] = {"id": new_id, **user.model_dump()}
    return users_db[new_id]


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)