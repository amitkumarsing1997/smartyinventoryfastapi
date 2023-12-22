# from src2.app.user.user_iservice import IUserService
from src2.app.auth.auth_iservice import IAuthService
from src2.app.auth.auth_repo import AuthRepo
from src2.app.auth.auth_schema import AuthResponse, UserRespSchema ,Token
from src2.app.exception.custom_exception import GenericException
from src2.app.user.user_repo import UserRepo
from fastapi import Depends
from src2.app.user.user_schema import CreateUserRequest
from src2.app.config.db_config import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from src2.app.user.user_repo import UserRepo
from src2.app.models.models import Users
from sqlalchemy.orm import Session
from fastapi import HTTPException


# open_ai: OpenAI = Depends()


class UserREspSchema:
    pass


class AuthService(IAuthService):
    def __init__(self, authRepo: AuthRepo = Depends()) -> None:
        super().__init__()
        self.authRepo = authRepo

    async def reg_user(self, create_user_request: CreateUserRequest, db: Session)->AuthResponse[str]:
        print("hello amit")
        print(create_user_request)
        print(type(self.authRepo))
        print(type(db))
        return AuthResponse[str](content=await self.authRepo.create_user(create_user_request, db))

    async def auth_user(self, username: str, password: str, db: Session) -> AuthResponse[UserRespSchema]:
        print("in user service")
        print(type(db))
        user_obj = self.authRepo.authenticate_user(username, password, db)
        if user_obj == False:
            # raise HTTPException(msg=418, msg_code="Nope! I don't like 3.")
            raise HTTPException(status_code=401, detail="Authentication Failed.")
            # raise GenericException(msg="Exception occured due to unauthenticated user",
            #                        msg_code="not a valid user")

        user_resp_sch = UserRespSchema(
             id=user_obj.id,
             email = user_obj.email,
             username = user_obj.username,
             first_name = user_obj.first_name,
             last_name = user_obj.last_name,
             role = user_obj.role
         )

        return AuthResponse[UserRespSchema](content = user_resp_sch)


    async def login_get_access_token(self, username: str, password: str, db: Session)->Token:
        token_obj = Token(access_token= await self.authRepo.login_get_access_token(username,password,db),
                          token_type = "bearer")
        return token_obj

    # class Token(BaseModel):
    #     access_token: str
    #     token_type: str

    async def get_current_user(self) ->dict:
        return await self.authRepo.get_current_user()
