from fastapi import Depends,HTTPException

from src2.app.auth.auth_repo import AuthRepo
# from src.app.config.db_config import SessionLocal
from src2.app.config.db_config import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from src2.app.user.user_schema import CreateUserRequest
from src2.app.models.models import Users
from src2.app.config.authkey import bcrypt_context, SECRET_KEY, ALGORITHM, oauth2_bearer
from jose import jwt,JWTError
from datetime import timedelta,datetime
from starlette import status
# from src2.app.config.db_config import Database

class UserRepo:
    # def __init__(self) -> None:
    #  pass

    def __init__(self) -> None:
        super().__init__()
    
    # async def authenticate_user(self,username:str,password:str,db:Session)->Users:
    #  user=db.query(Users).filter(Users.username==username).first()
    #  if not user:
    #     return False
    #  if not bcrypt_context.verify(password,user.hashed_password):
    #     return False
    #  print(user.email)
    #  return user
    #
    # to create token




    # async def create_access_token(username: str,user_id:int,role:str,expires_delta:timedelta):
    #  encode={'sub':username,'id':user_id,'role':role}
    #  expires=datetime.utcnow()+expires_delta
    #  encode.update({'exp':expires})
    #  return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)


    async def get_current_user(self,token: str)->dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get('sub')
            user_id: int = payload.get('id')
            user_role: str = payload.get('role')
            if username is None or user_id is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail='Could not validate user understood amit: ')
            return {'username': username, 'id': user_id, 'user_role': user_role}
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate userfff: ')

    
    



