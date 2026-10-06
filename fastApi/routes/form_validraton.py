import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()


class User(BaseModel):
  name: str
  age:int
  email:str


@router.post("/users") 
def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "email": user.email
    }


