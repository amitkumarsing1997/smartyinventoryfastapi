from bson import ObjectId

from src2.app.config.mongo_config import database
from src2.app.muser.user_schema import UserMongoSchema
from fastapi.encoders import jsonable_encoder

user_collection = database.get_collection("user_collection")


class MongoAuthRepo:
    # database = client.userdetails
    #
    # user_collection = database.get_collection("user_collection")
    #
    # invitation_collection = database.get_collection("invitation_collection")
    # @staticmethod
    # async def insert_user_detail(userschema_dict: dict):
    #     # print("in user Repo-------------")
    #     # print(type(userschema))
    #     # userschema_jsonable = jsonable_encoder(userschema)
    #     # print(type(userschema_jsonable))
    #     pymongouser = await user_collection.insert_one(userschema_dict)
    #     # user_id = pymongouser.inserted_id
    #     # print(user_id)
    #     # print(type(user_id))
    #     # return user_id
    #     return pymongouser


    @staticmethod
    async def find_user(userfield: dict):
        user = await user_collection.find_one(userfield)
        # print(user)
        # print(type(user))
        return user

