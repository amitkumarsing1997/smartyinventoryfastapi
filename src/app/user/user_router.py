
from fastapi import APIRouter, Depends,status
from pydantic import BaseModel
from typing_extensions import Annotated
from src.app.user.user_iservice import IUserService
from src.app.user.user_service import UserService
# from src.app.user.user_schema import CreateUserRequest
from starlette import status
from src.app.config.db_config import SessionLocal
from sqlalchemy.orm import Session
from src.app.models.model import Users
from src.app.user.user_schema import CreateUserRequest
from src.app.shared.response import CreateUserResponse

userRouter = APIRouter(prefix="/user",tags=["User"])


UserServiceIns = Annotated[IUserService,Depends(UserService)]


@userRouter.post("/",status_code=status.HTTP_201_CREATED,response_model=CreateUserResponse)
async def create_user(
    create_user_request: CreateUserRequest,
    service:UserServiceIns
):
    # print(type(service))
    await service.reg_user(create_user_request)
    print("hello amit")
    return CreateUserResponse()
  




# # @userRouter.post("/add-user",response_model=Response[str],name="user created")
# @userRouter.post("/add-user",status_code=status.HTTP_201_CREATED)
# async def create_user(service:UserServiceIns,create_user_request:CreateUserRequest):
#     # return Response[str](body=await service.reg_user)
#     await service.reg_user(create_user_request)

# import sys
# sys.path.append("..")

# from starlette import status
# from starlette.responses import RedirectResponse

# from fastapi import Depends, APIRouter, Request, Form
# import models
# from database import engine, SessionLocal
# from sqlalchemy.orm import Session
# from .auth import get_current_user

# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates


# router = APIRouter(
#     prefix="/todos",
#     tags=["todos"],
#     responses={404: {"description": "Not found"}}
# )

# models.Base.metadata.create_all(bind=engine)

# templates = Jinja2Templates(directory="templates")


# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()

#  @router.post("/add-todo", response_class=HTMLResponse)
# async def create_todo(request: Request, title: str = Form(...), description: str = Form(...),
#                       priority: int = Form(...), db: Session = Depends(get_db)):
#     user = await get_current_user(request)
#     if user is None:
#         return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

#     todo_model = models.Todos()
#     todo_model.title = title
#     todo_model.description = description
#     todo_model.priority = priority
#     todo_model.complete = False
#     todo_model.owner_id = user.get("id")

#     db.add(todo_model)
#     db.commit()

#     return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)



# @router.get("/", response_class=HTMLResponse)
# async def read_all_by_user(request: Request, db: Session = Depends(get_db)):

#     user = await get_current_user(request)
#     if user is None:
#         return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

#     todos = db.query(models.Todos).filter(models.Todos.owner_id == user.get("id")).all()

#     return templates.TemplateResponse("home.html", {"request": request, "todos": todos, "user": user})


# @router.get("/add-todo", response_class=HTMLResponse)
# async def add_new_todo(request: Request):
#     user = await get_current_user(request)
#     if user is None:
#         return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

#     return templates.TemplateResponse("add-todo.html", {"request": request, "user": user})





# @router.get("/edit-todo/{todo_id}", response_class=HTMLResponse)
# async def edit_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):

#     user = await get_current_user(request)
#     if user is None:
#         return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

#     todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

#     return templates.TemplateResponse("edit-todo.html", {"request": request, "todo": todo, "user": user})


# @router.post("/edit-todo/{todo_id}", response_class=HTMLResponse)
# async def edit_todo_commit(request: Request, todo_id: int, title: str = Form(...),
#                            description: str = Form(...), priority: int = Form(...),
#                            db: Session = Depends(get_db)):

#     user = await get_current_user(request)
#     if user is None:
#         return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

#     todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

#     todo_model.title = title
#     todo_model.description = description
#     todo_model.priority = priority

#     db.add(todo_model)
#     db.commit()

#     return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


# @router.get("/delete/{todo_id}")
# async def delete_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):

#     user = await get_current_user(request)
#     if user is None:
#         return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

#     todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id)\
#         .filter(models.Todos.owner_id == user.get("id")).first()

#     if todo_model is None:
#         return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)

#     db.query(models.Todos).filter(models.Todos.id == todo_id).delete()

#     db.commit()

#     return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)





# @router.get("/complete/{todo_id}", response_class=HTMLResponse)
# async def complete_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):

#     user = await get_current_user(request)
#     if user is None:
#         return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

#     todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

#     todo.complete = not todo.complete

#     db.add(todo)
#     db.commit()

#     return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)