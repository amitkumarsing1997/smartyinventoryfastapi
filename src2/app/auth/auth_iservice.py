from abc import ABC,abstractmethod

from src2.app.auth.auth_schema import AuthResponse, UserRespSchema, Token
# from src.app.user.user_schema import CreateUserRequest
from src2.app.user.user_schema import CreateUserRequest
from src2.app.user.user_repo import UserRepo
from src2.app.models.models import Users
from sqlalchemy.orm import Session

class IAuthService(ABC):

    @abstractmethod
    async def reg_user(self,create_user_request:CreateUserRequest,db:Session)->AuthResponse:
        pass

    @abstractmethod
    async def auth_user(self,username:str,password:str,db:Session)->AuthResponse[UserRespSchema]:
        pass

    @abstractmethod
    async def login_get_access_token(self,username:str,password:str,db:Session)->Token:
        pass

    async def get_current_user(self)->dict:
        pass