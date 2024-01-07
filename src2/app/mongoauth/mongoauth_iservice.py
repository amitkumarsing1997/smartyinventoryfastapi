from abc import ABC
from src2.app.muser.user_schema import UserMongoSchema


class IMongoAuthService(ABC):
    # async def insert_user_if_not_present_in_collecton(self, userschema: UserMongoSchema):
    #     pass

    async def authenticate_user_inservice(self,username,password):
        pass

    async def create_access_token(self,username,firstname):
        pass

    # async def update_user_password(self,id,password):
    #     pass
