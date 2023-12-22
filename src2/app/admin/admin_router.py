import logging
from fastapi import FastAPI, APIRouter, Depends, Form, HTTPException, Path
from pydantic import BaseModel

from src2.app.admin.admin_schema import AdminTodoRespSchema, AdminResponse
from src2.app.models.models import Users, Todos
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
from src2.app.auth.auth_schema import Token
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from OpenSSL import SSL
from src2.app.config.authkey import bcrypt_context, SECRET_KEY, ALGORITHM, token_str
# from src2.app.config.db_config import Database
from src2.app.config.db_config import db_dependency
from src2.app.admin.admin_iservice import IAdminService
from src2.app.admin.admin_service import AdminService



log = logging.getLogger()

adminRouter = APIRouter(
    prefix='/admin',
    tags=['Admin']
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
UserServiceIns = Annotated[IUserService,Depends(UserService)]
AdminServiceIns = Annotated[IAdminService,Depends(AdminService)]




@adminRouter.get("/todo",status_code=status.HTTP_200_OK,response_model=Response[AdminResponse[list[AdminTodoRespSchema]]])
async def read_all(token:token_str,service:AdminServiceIns,db: db_dependency)->Response[AdminResponse[list[AdminTodoRespSchema]]]:
    admin_resp_sch = await service.get_list_all_todos(token,db)
    return Response[AdminResponse[list[AdminTodoRespSchema]]](body = admin_resp_sch)
    # user = await service.get_current_user(token)
    # if user is None or user.get('user_role')!='admin':
    #     raise HTTPException(status_code=401, detail='Authentication Failed')
    # return db.query(Todos).all()


@adminRouter.delete("/todo/{todo_id}",response_model=Response[AdminResponse[str]])
async def delete_todo(token:token_str,service:AdminServiceIns,db:db_dependency,todo_id:int=Path(gt=0)):
    admin_resp_sch = await service.deleteselectedid(token,db,todo_id)
    return Response[AdminResponse[str]](body = admin_resp_sch)
    # if user is None or user.get('user_role')!='admin':
    #     raise HTTPException(status_code=401,detail='Authentication Failed')
    # todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
    # if todo_model is None:
    #     raise HTTPException(status_code=404,detail="Todo not found.")
    # db.query(Todos).filter(Todos.id==todo_id).delete()
    # db.commit()
    #

# @router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
# async def delete_todo(user:user_dependency,db:db_dependency,todo_id:int=Path(gt=0)):
#     if user is None or user.get('user_role')!='admin':
#         raise HTTPException(status_code=401,detail='Authentication Failed')
#     todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404,detail="Todo not found.")
#     db.query(Todos).filter(Todos.id==todo_id).delete()
#     db.commit()




# @adminRouter.get("/todo",status_code=status.HTTP_200_OK)
# async def read_all(token:token_str,service:UserServiceIns,db: db_dependency):
#     user = await service.get_current_user(token)
#     if user is None or user.get('user_role')!='admin':
#         raise HTTPException(status_code=401, detail='Authentication Failed')
#     return db.query(Todos).all()




#     # @userRouter.get('/get_current_user', status_code=status.HTTP_200_OK)
#     # async def get_user(token: token_str, service: UserServiceIns, db: db_dependency):
#     #     user = await service.get_current_user(token)
#     #     print("in user router")
#     #     print(user)
#     #     return db.query(Users).filter(Users.id == user.get('id')).first()
#
#
# @router.get("/todo",status_code=status.HTTP_200_OK)
# async def read_all(user:user_dependency,db:db_dependency):
#     if user is None or user.get('user_role')!='admin':
#         raise HTTPException(status_code=401,detail='Authentication Failed')
#     return db.query(Todos).all()



# @router.get("/todo",status_code=status.HTTP_200_OK)
# async def read_all(user:user_dependency,db:db_dependency):
#     if user is None or user.get('user_role')!='admin':
#         raise HTTPException(status_code=401,detail='Authentication Failed')
#     return db.query(Todos).all()




# @router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
# async def delete_todo(user:user_dependency,db:db_dependency,todo_id:int=Path(gt=0)):
#     if user is None or user.get('user_role')!='admin':
#         raise HTTPException(status_code=401,detail='Authentication Failed')
#     todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404,detail="Todo not found.")
#     db.query(Todos).filter(Todos.id==todo_id).delete()
#     db.commit()
#
#
#
#
#
# @adminRouter.post("/register/person",status_code=status.HTTP_201_CREATED,response_model=Token)
# async def create_user(
#     create_user_request: CreateUserRequest,
#      db:db_dependency,
#     service: AuthServiceIns
# ):
#     # print(type(service))
#     await service.reg_user(create_user_request,db)
#     print("hello amit")
#     log.debug(f" RES OF result : : {await service.reg_user(create_user_request,db)}")
#     # print(type(us))
#     # db.add(us)
#     # db.commit()
#     var = await service.reg_user(create_user_request,db)
#     return CreateUserResponse()
#
# @authRouter.post("/login/user",status_code=status.HTTP_202_ACCEPTED,response_model=CreateUserResponse)
# async def login(username: Annotated[str, Form()],
#                 password: Annotated[str, Form()],
#                 db:db_dependency,
#                 service:AuthServiceIns):
#     log.debug(f" USER Email is : : {await service.auth_user(username,password,db)}")
#     print("in User ROUTER----->")
#     var2 = await service.auth_user(username,password,db)
#     print("in User ROUTER----->",var2.email)
#     return CreateUserResponse()
#
#
#
# @authRouter.post("/token", response_model=Token)
# async def login_for_access_token(
#          form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
#         service:AuthServiceIns,
#         db: db_dependency):
#      token = await service.login_get_access_token(form_data.username, form_data.password, db)
#      return {'access_token':token, 'token_type':'bearer'}



# @authRouter.post("/token", response_model=Token)
# async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
#                                  db: db_dependency):
#     user = authenticate_user(form_data.username, form_data.password, db)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail='Could not validate user. ')
#     token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
#     return {'access_token': token, 'token_type': 'bearer'}

