from abc import ABC, abstractmethod


class ITodosService(ABC):
    async def read_all_todos(self,db):
        pass
