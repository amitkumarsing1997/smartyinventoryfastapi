from src2.app.exception.custom_exception import GenericException
from src2.app.minvitation.invitation_iservice import IInvitationService
from src2.app.minvitation.invitation_repo import InvitationRepoMongo
from _datetime import datetime,timedelta
import uuid
from fastapi import HTTPException


class InvitationService(IInvitationService):
    def __init__(self):
        super().__init__()

    async def hello_amit(self):
        print("hello amit")

    async def invitation_insertion(self,userObjId):
        invitation_data = {
            "userId":userObjId,
            "token":str(uuid.uuid4()),
            "status":"ACTIVE",
            "expire_on":datetime.now() + timedelta(minutes=60)
        }
        pymongo_insertion_obj = await InvitationRepoMongo.insert_invitation_detail(invitation_data)
        return pymongo_insertion_obj

    async def is_token_valid(self,token_detail):
        invitation_doc = await InvitationRepoMongo.find_token_details(token_detail)
        if invitation_doc and invitation_doc.get("status")=="ACTIVE" \
            and invitation_doc.get("expire_on") > datetime.now():
            # print(type(invitation_doc))
            # if invitation_doc.get("status")=="ACTIVE"
            return invitation_doc
        # raise GenericException(msg="invitaton token is not found>>>>", msg_code="500"
        # raise HTTPException(msg="invitaton token is not found>>>>", msg_code="200")
        raise HTTPException(status_code=404, detail="Invitation was not found.")









