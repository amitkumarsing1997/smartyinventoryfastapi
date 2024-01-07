from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from passlib.context import CryptContext
from starlette import status

SECRET_KEY = '1b12971d44e18538e9cd51020e0588718c59d21ee962bcb0f0e78694bb682b69'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/authmain/token')
print("in auth config")
# print(oauth2_bearer.success)
token_str = Annotated[str,Depends(oauth2_bearer)]
print(token_str)