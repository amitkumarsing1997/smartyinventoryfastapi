from fastapi import APIRouter, Depends, Form, HTTPException
from typing import Annotated

from starlette import status
from starlette.responses import JSONResponse

from src2.app.mongoauth.util.mongo_util import authenticate_user, get_current_user
from src2.app.muser.user_schema import UserMongoSchema
from src2.app.mongoauth.mongoauth_iservice import IMongoAuthService
from src2.app.mongoauth.mongoauth_service import MongoAuthService
from src2.app.mongoauth.mongoauth_schema import Token

mongoAuthRouter = APIRouter(prefix="/usermongoauth", tags=["MONGO_AUTH"])

MongoAuthServiceIns = Annotated[IMongoAuthService, Depends(MongoAuthService)]


@mongoAuthRouter.post("/login/user")
async def login(username: Annotated[str, Form()],
                password: Annotated[str, Form()],
                service: MongoAuthServiceIns):
    user_auth = await service.authenticate_user_inservice(username, password)
    return JSONResponse(status_code=200, content={"message": "user has been authenticated"})


@mongoAuthRouter.post("/createaccesstoken", response_model=Token)
async def login_for_access_token(username: Annotated[str, Form()],
                                 password: Annotated[str, Form()],
                                 service: MongoAuthServiceIns):
    user_auth = await service.authenticate_user_inservice(username, password)
    print("in mongo Auth Router-----------")
    print(type(user_auth))
    token = await service.create_access_token(user_auth.get("email"), user_auth.get("firstName"))
    return token


user_dependency = Annotated[dict, Depends(get_current_user)]


@mongoAuthRouter.get("/getcurrentuser", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return user

# @router.get("/todo",status_code=status.HTTP_200_OK)
# async def read_all(user:user_dependency,db:db_dependency):
#     if user is None or user.get('user_role')!='admin':
#         raise HTTPException(status_code=401,detail='Authentication Failed')
#     return db.query(Todos).all()


# @router.post("/token",response_model=Token)
# async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
#                                  db:db_dependency):
#     user=authenticate_user(form_data.username,form_data.password,db)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail='Could not validate user. ')
#     token=create_access_token(user.username,user.id,user.role,timedelta(minutes=20))
#     return {'access_token':token,'token_type':'bearer'}
