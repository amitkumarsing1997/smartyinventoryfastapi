

# from typing import Annotated
# from pydantic import BaseModel, Field
# from sqlalchemy.orm import Session
# from fastapi import FastAPI,Depends, HTTPException,Path
from fastapi import FastAPI
# import models
from src2.app.models import models
# from models import Todos
# from database import engine,SessionLocal
# from database import engine
from src2.app.config.db_config import engine
# from routers import auth
# from routers import auth,todos,admin,users
from src2.app.user import user_router

# import starlette.status

app=FastAPI()

# models.Base.metadata.create_all(bind=engine)

app.include_router(user_router.userrouter)
# app.include_router(todos.router)
# app.include_router(admin.router)
# app.include_router(users.router)




# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# db_dependency=Annotated[Session,Depends(get_db)]

# ## for video 94
# class TodoRequest(BaseModel):
#     title:str=Field(min_length=3)
#     description:str=Field(min_length=3,max_length=100)
#     priority:int=Field(gt=0,lt=6)
#     complete:bool


# #video 94 post request 

# @app.post("/todo",status_code=starlette.status.HTTP_201_CREATED)
# async def create_todo(db:db_dependency,todo_request:TodoRequest):
#     todo_model=Todos(**todo_request.model_dump())
#     db.add(todo_model)
#     db.commit()

# # video 92   get all todos from database
# @app.get("/",status_code=starlette.status.HTTP_200_OK)
# async def read_all(db: db_dependency):
#     return db.query(Todos).all()

# # video 93 get todo by id

# @app.get("/todo/{todo_id}",status_code=starlette.status.HTTP_200_OK)
# async def read_todo(db: db_dependency,todo_id:int=Path(gt=0)):
#     todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
#     if todo_model is not None:
#         return todo_model
#     raise HTTPException(status_code=404,detail='Todo not found.')

# #video 95 put request 
# @app.put("/todo/{todo_id}",status_code=starlette.status.HTTP_204_NO_CONTENT)
# async def update_todo(db:db_dependency,
#                       todo_request:TodoRequest,
#                       todo_id:int=Path(gt=0)):
#     todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404,detail='Todo not found.')
    
#     todo_model.title=todo_request.title
#     todo_model.description=todo_request.description
#     todo_model.priority=todo_request.priority
#     todo_model.complete=todo_request.complete
    
#     db.add(todo_model)
#     db.commit()

# #video 96 delete request
# @app.delete("/todo/{todo_id}",status_code=starlette.status.HTTP_204_NO_CONTENT)
# async def delete_todo(db:db_dependency,todo_id:int=Path(gt=0)):
#     todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404,detail='Todo not foound.')
#     db.query(Todos).filter(Todos.id==todo_id).delete()
#     db.commit()
    



