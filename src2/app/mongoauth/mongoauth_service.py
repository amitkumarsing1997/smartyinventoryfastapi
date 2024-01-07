from src2.app.exception.custom_exception import GenericException
from src2.app.muser.user_iservice import IUserServiceMongo
from src2.app.muser.user_schema import UserMongoSchema,ActualUserMongoSchema
from src2.app.muser.user_repo import UserRepoMongo
from src2.app.minvitation.invitation_iservice import IInvitationService
from src2.app.minvitation.invitation_service import InvitationService
from src2.app.minvitation.invitation_repo import InvitationRepoMongo
from fastapi.encoders import jsonable_encoder
from fastapi import Depends
from typing import Annotated
from src2.app.muser.util.emailjinjaofficial import send_with_template
from src2.app.config.authkey import bcrypt_context
from src2.app.mongoauth.util.mongo_util import authenticate_user,create_access_token
from src2.app.mongoauth.mongoauth_schema import Token

from src2.app.mongoauth.mongoauth_iservice import IMongoAuthService

from datetime import timedelta

from src2.app.mongoauth.mongoauth_repo import MongoAuthRepo
class MongoAuthService(IMongoAuthService):

    def __init__(self):
        super().__init__()
        # self.irepo = irepo
    # def __init__(self,iinvitation:IInvitationService= Depends(InvitationService)):
    #     super().__init__()
    #     self.iinvitation = iinvitation
    # def __init__(self,iinvitation:InvitationService = Depends()):
    #     super().__init__()
    #     self.iinvitation = iinvitation
    # def __init__(self, userRepo: UserRepo = Depends()) -> None:
    #     super().__init__()
    #     self.userRepo = userRepo

    async def authenticate_user_inservice(self, username, password):
        print("in authenticate user service--------")
        return await authenticate_user(username,password)

    async def create_access_token(self,username,firstname):
        print("in serive of create_access_token-------------")
        token_str = await create_access_token(username,firstname,timedelta(minutes=20))
        token_model = Token(access_token=token_str,token_type="bearer")
        return token_model
        # userobj = await authenticate_user_inservice(username, password)




    # async def authenticate_user(self,username,password):
    #     print("in authenticate user service--------")
    #     userobj = await MongoAuthRepo.find_user({"email": username})
    #     if not userobj:
    #         raise GenericException(msg="user email incorrect", msg_code="500")
    #     if not bcrypt_context.verify(password, userobj.get("password")):
    #         raise GenericException(msg="user password incorrect", msg_code="500")
    #     return userobj






