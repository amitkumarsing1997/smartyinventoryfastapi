from src2.app.exception.custom_exception import GenericException
from src2.app.muser.user_iservice import IUserServiceMongo
from src2.app.muser.user_schema import UserMongoSchema,ActualUserMongoSchema
from src2.app.muser.user_repo import UserRepoMongo
from src2.app.minvitation.invitation_iservice import IInvitationService
from src2.app.minvitation.invitation_service import InvitationService
from src2.app.minvitation.invitation_repo import InvitationRepoMongo
from fastapi.encoders import jsonable_encoder
from fastapi import Depends
from typing import Annotated
from src2.app.muser.util.emailjinjaofficial import send_with_template
from src2.app.config.authkey import bcrypt_context
class UserServiceMongo(IUserServiceMongo):

    def __init__(self, iinvitation:Annotated[IInvitationService,Depends(InvitationService)]):
        super().__init__()
        self.iinvitation = iinvitation
        # self.irepo = irepo
    # def __init__(self,iinvitation:IInvitationService= Depends(InvitationService)):
    #     super().__init__()
    #     self.iinvitation = iinvitation
    # def __init__(self,iinvitation:InvitationService = Depends()):
    #     super().__init__()
    #     self.iinvitation = iinvitation
    # def __init__(self, userRepo: UserRepo = Depends()) -> None:
    #     super().__init__()
    #     self.userRepo = userRepo

    # def student_helper(student) -> dict:
    #     return {
    #         "id": str(student["_id"]),
    #         "fullname": student["fullname"],
    #         "email": student["email"],
    #         "course_of_study": student["course_of_study"],
    #         "year": student["year"],
    #         "GPA": student["gpa"],
    #     }

    # async def user_helper(userschema) -> dict:
    #     return {
    #         "firstName": userschema.firstName,
    #         "lastName": userschema.lastName,
    #         "email": userschema.email,
    #         "hashed_pass": bcrypt_context.hash(userschema.password),
    #         "mobileNumber": userschema.mobileNumber,
    #
    #     }
    async def insert_user_if_not_present_in_collecton(self,userschema:UserMongoSchema):
        # print(type(userschema))
        # actualuserschema = (
        #     ActualUserMongoSchema(firstName=userschema.firstName,
        #                           lastName=userschema.lastName,
        #                           email=userschema.email,
        #                           password=bcrypt_context.hash(userschema.password),
        #                           mobileNumber = userschema.mobileNumber
        #                           ))
        # userschema_jsonable = jsonable_encoder(actualuserschema )
        userschema_jsonable = jsonable_encoder(userschema)
        # print(type(userschema_jsonable))
        emaildata = userschema_jsonable.get("email")
        userobj = await UserRepoMongo.find_user({"email":emaildata})
        if userobj:
            raise GenericException(msg="user email already present", msg_code="500")
        pymongouser = await UserRepoMongo.insert_user_detail(userschema_jsonable)
        user_Objid = pymongouser.inserted_id
        print(user_Objid)
        # return user_Objid
        pymongo_invitation_userobj = await self.iinvitation.invitation_insertion(user_Objid)
        # inserted_id is user for to get id from the pymongo object
        invitation_user_id = pymongo_invitation_userobj.inserted_id
        print(invitation_user_id)
        invitattion_obj = await InvitationRepoMongo.get_invitation_document(invitation_user_id)
        print(invitattion_obj)
        token_det = invitattion_obj.get("token")
        print(token_det)
        token_dict={
            "token":token_det
        }
        await send_with_template(token_dict)


    async def authenticate_user(self,username,password):
        print("in authenticate user service--------")
        userobj = await UserRepoMongo.find_user({"email": username})
        if not userobj:
            raise GenericException(msg="user email incorrect", msg_code="500")
        if not bcrypt_context.verify(password, userobj.get("password")):
            raise GenericException(msg="user password incorrect", msg_code="500")
        return userobj

    async def update_user_password(self,id,password):
        print("in update user service----")
        print(type(id))
        # await UserRepoMongo.hello_testing()
        user = await UserRepoMongo.find_user_by_id(id)
        if user:
            updated_user = await UserRepoMongo.update_user_password(id,bcrypt_context.hash(password))
            return updated_user
        raise GenericException(msg_code="403",msg="user is not in user collection")




