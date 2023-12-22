import logging
from fastapi import FastAPI, APIRouter, Depends, Form
from pydantic import BaseModel
from src2.app.models.models import Users
from src2.app.config.db_config import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from src2.app.user.user_schema import CreateUserRequest
from src2.app.user.user_repo import UserRepo
from src2.app.shared.response import CreateUserResponse, Response
from src2.app.user.user_iservice import IUserService
from src2.app.user.user_service import UserService
from src2.app.auth.auth_iservice import IAuthService
from src2.app.auth.auth_iservice import IAuthService
from src2.app.auth.auth_service import AuthService
from src2.app.auth.auth_schema import Token, AuthResponse, UserRespSchema
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from OpenSSL import SSL
from src2.app.config.authkey import bcrypt_context, SECRET_KEY, ALGORITHM
# from src2.app.config.db_config import Database
from src2.app.config.db_config import db_dependency
from src2.app.exception.custom_exception import GenericException



log = logging.getLogger()

authRouter = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

# SECRET_KEY='1b12971d44e18538e9cd51020e0588718c59d21ee962bcb0f0e78694bb682b69'
# ALGORITHM='HS256'


# bcrypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

# oauth2_bearer=OAuth2PasswordBearer(tokenUrl='auth/token')

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# db_dependency=Annotated[Session,Depends(get_db)]

AuthServiceIns = Annotated[IAuthService, Depends(AuthService)]

@authRouter.post("/register/person",status_code=status.HTTP_201_CREATED,response_model=Response[AuthResponse])
async def create_user(
    create_user_request: CreateUserRequest,
    db:db_dependency,
    service: AuthServiceIns
):
    # await service.reg_user(create_user_request,db)
    # print("hello amit")
    # log.debug(f" RES OF result : : {await service.reg_user(create_user_request,db)}")
    return Response[AuthResponse](body = await service.reg_user(create_user_request,db))

@authRouter.post("/login/user",status_code=status.HTTP_202_ACCEPTED,response_model=Response[AuthResponse[UserRespSchema]])
async def login(username: Annotated[str, Form()],
                password: Annotated[str, Form()],
                db:db_dependency,
                service:AuthServiceIns):
    log.debug(f" USER Email is : : {await service.auth_user(username,password,db)}")
    print("in User ROUTER----->")

    user_auth = await service.auth_user(username,password,db)
    return Response[AuthResponse[UserRespSchema]](body = await service.auth_user(username,password,db))


@authRouter.post("/token", response_model=Token)
async def login_for_access_token(
         form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        service:AuthServiceIns,
        db: db_dependency):
     return await service.login_get_access_token(form_data.username, form_data.password, db)







# @authRouter.post("/token", response_model=Token)
# async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
#                                  db: db_dependency):
#     user = authenticate_user(form_data.username, form_data.password, db)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail='Could not validate user. ')
#     token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
#     return {'access_token': token, 'token_type': 'bearer'}

