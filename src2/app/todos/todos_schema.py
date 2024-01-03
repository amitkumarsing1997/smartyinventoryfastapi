from typing import TypeVar, Generic

from pydantic import BaseModel, Field

T = TypeVar('T', bound=BaseModel)


class TodosResponse(BaseModel, Generic[T]):
    resp: str = "in todos schema"
    content: T | None = None


class TodoSchema(BaseModel):
    id: int
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: int
    owner_id: int


class TodoRequestSchema(BaseModel):
    title:str=Field(min_length=3)
    description:str=Field(min_length=3,max_length=100)
    priority:int=Field(gt=0,lt=6)
    complete:bool
