import logging
from fastapi import FastAPI, APIRouter, Depends, Form,Path
from typing import Annotated

from src2.app.shared.response import Response
from src2.app.todos.todos_iservice import ITodosService
from src2.app.todos.todos_schema import TodosResponse, TodoSchema,TodoRequestSchema
from src2.app.todos.todos_service import TodosService
from src2.app.config.db_config import db_dependency
from src2.app.config.authkey import token_str
from src2.app.config.authkey import oauth2_bearer, get_current_user

todosRouter = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

TodosServiceIns = Annotated[ITodosService, Depends(TodosService)]

@todosRouter.get("/gettodos",response_model=Response[TodosResponse[list[TodoSchema]]])
async def get_todos(token:token_str,db:db_dependency,service:TodosServiceIns)->Response[TodosResponse[list[TodoSchema]]]:
    todo_resp_sch = await service.read_all_todos(token,db)
    print(type(todo_resp_sch))
    return Response[TodosResponse[list[TodoSchema]]](body = todo_resp_sch)

@todosRouter.get("/todo/{todo_id}",response_model=Response[TodosResponse[TodoSchema]])
async def read_todo(token:token_str,db: db_dependency, service:TodosServiceIns,todo_id: int = Path(gt=0))->Response[TodosResponse[TodoSchema]]:
    todo_resp_sch = await service.get_todo_by_id(token,db,todo_id)
    return Response[TodosResponse[TodoSchema]](body = todo_resp_sch)


@todosRouter.post("/todo",response_model=Response[TodosResponse[str]])
async def create_todo(token:token_str,db: db_dependency,service:TodosServiceIns,
                      todo_request: TodoRequestSchema)->Response[TodosResponse[str]]:
    to_do_model_added = await service.createTodo(token,db,todo_request)
    return Response[TodosResponse[str]](body=to_do_model_added)

@todosRouter.put("/todo/{todo_id}",response_model=Response[TodosResponse[str]])
async def update_todo(token:token_str,db:db_dependency,service:TodosServiceIns,todo_request:TodoRequestSchema,todo_id:int = Path(gt=0),)->Response[TodosResponse[str]]:
    todo_model_updated = await service.update_todo_by_id(token,db,todo_request,todo_id)
    return Response[TodosResponse[str]](body = todo_model_updated)

@todosRouter.delete("/todo/{todo_id}",response_model=Response[TodosResponse[str]])
async def delete_todo(token:token_str,db:db_dependency,service:TodosServiceIns,todo_id:int=Path(gt=0))->Response[TodosResponse[str]]:
    todo_model_deleted = await service.delete_todo_by_id(token,db,todo_id)
    return Response[TodosResponse[str]](body = todo_model_deleted)





