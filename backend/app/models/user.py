from typing import Optional
import uuid
from sqlmodel import SQLModel, Field
from pydantic import EmailStr

class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    first_name: str = Field(max_length=255, nullable=False)
    last_name: str = Field(max_length=255, nullable=False)

class UserCreate(UserBase):
    password: str = Field(min_length=8,max_length=40)

class UserRegister(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    first_name: str = Field(max_length=255, nullable=False)
    last_name: str = Field(max_length=255, nullable=False)
    password: str = Field(min_length=8,max_length=40)
    
class Users(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str


class UserRead(UserBase):
    id: uuid.UUID

class UserUpdate(UserBase):
    email: Optional[str] = None
    first_name: str | None = Field(default=None, max_length=255)
    last_name: str | None = Field(default=None, max_length=255)

# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: uuid.UUID


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int