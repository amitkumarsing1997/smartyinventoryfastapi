from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, HTTPException
# from jose import jwt, JWTError
# from OpenSSL import SSL
from jose import jwt, JWTError
from starlette import status

SECRET_KEY = '1b12971d44e18538e9cd51020e0588718c59d21ee962bcb0f0e78694bb682b69'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
print("in auth config")
# print(oauth2_bearer.success)
token_str = Annotated[str,Depends(oauth2_bearer)]
print(token_str)




async def get_current_user(self, token: Annotated[str,Depends(oauth2_bearer)]) -> dict:
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


# async def get_current_user(self, token: str) -> dict:
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get('sub')
#         user_id: int = payload.get('id')
#         user_role: str = payload.get('role')
#         if username is None or user_id is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                                 detail='Could not validate user understood amit: ')
#         return {'username': username, 'id': user_id, 'user_role': user_role}
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail='Could not validate userfff: ')








# async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get('sub')
#         user_id: int = payload.get('id')
#         user_role: str = payload.get('role')
#         if username is None or user_id is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                                 detail='Could not validate user: ')
#         return {'username': username, 'id': user_id, 'user_role': user_role}
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail='Could not validate user: ')





