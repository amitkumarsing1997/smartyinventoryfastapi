# from fastapi import Depends, HTTPException
# # from src.app.config.db_config import SessionLocal
# from src2.app.config.db_config import SessionLocal
# from sqlalchemy.orm import Session
# from typing import Annotated
# from src2.app.user.user_schema import CreateUserRequest
# from src2.app.models.models import Users
# from src2.app.config.authkey import bcrypt_context, SECRET_KEY, ALGORITHM, oauth2_bearer
# from jose import jwt, JWTError
# from datetime import timedelta, datetime
# from starlette import status
#
# class AdminRepo:
#     def __init__(self) -> None:
#         pass
#
#     # async def create_user(self, create_user_request: CreateUserRequest, db: Session):
#     #     create_user_model = Users(
#     #         email=create_user_request.email,
#     #         username=create_user_request.username,
#     #         first_name=create_user_request.first_name,
#     #         last_name=create_user_request.last_name,
#     #         role=create_user_request.role,
#     #         # hashed_password=create_user_request.password,
#     #         hashed_password=bcrypt_context.hash(create_user_request.password),
#     #         is_active=True
#     #     )
#     #     db.add(create_user_model)
#     #     db.commit()
#     #     print("hi amit data successfully inserted")
#     #     # return create_user_model
#     #
#     # def authenticate_user(self, username: str, password: str, db: Session) -> Users:
#     #     user = db.query(Users).filter(Users.username == username).first()
#     #     if not user:
#     #         return False
#     #     if not bcrypt_context.verify(password, user.hashed_password):
#     #         return False
#     #     return user
#     #
#     # # to create token
#     #
#     #
#     #
#     # #  to create access token
#     # def create_access_token(self,username: str, user_id: int, role: str, expires_delta: timedelta):
#     #     encode = {'sub': username, 'id': user_id, 'role': role}
#     #     expires = datetime.utcnow() + expires_delta
#     #     encode.update({'exp': expires})
#     #     return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
#     # #
#     #
#     #
#     # async def login_get_access_token(self,username:str,password:str,db:Session)->str:
#     #     user=self.authenticate_user(username,password,db)
#     #     if not user:
#     #         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#     #                             detail='Could not validate user. ')
#     #     token = self.create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
#     #     return token
#
#
#
#     async def get_current_user(self,token: str)->dict:
#         try:
#             payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#             username: str = payload.get('sub')
#             user_id: int = payload.get('id')
#             user_role: str = payload.get('role')
#             if username is None or user_id is None:
#                 raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                                     detail='Could not validate user understood amit: ')
#             return {'username': username, 'id': user_id, 'user_role': user_role}
#         except JWTError:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                                 detail='Could not validate userfff: ')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
