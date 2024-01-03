from fastapi import APIRouter, Depends, Form
from typing import Annotated

from starlette.responses import JSONResponse

from src2.app.muser.user_iservice import IUserServiceMongo
from src2.app.muser.user_service import UserServiceMongo
from src2.app.muser.user_schema import UserMongoSchema

userRouterMongo = APIRouter(prefix="/usermongo", tags=["MONGO"])

UserServiceMongoIns = Annotated[IUserServiceMongo, Depends(UserServiceMongo)]
@userRouterMongo.post("/save")
async def insertUserIfNotPresentInCollection(userschema: UserMongoSchema, service: UserServiceMongoIns) -> JSONResponse:
    await service.insert_user_if_not_present_in_collecton(userschema)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


@userRouterMongo.post("/login/user")
async def login(username: Annotated[str, Form()],
                password: Annotated[str, Form()],
                service:UserServiceMongoIns):
    user_auth = await service.authenticate_user(username,password)
    return JSONResponse(status_code=200 , content={"message": "user has been authenticated"})


