from src2.app.admin.admin_iservice import IAdminService
from src2.app.user.user_iservice import IUserService
from src2.app.user.user_repo import UserRepo
from fastapi import Depends,HTTPException
from src2.app.user.user_schema import CreateUserRequest
from src2.app.config.db_config import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from src2.app.user.user_repo import UserRepo
from src2.app.models.models import Users, Todos
from sqlalchemy.orm import Session
# from src2.app.admin.admin_repo import AdminRepo
from src2.app.auth.auth_repo import AuthRepo
from src2.app.user.user_repo import UserRepo
from src2.app.admin.admin_schema import AdminTodoRespSchema,AdminResponse
# open_ai: OpenAI = Depends()


class AdminService(IAdminService):
    def __init__(self, userRepo: UserRepo = Depends()) -> None:
        super().__init__()
        self.userRepo = userRepo



    async def get_list_all_todos(self, token, db) ->AdminResponse[list[AdminTodoRespSchema]]:
        user = await self.userRepo.get_current_user(token)
        if user is None or user.get('user_role') != 'admin':
            raise HTTPException(status_code=401, detail='Authentication Failed')
        db_query_obj = db.query(Todos).all()
        print("in admin service -----------")
        print(db_query_obj)
        list_obj = [AdminTodoRespSchema(id=db_obj.id,title=db_obj.title,description=db_obj.description,
                                   priority=db_obj.priority,complete=db_obj.complete,owner_id=db_obj.owner_id)
               for db_obj in db_query_obj]
        # list_obj = [AdminTodoRespSchema(** db_obj.model_dump()) for db_obj in db_query_obj]
        print(list_obj)
        return AdminResponse[list[AdminTodoRespSchema]](content = list_obj)

    async def deleteselectedid(self,token, db, todo_id) -> AdminResponse[str]:
        user = await self.userRepo.get_current_user(token)
        if user is None or user.get('user_role') != 'admin':
            raise HTTPException(status_code=401, detail='Authentication Failed')
        todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
        if todo_model is None:
            raise HTTPException(status_code=404 , detail='Todo not Found at given id ')
        db.query(Todos).filter(Todos.id==todo_id).delete()
        db.commit()
        return AdminResponse[str](content= "data successfully deleted")



        # class AuthResponse(BaseModel, Generic[T]):
        #     resp: str = "in admin schema"
        #     content: T | None = None
        # return ([AdminTodoRespSchema(id=db_obj.id,title=db_obj.title,description=db_obj.description,
        #                            priority=db_obj.priority,complete=db_obj.complete,owner_id=db_obj.owner_id)
        #        for db_obj in db_query_obj])

        # print([AdminTodoRespSchema(** db_obj)for db_obj in db_query_obj])
        # return [RepeatingSentencesSchema(sentence=sentence.get("content")) async for sentence in sentences]
        # for obj in db_query_obj:
        #     print(obj.id)
        # print(type(db_query_obj))
        # admin_res_sch = AdminTodoRespSchema(
        #
        # )
        #

        # @adminRouter.get("/todo", status_code=status.HTTP_200_OK)
        # async def read_all(token: token_str, service: AdminServiceIns, db: db_dependency):
        #     admin_resp_sch = await service.get_list_all_todos(token, db)
        #     user = await service.get_current_user(token)
        #     if user is None or user.get('user_role') != 'admin':
        #         raise HTTPException(status_code=401, detail='Authentication Failed')
        #     return db.query(Todos).all()




