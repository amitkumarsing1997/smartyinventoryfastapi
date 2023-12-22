

from src2.app.user.user_iservice import IUserService
from src2.app.user.user_repo import UserRepo
from fastapi import Depends
from src2.app.user.user_schema import CreateUserRequest
from src2.app.config.db_config import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from src2.app.user.user_repo import UserRepo
from src2.app.models.models import Users
from sqlalchemy.orm import Session
# open_ai: OpenAI = Depends() 


class UserService(IUserService):
    def __init__(self, userrepo: UserRepo = Depends()) -> None:
        super().__init__()
        self.userrepo = userrepo

    async def auth_user(self,username:str,password:str,db:Session)->Users:
        print("in user service")
        print(type(db))
        return await self.userrepo.authenticate_user(username,password,db)
        print("hiiifhfi",var.email)


    async def get_current_user(self,token:str)-> dict:
        return await self.userrepo.get_current_user(token)


    
