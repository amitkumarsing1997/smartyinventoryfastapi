

from bson.objectid import ObjectId
from fastapi import HTTPException
import datetime
import uuid
# from app.server.exception.handler import GenericException
from src2.app.exception.custom_exception import GenericException

import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database = client.students
#
# student_collection = database.get_collection("students_collection")

database = client.userdetails

user_collection = database.get_collection("user_collection")

invitation_collection = database.get_collection("invitation_collection")

# from app.server.user.user_schema import UserSchema
#
#
#
# async def add_user(user_data: UserSchema):
#     print(type(user_data))
#     email = user_data.get("email")
#     # print("email is : :")
#     # print(email)
#     find_user = await user_collection.find_one({"email":email})
#     if find_user:
#         # raise HTTPException(status_code=500,detail="user email already present")
#         raise GenericException(msg="user email alrady present",msg_code="500")
#     user_inserted = await user_collection.insert_one(user_data)
#     invitation_inserted = await invitation_collection.insert_one({
#         "userId":user_inserted.inserted_id,
#         "token": str(uuid.uuid4()),
#         "status":"ACTIVE",
#         "expire_on":datetime.datetime.now()
#     })
#     print(user_inserted.inserted_id)
#     print(type(invitation_inserted.inserted_id))
#     invitation_user = await invitation_collection.find_one({"_id":invitation_inserted.inserted_id})
#     print(invitation_user.get("token"))
#     return invitation_user.get("token")








