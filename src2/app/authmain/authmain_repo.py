from datetime import timedelta

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src2.app.config.authkeymain import bcrypt_context
from src2.app.models.models import Users
from src2.app.user.user_schema import CreateUserRequest
from src2.app.authmain.util.authmain_util import create_access_token


class AuthMainRepo:
    @staticmethod
    async def create_user(create_user_request: CreateUserRequest, db: Session) -> str:
        create_user_model = Users(
            email=create_user_request.email,
            username=create_user_request.username,
            first_name=create_user_request.first_name,
            last_name=create_user_request.last_name,
            role=create_user_request.role,
            # hashed_password=create_user_request.password,
            hashed_password=bcrypt_context.hash(create_user_request.password),
            is_active=True
        )
        db.add(create_user_model)
        db.commit()
        return "hi amit data successfully inserted"

    @staticmethod
    def authenticate_user(username: str, password: str, db: Session) -> Users:
        user = db.query(Users).filter(Users.username == username).first()
        if not user:
            return False
        if not bcrypt_context.verify(password, user.hashed_password):
            return False
        return user

    @staticmethod
    def login_get_access_token(username: str, password: str, db: Session) -> str:
        user = AuthMainRepo.authenticate_user(username, password, db)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user. ')
        token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
        return token

