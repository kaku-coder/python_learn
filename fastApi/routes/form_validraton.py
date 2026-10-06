from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    name: str
    age: int
    email: str


users: list[User] = []


@router.get("/users")
def get_users():
    return [user.model_dump() for user in users]


@router.post("/users")
def create_user(user: User):
    users.append(user)
    return user

