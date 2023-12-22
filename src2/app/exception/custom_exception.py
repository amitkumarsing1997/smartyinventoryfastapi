from typing import Optional,Any

class GenericException(Exception):

    def __init__(self,
                 msg: Optional[str] = None,
                 msg_code: Optional[str] = None,
                 body: Optional[Any] = None,)->None:
        self.msg: Optional[str] = msg
        self.msg_code:str = msg_code
        self.body: Optional[str] = body