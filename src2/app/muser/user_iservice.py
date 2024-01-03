from abc import ABC
from src2.app.muser.user_schema import UserMongoSchema


class IUserServiceMongo(ABC):
    async def insert_user_if_not_present_in_collecton(self, userschema: UserMongoSchema):
        pass

    async def authenticate_user(self,username,password):
        pass

    async def update_user_password(self,id,password):
        pass


