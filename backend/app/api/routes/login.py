from datetime import timedelta
from typing import Annotated, Any
import uuid

from app.config import security
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.crud.user import authenticate_user
from app.api import deps
from app.models.token import Token
# from models id

router = APIRouter()

@router.post("/login/access-token")
def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Session = Depends(deps.get_session))  -> Token:
  
    user = authenticate_user(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=300)
    return Token(
        access_token= security.create_access_token(
            user.id, expires_delta=access_token_expires
        )
    )
    
