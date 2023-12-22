import logging
from src2.app.todos.todos_iservice import ITodosService
from src2.app.user.user_repo import UserRepo
from typing import Annotated
from fastapi import Depends,HTTPException

log = logging.getLogger()
class TodosService(ITodosService):
    def __init__(self,userRepo:Annotated[UserRepo,Depends()]):
        self.userRepo = userRepo
        print("in todoserviceconstructor")

    # def __init__(self, userRepo:UserRepo = Depends()):
    #     self.userRepo = userRepo
    #     print("in todoserviceconstructor")
    async def read_all_todos(self,db):
        print("in todo service")
        print("user is authanticated")
        # user = await self.userRepo.get_current_user(token)
        # print("after user is called---")
        # if user is None:
        #     raise HTTPException(status_code=401,detail="Authentication Failed")
        # # log.debug(f" User : : {user}")
        # log.debug(f" RES OF result : : {user}")
        # log.debug(f" RES OF result : : {user}")
        # log.info(f" RES OF result : : {user}")
        # print(log)
        # print(user)


