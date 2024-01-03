from abc import ABC, abstractmethod

from src2.app.todos.todos_schema import TodosResponse, TodoSchema


class ITodosService(ABC):
    async def read_all_todos(self,token,db)->TodosResponse[list[TodoSchema]]:
        pass

    async def get_todo_by_id(self,token,db,todo_id)->TodosResponse[TodoSchema]:
        pass


    async def createTodo(self,token,db,todo_request)->TodosResponse[str]:
        pass


    async def update_todo_by_id(self,token, db, todo_request,todo_id)->TodosResponse[str]:
        pass

    async def delete_todo_by_id(self,token,db,todo_id)->TodosResponse[str]:
        pass
