

from typing import TypeVar,Generic
from pydantic import BaseModel


T = TypeVar('T',bound=BaseModel)


class UserResponse(BaseModel,Generic[T]):
    resp:str="in user schema"
    content: T | None = None


class CreateUserRequest(BaseModel):
    username:str
    email:str
    first_name:str
    last_name:str
    password:str
    role:str

class UserRespSchema(BaseModel):
    id:int
    email:str
    username:str
    first_name:str
    last_name:str
    role:str

class UserVerification(BaseModel):
    password:str
    new_password:str

class Token(BaseModel):
    access_token:str
    token_type:str





# # ######
#
# from pydantic import BaseModel, Field
#
#
# class CreateUserRequest(BaseModel):
#     username:str
#     email:str
#     first_name:str
#     last_name:str
#     password:str
#     role:str
#
# class Token(BaseModel):
#     access_token:str
#     token_type:str
#
#
# #Pydentic class for verification
# class UserVerification(BaseModel):
#     password:str
#     new_password:str=Field(min_length=6)
#
#
# # from database import Base
#
# # from src.app.config.db_config import Base
# # from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
#
#
# # class Users(Base):
# #     __tablename__='users'
# #     id=Column(Integer,primary_key=True,index=True)
# #     email=Column(String,unique=True)
# #     username=Column(String,unique=True)
# #     first_name=Column(String)
# #     last_name=Column(String)
# #     hashed_password=Column(String)
# #     is_active=Column(Boolean,default=True)
# #     role=Column(String)
#
# # class Todos(Base):
# #     __tablename__='todos'
#
# #     id=Column(Integer,primary_key=True,index=True)
# #     title=Column(String)
# #     description=Column(String)
# #     priority=Column(Integer)
# #     complete=Column(Boolean,default=False)
# #     owner_id=Column(Integer,ForeignKey("users.id"))
#
#
#
#
# # class Account(Base):
# #     __tablename__='account'
# #     id = Column(Integer,primary_key=True,index=True)
# #     acc_name = Column(String,unique=True)
# #     address = Column(String)
#
# # # id bigint AI PK
# # # uid varchar(50)
# # # email varchar(255)
# # # full_name varchar(255)
# # # password varchar(500)
# # # user_status varchar(30)
# # # user_type varchar(20)
# # # user_name varchar(50)
# # # acc_id bigint
#
# # class User(Base):
# #     __tablename__='user'
# #     id = Column(Integer,primary_key=True,index=True)
# #     email = Column(String,unique=True)
# #     full_name = Column(String)
# #     password = Column(String)
# #     user_status = Column(String)
# #     user_type = Column(String)
# #     user_name = Column(String)
# #     acc_id = Column(Integer,ForeignKey("account.id"))
