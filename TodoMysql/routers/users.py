# from typing import Annotated
# from pydantic import BaseModel, Field
# from sqlalchemy.orm import Session
# # from fastapi import FastAPI,Depends, HTTPException,Path
# from fastapi import APIRouter,Depends, HTTPException,Path
# import models
# from models import Todos,Users
# # from database import engine,SessionLocal
# from database import SessionLocal
# # from routers import auth
# import starlette.status as status
# from .auth import get_current_user
# #because we dealing with password we need to verify the password
# from passlib.context import CryptContext

# # app=FastAPI()
# router=APIRouter(
#     prefix='/user',
#     tags=['user']
# )

# # models.Base.metadata.create_all(bind=engine)

# # app.include_router(auth.router)


# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# db_dependency=Annotated[Session,Depends(get_db)]

# user_dependency=Annotated[dict,Depends(get_current_user)]

# bcrypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

# #Pydentic class for verification
# class UserVerification(BaseModel):
#     password:str
#     new_password:str=Field(min_length=6)



# @router.get('/',status_code=status.HTTP_200_OK)
# async def get_user(user:user_dependency,db:db_dependency):
#     if user is None:
#         raise HTTPException(status_code=401,detail="Authentication Failed")
#     return db.query(Users).filter(Users.id==user.get('id')).first()


# @router.put("/password",status_code=status.HTTP_204_NO_CONTENT)
# async def change_password(user:user_dependency,
#                           db:db_dependency,
#                           user_verification:UserVerification):
#     if user is None:
#         raise HTTPException(status_code=401,detail="Authentication Failed")
#     user_model=db.query(Users).filter(Users.id==user.get('id')).first()

#     if not bcrypt_context.verify(user_verification.password,user_model.hashed_password):
#         raise HTTPException(status_code=401,detail="Error on password change")
#     user_model.hashed_password=bcrypt_context.hash(user_verification.new_password)
#     db.add(user_model)
#     db.commit()

