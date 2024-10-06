from typing import Any
import uuid
from fastapi import APIRouter
from sqlmodel import Session
from app.models.user import Users, UserPublic, UserRegister, UserCreate
from app.config.db import SessionDep
from app.crud import user

router = APIRouter()


@router.post("/signup", response_model=UserPublic)
def create_user(session: SessionDep, user_create: UserRegister) -> Any:
    new_user = user.create_user(session=session, user_create=user_create)
    return new_user




    
    