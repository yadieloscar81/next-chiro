import uuid
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import Any, Optional
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(subject: uuid.UUID | Any, expires_delta: Optional[timedelta] = None):
    expire = datetime.now(timezone.utc)+ (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    payload = ({"exp": expire, "sub": str(subject) })
    encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

print(create_access_token({"sub": 5}))