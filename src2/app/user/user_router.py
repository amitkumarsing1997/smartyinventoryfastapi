import logging
from fastapi import FastAPI, APIRouter, Depends, Form, HTTPException
from pydantic import BaseModel
from src2.app.models.models import Users
from src2.app.config.db_config import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from src2.app.user.user_schema import UserVerification
from src2.app.user.user_repo import UserRepo
from src2.app.shared.response import CreateUserResponse
from src2.app.user.user_iservice import IUserService
from src2.app.user.user_service import UserService
from src2.app.config.db_config import db_dependency
from src2.app.config.authkey import oauth2_bearer,token_str
from src2.app.shared.response import Response
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from OpenSSL import SSL
from src2.app.config.authkey import bcrypt_context, SECRET_KEY, ALGORITHM
# from src2.app.config.db_config import Database

log = logging.getLogger()

userRouter = APIRouter(
    # video 110
    prefix='/user',
    tags=['User']
)

# SECRET_KEY='1b12971d44e18538e9cd51020e0588718c59d21ee962bcb0f0e78694bb682b69'
# ALGORITHM='HS256'


# bcrypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

# oauth2_bearer=OAuth2PasswordBearer(tokenUrl='auth/token')


UserServiceIns = Annotated[IUserService, Depends(UserService)]
# user_dependency=Annotated[dict,Depends(get_current_user)]




@userRouter.get('/get_current_user',status_code=status.HTTP_200_OK)
async def get_user(token:token_str,service:UserServiceIns,db:db_dependency):
    user = await service.get_current_user(token)
    print("in user router")
    print(user)
    return db.query(Users).filter(Users.id==user.get('id')).first()



@userRouter.put("/password",response_model=Response[str])
async def change_password(token:token_str,
                          service:UserServiceIns,db:db_dependency,
                          user_verification:UserVerification):
    user = await service.get_current_user(token)
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication Failed")
    user_model=db.query(Users).filter(Users.id==user.get('id')).first()

    if not bcrypt_context.verify(user_verification.password,user_model.hashed_password):
        raise HTTPException(status_code=401,detail="Error on password change")
    user_model.hashed_password=bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()
    return Response[str](body="password changed successfully....")






