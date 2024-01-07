from sqlalchemy.orm import Session

from src2.app.authmain.authmain_schema import AuthResponse, UserRespSchema
from src2.app.exception.custom_exception import GenericException
from src2.app.muser.user_iservice import IUserServiceMongo
from src2.app.muser.user_schema import UserMongoSchema,ActualUserMongoSchema
from src2.app.muser.user_repo import UserRepoMongo
from src2.app.minvitation.invitation_iservice import IInvitationService
from src2.app.minvitation.invitation_service import InvitationService
from src2.app.minvitation.invitation_repo import InvitationRepoMongo
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, HTTPException
from typing import Annotated
from src2.app.muser.util.emailjinjaofficial import send_with_template
from src2.app.config.authkey import bcrypt_context
from src2.app.mongoauth.util.mongo_util import authenticate_user,create_access_token
from src2.app.authmain.authmain_schema import Token

from src2.app.authmain.authmain_iservice import IAuthMainService
from src2.app.authmain.authmain_repo import AuthMainRepo
# from src2.app.mongoauth.mongoauth_iservice import IMongoAuthService

from datetime import timedelta

from src2.app.mongoauth.mongoauth_repo import MongoAuthRepo
from src2.app.user.user_schema import CreateUserRequest
from src2.app.authmain.util.authmain_util import create_access_token


class AuthMainService(IAuthMainService):

    def __init__(self):
        pass


    async def reg_user(self, create_user_request: CreateUserRequest, db: Session)->AuthResponse[str]:
        print("hello amit")
        print(create_user_request)
        # print(type(self.authRepo))
        print(type(db))
        return AuthResponse[str](content=await AuthMainRepo.create_user(create_user_request, db))

    async def auth_user(self, username: str, password: str, db: Session) -> AuthResponse[UserRespSchema]:
        print("in user service")
        print(type(db))
        user_obj = AuthMainRepo.authenticate_user(username, password, db)
        if user_obj == False:

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

    def login_get_access_token(self,username: str, password: str, db: Session)->Token:
        token_obj = Token(access_token= AuthMainRepo.login_get_access_token(username,password,db),
                          token_type = "bearer")
        return token_obj



