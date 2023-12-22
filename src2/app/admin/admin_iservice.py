from abc import ABC, abstractmethod

from src2.app.admin.admin_schema import AdminResponse, AdminTodoRespSchema
# from src.app.user.user_schema import CreateUserRequest
from src2.app.user.user_schema import CreateUserRequest
from src2.app.user.user_repo import UserRepo
from src2.app.models.models import Users
from sqlalchemy.orm import Session


class IAdminService(ABC):

    # @abstractmethod
    # async def auth_user(self, username: str, password: str, db: Session) -> Users:
    #     pass
    #
    # @abstractmethod
    # async def get_current_user(self, token: str) -> dict:
    #     pass

    @abstractmethod
    async def get_list_all_todos(self, token, db)->AdminResponse[list[AdminTodoRespSchema]]:
        pass

    @abstractmethod
    async def deleteselectedid(token,db,todo_id)->AdminResponse[str]:
        pass
