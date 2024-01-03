from typing import TypeVar, Generic
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class UserResponse(BaseModel, Generic[T]):
    resp: str = "in user response"
    content: T | None = None


class UserMongoSchema(BaseModel):
    firstName: str
    lastName: str
    email: str
    mobileNumber: int

class ActualUserMongoSchema(BaseModel):
    firstName:str
    lastName:str
    email:str
    password:str
    mobileNumber:int




