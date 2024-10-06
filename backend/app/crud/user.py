from typing import Optional
from sqlmodel import Session, select
from app.models.user import Users, UserCreate
from app.config.security import get_password_hash, verify_password

def get_user_by_email(session: Session, user_id: int) -> Optional[Users]:
    return session.get(Users, user_id)

def get_user_by_email(session: Session, email: str) -> Optional[Users]:
    statement = select(Users).where(Users.email == email)
    return session.exec(statement).first()

def create_user(session: Session, user_create: UserCreate) -> Users:
    user = Users.model_validate(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    print("Users ", user)
    return user

def authenticate_user(session: Session, email: str, password: str) -> Optional[Users]:
    Users = get_user_by_email(session, email)
    if not Users:
        return None
    return Users
