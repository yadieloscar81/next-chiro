import uuid

from fastapi import FastAPI
from pydantic import EmailStr, BaseModel
from sqlmodel import Field, Relationship, SQLModel

app = FastAPI()

class User(BaseModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    full_name: str
    email: str
    hashed_password: str
    
    
@app.get("/")
def read_root():
    return{"Hello": "World"}

@app.get("/users/{user_id}")
def read_user(user_id: int, user: User):
    return{"user": user.full_name}