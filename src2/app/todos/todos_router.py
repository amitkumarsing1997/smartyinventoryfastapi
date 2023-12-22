import logging
from fastapi import FastAPI, APIRouter, Depends, Form
from typing import Annotated
from src2.app.todos.todos_iservice import ITodosService
from src2.app.todos.todos_service import TodosService
from src2.app.config.db_config import db_dependency
from src2.app.config.authkey import token_str
from src2.app.config.authkey import oauth2_bearer, get_current_user

todosRouter = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

TodosServiceIns = Annotated[ITodosService, Depends(TodosService)]

token_str = Annotated[str, Depends(oauth2_bearer)]


# print(token_str)
# @todosRouter.get("/gettodos")
# async def get_todos(token:token_str,db:db_dependency,service:TodosServiceIns):
#     await service.read_all_todos(token,db)
#     print("in todosRouter of get function")
#

@todosRouter.get("/get/")
async def get_todos():
    return [{"item": "Foo"}, {"item": "Bar"}]

# ///////////////////////////

#
# import logging
# from fastapi import FastAPI, APIRouter, Depends, Form
# from pydantic import BaseModel
# from src2.app.models.models import Users
# from src2.app.config.db_config import SessionLocal
# from typing import Annotated
# from sqlalchemy.orm import Session
# from starlette import status
# from src2.app.user.user_schema import CreateUserRequest
# from src2.app.user.user_repo import UserRepo
# from src2.app.shared.response import CreateUserResponse, Response
# from src2.app.user.user_iservice import IUserService
# from src2.app.user.user_service import UserService
# from src2.app.auth.auth_iservice import IAuthService
# from src2.app.auth.auth_iservice import IAuthService
# from src2.app.auth.auth_service import AuthService
# from src2.app.auth.auth_schema import Token, AuthResponse, UserRespSchema
# from passlib.context import CryptContext
# from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
# from jose import jwt, JWTError
# from OpenSSL import SSL
# from src2.app.config.authkey import bcrypt_context, SECRET_KEY, ALGORITHM
# # from src2.app.config.db_config import Database
# from src2.app.config.db_config import db_dependency
# from src2.app.exception.custom_exception import GenericException
#
#
#
# log = logging.getLogger()
#
# authRouter = APIRouter(
#     prefix='/auth',
#     tags=['Auth']
# )
#
# # SECRET_KEY='1b12971d44e18538e9cd51020e0588718c59d21ee962bcb0f0e78694bb682b69'
# # ALGORITHM='HS256'
#
#
# # bcrypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')
#
# # oauth2_bearer=OAuth2PasswordBearer(tokenUrl='auth/token')
#
# # def get_db():
# #     db=SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()
# #
# # db_dependency=Annotated[Session,Depends(get_db)]
#
# AuthServiceIns = Annotated[IAuthService, Depends(AuthService)]
#
# @authRouter.post("/register/person",status_code=status.HTTP_201_CREATED,response_model=Response[AuthResponse])
# async def create_user(
#     create_user_request: CreateUserRequest,
#     db:db_dependency,
#     service: AuthServiceIns
# ):
#     await service.reg_user(create_user_request,db)
#     print("hello amit")
#     log.debug(f" RES OF result : : {await service.reg_user(create_user_request,db)}")
#     return Response[AuthResponse](body = await service.reg_user(create_user_request,db))
#
# @authRouter.post("/login/user",status_code=status.HTTP_202_ACCEPTED,response_model=Response[AuthResponse[UserRespSchema]])
# async def login(username: Annotated[str, Form()],
#                 password: Annotated[str, Form()],
#                 db:db_dependency,
#                 service:AuthServiceIns):
#     log.debug(f" USER Email is : : {await service.auth_user(username,password,db)}")
#     print("in User ROUTER----->")
#
#     user_auth = await service.auth_user(username,password,db)
#     return Response[AuthResponse[UserRespSchema]](body = await service.auth_user(username,password,db))
#
#
# @authRouter.post("/token", response_model=Token)
# async def login_for_access_token(
#          form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
#         service:AuthServiceIns,
#         db: db_dependency):
#      return await service.login_get_access_token(form_data.username, form_data.password, db)
#
#
#
#
#
# /////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# # @authRouter.post("/token", response_model=Token)
# # async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
# #                                  db: db_dependency):
# #     user = authenticate_user(form_data.username, form_data.password, db)
# #     if not user:
# #         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
# #                             detail='Could not validate user. ')
# #     token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
# #     return {'access_token': token, 'token_type': 'bearer'}
#
#
#
#
#
#
# from typing import Annotated
# from pydantic import BaseModel, Field
# from sqlalchemy.orm import Session
# # from fastapi import FastAPI,Depends, HTTPException,Path
# from fastapi import APIRouter, Depends, HTTPException, Path
# import models
# from models import Todos
# # from database import engine,SessionLocal
# from database import SessionLocal
# # from routers import auth
# import starlette.status as status
# from .auth import get_current_user
#
# # app=FastAPI()
# router = APIRouter()
#
#
# # models.Base.metadata.create_all(bind=engine)
#
# # app.include_router(auth.router)
#
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# db_dependency = Annotated[Session, Depends(get_db)]
#
# user_dependency = Annotated[dict, Depends(get_current_user)]
#
#
# ## for video 94
# class TodoRequest(BaseModel):
#     title: str = Field(min_length=3)
#     description: str = Field(min_length=3, max_length=100)
#     priority: int = Field(gt=0, lt=6)
#     complete: bool
#
#
# # video 92   get all todos from database
# # @app.get("/",status_code=starlette.status.HTTP_200_OK)
# # async def read_all(db: db_dependency):
# #     return db.query(Todos).all()
#
# @router.get("/", status_code=status.HTTP_200_OK)
# async def read_all(user: user_dependency, db: db_dependency):
#     if user is None:
#         raise HTTPException(status_code=401, detail='Authentication Failed')
#     return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()
#
#
# # video 93 get todo by id
#
# # @app.get("/todo/{todo_id}",status_code=starlette.status.HTTP_200_OK)
# # async def read_todo(db: db_dependency,todo_id:int=Path(gt=0)):
# #     todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
# #     if todo_model is not None:
# #         return todo_model
# #     raise HTTPException(status_code=404,detail='Todo not found.')
#
#
# @router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
# async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
#     if user is None:
#         raise HTTPException(status_code=401, detail='Authentication Failed')
#     todo_model = db.query(Todos).filter(Todos.id == todo_id) \
#         .filter(Todos.owner_id == user.get('id')).first()
#     if todo_model is not None:
#         return todo_model
#     raise HTTPException(status_code=404, detail='Todo not found.')
#
#
# # video 94 post request
#
# # @app.post("/todo",status_code=starlette.status.HTTP_201_CREATED)
# # async def create_todo(db:db_dependency,todo_request:TodoRequest):
# #     todo_model=Todos(**todo_request.model_dump())
# #     db.add(todo_model)
# #     db.commit()
#
# @router.post("/todo", status_code=status.HTTP_201_CREATED)
# async def create_todo(user: user_dependency, db: db_dependency,
#                       todo_request: TodoRequest):
#     if user is None:
#         raise HTTPException(status_code=401, detail='Authentication Failed')
#     todo_model = Todos(**todo_request.model_dump(), owner_id=user.get('id'))
#     db.add(todo_model)
#     db.commit()
#
#
# # video 95 put request
# # @app.put("/todo/{todo_id}",status_code=starlette.status.HTTP_204_NO_CONTENT)
# # async def update_todo(db:db_dependency,
# #                       todo_request:TodoRequest,
# #                       todo_id:int=Path(gt=0)):
# #     todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
# #     if todo_model is None:
# #         raise HTTPException(status_code=404,detail='Todo not found.')
#
# #     todo_model.title=todo_request.title
# #     todo_model.description=todo_request.description
# #     todo_model.priority=todo_request.priority
# #     todo_model.complete=todo_request.complete
#
# #     db.add(todo_model)
# #     db.commit()
#
#
# @router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def update_todo(user: user_dependency,
#                       db: db_dependency,
#                       todo_request: TodoRequest,
#                       todo_id: int = Path(gt=0)):
#     if user is None:
#         raise HTTPException(status_code=401, detail='Authentication Failed')
#     todo_model = db.query(Todos).filter(Todos.id == todo_id) \
#         .filter(Todos.owner_id == user.get('id')).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail='Todo not found.')
#
#     todo_model.title = todo_request.title
#     todo_model.description = todo_request.description
#     todo_model.priority = todo_request.priority
#     todo_model.complete = todo_request.complete
#
#     db.add(todo_model)
#     db.commit()
#
#
# # video 96 delete request
# # @app.delete("/todo/{todo_id}",status_code=starlette.status.HTTP_204_NO_CONTENT)
# # async def delete_todo(db:db_dependency,todo_id:int=Path(gt=0)):
# #     todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
# #     if todo_model is None:
# #         raise HTTPException(status_code=404,detail='Todo not foound.')
# #     db.query(Todos).filter(Todos.id==todo_id).delete()
# #     db.commit()
#
#
# @router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
#     if user is None:
#         raise HTTPException(status_code=401, detail='Authentication Failed')
#     todo_model = db.query(Todos).filter(Todos.id == todo_id). \
#         filter(Todos.owner_id == user.get('id')).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail='Todo not foound.')
#     db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).delete()
#     db.commit()
#
#
# 1
