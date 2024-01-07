from fastapi import APIRouter, Depends, Form, HTTPException
from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from starlette.responses import JSONResponse

from src2.app.authmain.authmain_schema import AuthResponse, UserRespSchema
from src2.app.authmain.util.authmain_util import get_current_user
from src2.app.muser.user_schema import UserMongoSchema
from src2.app.authmain.authmain_iservice import IAuthMainService
from src2.app.authmain.authmain_service import AuthMainService
# from src2.app.mongoauth.mongoauth_iservice import IMongoAuthService
# from src2.app.mongoauth.mongoauth_service import MongoAuthService
from src2.app.mongoauth.mongoauth_schema import Token
from src2.app.shared.response import Response
from src2.app.user.user_schema import CreateUserRequest
from src2.app.config.db_config import db_dependency

authMainRouter = APIRouter(
    prefix='/authmain',
    tags=['AuthMain']
)

AuthMainServiceIns = Annotated[IAuthMainService,Depends(AuthMainService)]


# mongoAuthRouter = APIRouter(prefix="/usermongoauth", tags=["MONGO_AUTH"])
#
# MongoAuthServiceIns = Annotated[IMongoAuthService, Depends(MongoAuthService)]

user_dependency=Annotated[dict,Depends(get_current_user)]


@authMainRouter.post("/register/person",status_code=status.HTTP_201_CREATED,response_model=Response[AuthResponse])
async def create_user(
    create_user_request: CreateUserRequest,
    db:db_dependency,
    service: AuthMainServiceIns
):
    return Response[AuthResponse](body = await service.reg_user(create_user_request,db))


@authMainRouter.post("/login/user",status_code=status.HTTP_202_ACCEPTED,response_model=Response[AuthResponse[UserRespSchema]])
async def login(username: Annotated[str, Form()],
                password: Annotated[str, Form()],
                db:db_dependency,
                service:AuthMainServiceIns):
    user_auth = await service.auth_user(username,password,db)
    return Response[AuthResponse[UserRespSchema]](body = user_auth)


@authMainRouter.post("/token", response_model=Token)
async def login_for_access_token(
         username:Annotated[str, Form()],
        password:Annotated[str,Form()],
        service:AuthMainServiceIns,
        db: db_dependency):
     return service.login_get_access_token(username,password, db)



@authMainRouter.get("/getcurrentuser",status_code=status.HTTP_200_OK)
async def read_all(user:user_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    return user




