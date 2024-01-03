from bson import ObjectId

from src2.app.config.mongo_config import database
from src2.app.muser.user_schema import UserMongoSchema
from fastapi.encoders import jsonable_encoder

user_collection = database.get_collection("user_collection")


class UserRepoMongo:
    # database = client.userdetails
    #
    # user_collection = database.get_collection("user_collection")
    #
    # invitation_collection = database.get_collection("invitation_collection")
    @staticmethod
    async def insert_user_detail(userschema_dict: dict):
        # print("in user Repo-------------")
        # print(type(userschema))
        # userschema_jsonable = jsonable_encoder(userschema)
        # print(type(userschema_jsonable))
        pymongouser = await user_collection.insert_one(userschema_dict)
        # user_id = pymongouser.inserted_id
        # print(user_id)
        # print(type(user_id))
        # return user_id
        return pymongouser

    @staticmethod
    async def find_user(userfield: dict):
        user = await user_collection.find_one(userfield)
        # print(user)
        # print(type(user))
        return user

    @staticmethod
    async def hello_testing():
        print("hello testing ---------")

    @staticmethod
    # async def find_user_by_id():
    #     print("In find User--------")
    #     user = await user_collection.find_one({"_id": ObjectId("6594f0494f96249b94dd8bd8")})
    #     # print("In find User--------")
    #     print(user)
    #     print(type(user))
    #     return user

    async def find_user_by_id(id: ObjectId):
        user = await user_collection.find_one({"_id": id})
        print("In find User--------")
        print(user)
        print(type(user))
        return user

    @staticmethod
    async def update_user_password(id: ObjectId, password: str):
        # updated_user = await user_collection.update_one(
        #     {"_id": id}, {"$set": password}
        # )
        updated_user = await user_collection.update_one(
            {"_id": id}, {"$set": {"password": password}}
        )
        # return updated_user

    # user = db.query(Users).filter(Users.username == username).first()
    # if not user:
    #     return False
    # if not bcrypt_context.verify(password, user.hashed_password):
    #     return False
    # return user

    # @staticmethod
    # async def update_user_password(self, id: ObjectId, password: str):
    #     if len(password) < 1:
    #         raise Htt
    #
    #     if len(data) < 1:
    #         return False
    #     student = await student_collection.find_one({"_id": ObjectId(id)})
    #     if student:
    #         updated_student = await student_collection.update_one(
    #             {"_id": ObjectId(id)}, {"$set": data}
    #         )
    #         if updated_student:
    #             return True
    #         return False
