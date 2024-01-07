from abc import ABC, abstractmethod

from src2.app.authmain.authmain_schema import AuthResponse, UserRespSchema
from src2.app.muser.user_schema import UserMongoSchema
from src2.app.user.user_schema import CreateUserRequest
from sqlalchemy.orm import Session
from src2.app.authmain.authmain_schema import Token

class IAuthMainService(ABC):

    @abstractmethod
    async def reg_user(self, create_user_request: CreateUserRequest, db: Session) -> AuthResponse:
        pass

    @abstractmethod
    async def auth_user(self, username: str, password: str, db: Session) -> AuthResponse[UserRespSchema]:
        pass

    @abstractmethod
    async def login_get_access_token(self, username: str, password: str, db: Session) -> Token:
        pass


