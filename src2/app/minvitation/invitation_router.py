from fastapi import APIRouter,Depends
from typing import Annotated
from src2.app.minvitation.invitation_iservice import IInvitationService
from src2.app.minvitation.invitation_service import InvitationService
from starlette.responses import JSONResponse

from src2.app.muser.user_iservice import IUserServiceMongo
from src2.app.muser.user_service import UserServiceMongo

invitationMongoRepo = APIRouter(prefix="/invitation" ,tags=["INVITATION"])

InvitationServiceMongoIns = Annotated[IInvitationService,Depends(InvitationService)]
UserServiceMongoIns = Annotated[IUserServiceMongo, Depends(UserServiceMongo)]

@invitationMongoRepo.get("/checkvalidinvitation")
async def find_valid_invitaton_doc(token_detail:str,service:InvitationServiceMongoIns)->JSONResponse:
    invit_obj = await service.is_token_valid(token_detail)
    # print("inInvitation_router------>>>--->>>")
    # print(invit_obj)
    return JSONResponse(status_code=200,content={"message":"token is valid..."})

@invitationMongoRepo.put("/adduserpass")
async def update_user_withpassword(token_detail:str,service:InvitationServiceMongoIns,serviceuser:UserServiceMongoIns,password:str)->JSONResponse:
    invitation_obj = await service.is_token_valid(token_detail)
    print("we get userId")
    user_Id = invitation_obj.get("userId")
    print("in put ::::::")
    print(user_Id)
    await serviceuser.update_user_password(user_Id,password)
    return JSONResponse(status_code=200, content={"message": "password  is successfully changed for the valid token..."})


