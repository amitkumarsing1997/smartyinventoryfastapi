# from fastapi import FastAPI,APIRouter

# app=FastAPI()



from fastapi import APIRouter,Depends, HTTPException
from pydantic import BaseModel
from models import Users
from passlib.context import CryptContext
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt,JWTError
# from OpenSSL import SSL
from datetime import timedelta,datetime


router=APIRouter(
    #video 110
    prefix='/auth',
    tags=['auth']
)

# for jwt it is very important to generate token it is secret_key and algorithm

# SECRET_KEY='1b12971d44e18538e9cd51020e0588718c59d21ee962bcb0f0e78694bb682b69'
# ALGORITHM='HS256'


#later search it by chatgpt
# bcrypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

# oauth2_bearer=OAuth2PasswordBearer(tokenUrl='auth/token')


class CreateUserRequest(BaseModel):
    username:str
    email:str
    first_name:str
    last_name:str
    password:str
    role:str

class Token(BaseModel):
    access_token:str
    token_type:str

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency=Annotated[Session,Depends(get_db)]
print("##########")
print(type(db_dependency))

# #for authenticate user
# def authenticate_user(username:str,password:str,db):
#     user=db.query(Users).filter(Users.username==username).first()
#     if not user:
#         return False
#     if not bcrypt_context.verify(password,user.hashed_password):
#         return False
#     return user

# # to create token
# def create_access_token(username: str,user_id:int,role:str,expires_delta:timedelta):
#     encode={'sub':username,'id':user_id,'role':role}
#     expires=datetime.utcnow()+expires_delta
#     encode.update({'exp':expires})
#     return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

## video 109

# async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
#     try:
#         payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
#         username:str=payload.get('sub')
#         user_id:int=payload.get('id')
#         user_role:str=payload.get('role')
#         if username is None or user_id is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                                 detail='Could not validate user: ')
#         return {'username':username,'id':user_id,'user_role':user_role}
#     except JWTError:
#          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                                 detail='Could not validate user: ')


            





@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,
                      create_user_request: CreateUserRequest):
    create_user_model=Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=create_user_request.password,
        # hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )
    print(type(db))
    db.add(create_user_model)
    db.commit()


# @router.post("/token",response_model=Token)
# async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
#                                  db:db_dependency):
#     user=authenticate_user(form_data.username,form_data.password,db)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail='Could not validate user. ')
#     token=create_access_token(user.username,user.id,user.role,timedelta(minutes=20))
#     return {'access_token':token,'token_type':'bearer'}
   


