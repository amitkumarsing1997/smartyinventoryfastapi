from abc import ABC,abstractmethod

class IInvitationService(ABC):


    @abstractmethod
    async def invitation_insertion(self,userObjId):
        pass


    @abstractmethod
    async def is_token_valid(self,token_detail):
        pass
    @abstractmethod
    async def hello_amit(self):
        pass


