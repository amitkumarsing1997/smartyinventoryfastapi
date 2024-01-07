from datetime import timedelta,datetime
from fastapi import HTTPException,status
from src2.app.config.authkeymain import bcrypt_context
# from src2.app.config.mongoauthkey import bcrypt_context
from src2.app.exception.custom_exception import GenericException


# from src2.app.mongoauth.mongoauth_repo import MongoAuthRepo


from src2.app.config.authkeymain import SECRET_KEY,ALGORITHM
# from src2.app.config.mongoauthkey import SECRET_KEY,ALGORITHM
from jose import jwt, JWTError
from typing import Annotated
from fastapi import Depends
from src2.app.config.authkeymain import oauth2_bearer
# from src2.app.config.mongoauthkey import oauth2_bearer


#for authenticate user

# async def authenticate_user(username, password):
#     userobj = await MongoAuthRepo.find_user({"email": username})
#     if not userobj:
#         raise GenericException(msg="user email incorrect", msg_code="500")
#     if not bcrypt_context.verify(password, userobj.get("password")):
#         raise GenericException(msg="user password incorrect", msg_code="500")
#     return userobj

# to create token

def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta) -> str:
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


# async def create_access_token(username:str,first_name:str,expires_delta:timedelta):
#     encode={'username':username,'first_name':first_name}
#     expires = datetime.utcnow() + expires_delta
#     encode.update({'exp':expires})
#     return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)




async def get_current_user(token: Annotated[str,Depends(oauth2_bearer)]) -> dict:
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

