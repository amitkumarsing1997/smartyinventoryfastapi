from typing import TypeVar,Generic
from pydantic import BaseModel


T = TypeVar('T',bound=BaseModel)


class AuthResponse(BaseModel,Generic[T]):
    resp:str="in auth schema"
    content: T | None = None


class UserRespSchema(BaseModel):
    id:int
    email:str
    username:str
    first_name:str
    last_name:str
    role:str


class Token(BaseModel):
    access_token:str
    token_type:str





