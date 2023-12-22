from typing import TypeVar,Generic
from pydantic import BaseModel


T = TypeVar('T',bound=BaseModel)


class AdminResponse(BaseModel,Generic[T]):
    resp:str="in admin schema"
    content: T | None = None


class AdminTodoRespSchema(BaseModel):
    id:int
    title:str
    description:str
    priority:int
    complete: int
    owner_id:int



# class Todos(Base):
#     __tablename__='todos'
#     id=Column(Integer,primary_key=True,index=True)
#     title=Column(String)
#     description=Column(String)
#     priority=Column(Integer)
#     complete=Column(Boolean,default=False)
#     owner_id=Column(Integer,ForeignKey("users.id"))
