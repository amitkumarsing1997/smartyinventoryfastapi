import logging
from src2.app.todos.todos_iservice import ITodosService
from src2.app.todos.todos_schema import TodoSchema, TodosResponse
from src2.app.user.user_repo import UserRepo
from typing import Annotated
from fastapi import Depends,HTTPException
from src2.app.models.models import Todos

log = logging.getLogger()
class TodosService(ITodosService):
    def __init__(self,userRepo:Annotated[UserRepo,Depends()]):
        self.userRepo = userRepo
        print("in todoserviceconstructor")
    async def read_all_todos(self,token,db)->TodosResponse[list[TodoSchema]]:
        print("in todo service")
        print("user is authanticated")
        user = await self.userRepo.get_current_user(token)
        print("after user is called---")
        print(user)
        if user is None:
            raise HTTPException(status_code=401,detail="Authentication Failed")
        dbobj = db.query(Todos).filter(Todos.owner_id == user.get("id")).all()
        print(f"Type :: {type(dbobj[0])}")
        print(f"Method :: {dbobj[0].__dict__}")
        list_obj = [TodoSchema(**obj.__dict__) for obj in dbobj]
        print(f"in todo service --------{list_obj}")
        return TodosResponse[list[TodoSchema]](content = list_obj)


    async def get_todo_by_id(self,token,db,todo_id)->TodosResponse[TodoSchema]:
        user = await self.userRepo.get_current_user(token)
        if user is None:
            raise HTTPException(status_code=401, detail="Authentication Failed")
        todomodel = db.query(Todos).filter(Todos.id==todo_id).filter(Todos.owner_id == user.get("id")).first()
        if todomodel is not None:
         obj_sch = TodoSchema(**todomodel.__dict__)
         print(obj_sch)
         return TodosResponse[TodoSchema](content = obj_sch)
        raise HTTPException(status_code=401,detail="Todo Not found")

    async def createTodo(self,token,db,todo_request)->TodosResponse[str]:
        user = await self.userRepo.get_current_user(token)
        if user is None:
            raise HTTPException(status_code=401, detail="Authentication Failed")
        todo_model = Todos(**todo_request.model_dump(), owner_id=user.get("id"))
        db.add(todo_model)
        db.commit()
        return TodosResponse[str](content="Todo is successfully addedd")

    async def update_todo_by_id(self,token, db,todo_request,todo_id) -> TodosResponse[str]:
        user = await self.userRepo.get_current_user(token)
        if user is None:
            raise HTTPException(status_code=401, detail="Authentication Failed")
        todo_model = db.query(Todos).filter(Todos.id==todo_id) \
                .filter(Todos.owner_id == user.get('id')).first()
        if todo_model is None:
            raise HTTPException(status_code=404, detail="Todo not found.")
        todo_model.title=todo_request.title
        todo_model.description=todo_request.description
        todo_model.priority=todo_request.priority
        todo_model.complete=todo_request.complete
        db.add(todo_model)
        db.commit()
        return TodosResponse[str](content = "Todo successfully updated")

    async def delete_todo_by_id(self,token,db,todo_id)->TodosResponse[str]:
        user = await self.userRepo.get_current_user(token)
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')
        todo_model = db.query(Todos).filter(Todos.id == todo_id). \
            filter(Todos.owner_id == user.get('id')).first()
        if todo_model is None:
            raise HTTPException(status_code=404, detail='Todo not foound.')
        db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).delete()
        db.commit()
        return TodosResponse[str](content="Todo successfully deleted")








