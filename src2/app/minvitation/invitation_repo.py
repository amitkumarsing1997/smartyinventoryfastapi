from src2.app.config.mongo_config import database
from src2.app.muser.user_schema import UserMongoSchema
from fastapi.encoders import jsonable_encoder
invitation_collection = database.get_collection("invitation_collection")
from bson import ObjectId
class InvitationRepoMongo:
    @staticmethod
    async def insert_invitation_detail(invitation_data:dict):
        pymongo_invitaion_obj = await invitation_collection.insert_one(invitation_data)
        # print(pymongo_invitaion_obj)
        return pymongo_invitaion_obj


    @staticmethod
    async def get_invitation_document(id:ObjectId):
        invitation_user = await invitation_collection.find_one({"_id":id})
        return invitation_user

    @staticmethod
    async def find_token_details(token:str):
        invitation_doc = await invitation_collection.find_one({"token":token})
        # print("in token static method :::::")
        # print(invitation_doc)
        return invitation_doc





