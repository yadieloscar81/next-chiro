from typing import Generator
import uuid
from fastapi import Depends, HTTPException, status
from sqlmodel import Session
from jose import JWTError, jwt

from app.config.db import get_session
from app.config.config import settings
from app.models.user import Users
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")

ALGORITHM = "HS256"

def get_current_user(
    session: Session = Depends(get_session),
    token: str = Depends(oauth2_scheme)
) -> Users:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        user_id: uuid.UUID = int(payload.get("sub"))
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = session.get(Users, user_id)
    if user is None:
        raise credentials_exception
    return user
