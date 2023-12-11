from fastapi import FastAPI,APIRouter,Depends
from pydantic import BaseModel
from src2.app.models.models import Users
from src2.app.config.db_config import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from src2.app.user.user_schema import CreateUserRequest
from src2.app.user.user_repo import UserRepo
from src2.app.shared.response import CreateUserResponse
from src2.app.user.user_iservice import IUserService
from src2.app.user.user_service import UserService


userrouter=APIRouter(
    #video 110
    prefix='/user',
    tags=['User']
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

# Userrepo_obj=Annotated[UserRepo,Depends(get_db)]

# def get_user_repo(db: Session = Depends(get_db)) -> UserRepo:
#     return UserRepo(db)





UserServiceIns = Annotated[IUserService, Depends(UserService)]


@userrouter.post("/",status_code=status.HTTP_201_CREATED,response_model=CreateUserResponse)
async def create_user(
    create_user_request: CreateUserRequest,
     db:db_dependency,
    service:UserServiceIns
):
    # print(type(service))
    us=await service.reg_user(create_user_request)
    print("hello amit")
    print(type(us))
    db.add(us)
    db.commit()
    return CreateUserResponse()




# @userrouter.post("/", status_code=status.HTTP_201_CREATED,response_model=CreateUserResponse)
# async def create_user(
#     create_user_request: CreateUserRequest,
#     user_repo: UserRepo = Depends(get_user_repo)
# ):
#     await user_repo.create_user(create_user_request)
#     return CreateUserResponse()



# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# db_dependency = Depends(get_db)

# def get_user_repo() -> UserRepo:
#     return UserRepo()

# userrepo_obj = Depends(get_user_repo)


# @userrouter.post("/", status_code=status.HTTP_201_CREATED, response_model=CreateUserResponse)
# async def create_user(create_user_request: CreateUserRequest, user_repo:Userrepo_obj):
#     await user_repo.create_user(create_user_request)
#     return CreateUserResponse()


# class CreateUserRequest(BaseModel):
#     username:str
#     email:str
#     first_name:str
#     last_name:str
#     password:str
#     role:str


# @userrouter.post("/",status_code=status.HTTP_201_CREATED)
# async def create_user(db:db_dependency,
#                       create_user_request: CreateUserRequest):
#     create_user_model=Users(
#         email=create_user_request.email,
#         username=create_user_request.username,
#         first_name=create_user_request.first_name,
#         last_name=create_user_request.last_name,
#         role=create_user_request.role,
#         hashed_password=create_user_request.password,
#         # hashed_password=bcrypt_context.hash(create_user_request.password),
#         is_active=True
#     )
#     db.add(create_user_model)
#     db.commit()





