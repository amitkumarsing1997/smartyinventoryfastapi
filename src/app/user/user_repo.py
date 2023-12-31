from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.config.db_config import Database
from src.app.user.user_schema import CreateUserRequest
from src.app.models.model import Users
from typing import Annotated
from src.app.config.db_config import SessionLocal

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# db_dependency=Annotated[Session,Depends(get_db)]


# class UserRepo:
#     def __init__(self,db:Session=Depends(get_db))->None:
#         self.db=db     
#     async def create_user(self, create_user_request:CreateUserRequest):
#         create_user_model = Users(
#             email=create_user_request.email,
#             username=create_user_request.username,
#             first_name=create_user_request.first_name,
#             last_name=create_user_request.last_name,
#             role=create_user_request.role,
#             hashed_password=create_user_request.password,
#             # hashed_password=bcrypt_context.hash(create_user_request.password),
#             is_active=True
#         )
       
#         print("??????")
#         print (type(create_user_model))
#         # print(type(self.db)
#         print("&&&&&")
#         # self.db.add(create_user_model)
#         # self.db.commit()
#         # return create_user_model

# db=Database()


class UserRepo:
    def __init__(self, db:Database=Depends()) -> None:
        self.db = db

# class UserRepo:
#     def __init__(self, db: Database = Depends()) -> None:
#         self.db = db

    async def create_user(self, create_user_request: CreateUserRequest):
        create_user_model = Users(
            email=create_user_request.email,
            username=create_user_request.username,
            first_name=create_user_request.first_name,
            last_name=create_user_request.last_name,
            role=create_user_request.role,
            hashed_password=create_user_request.password,
            is_active=True
        )
        
        print("$$$self db class")
        print(type(self.db))
        # print(self.db.add(create_user_model))
        print(type(self.db.get_db().add(create_user_model)))
        # self.db.get_db().add(create_user_model).commit()
       
        # Use the Database class as a context manager
        # with self.database.get_db() as db:
        #     try:
        #         db.add(create_user_model)
        #         db.commit()
        #         db.refresh(create_user_model)
        #         print("User created successfully")
        #     except Exception as e:
        #         db.rollback()
        #         raise e


# 

# from fastapi import Depends
# from src.app.config.db_config import SessionLocal
# from sqlalchemy.orm import Session
# from typing import Annotated
# from src.app.user.user_schema import CreateUserRequest
# from src.app.models.model import Users
# from src.app.config.db_config import Database






# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# db_dependency=Annotated[Session,Depends(get_db)]

# db_dependency=Annotated[Session,Depends(get_db)]


# class UserRepo:
#     def __init__(self,db:Session=db_dependency)->None:
#         self.db=db

# dbobj = Database()
# # dbobj.

# # db_dependency=Annotated[Session,Depends(get_db)]
# # class UserRepo:
# #     def __init__(self,db:Session=dbobj.get_db) -> None:
# #         self.db=db

# class UserRepo:
#     def __init__(self,dbobj) -> None:
#         self.dbobj=dbobj
        
#     async def create_user(self, create_user_request:CreateUserRequest):
#         create_user_model = Users(
#             email=create_user_request.email,
#             username=create_user_request.username,
#             first_name=create_user_request.first_name,
#             last_name=create_user_request.last_name,
#             role=create_user_request.role,
#             hashed_password=create_user_request.password,
#             # hashed_password=bcrypt_context.hash(create_user_request.password),
#             is_active=True
#         )
#         # self.db
#         # print(type(self.db))
#         # self.db.add(create_user_model)
#         # await self.db.commit()
#         # print("Successfully created")
#         print (type(create_user_model))
#         print("databae object")
#         print(type(dbobj))
#         # return create_user_model
    

# @router.post("/",status_code=status.HTTP_201_CREATED)
# async def create_user(db:db_dependency,
#                       create_user_request: CreateUserRequest):
#     create_user_model=Users(
#         email=create_user_request.email,
#         username=create_user_request.username,
#         first_name=create_user_request.first_name,
#         last_name=create_user_request.last_name,
#         role=create_user_request.role,
#         # hashed_password=create_user_request.password,
#         hashed_password=bcrypt_context.hash(create_user_request.password),
#         is_active=True
#     )
#     db.add(create_user_model)
#     db.commit()

"""
from typing import List

from fastapi import APIRouter, Depends
from typing_extensions import Annotated
from src.app.communication.communication_iservice import ICommunicationService
from src.app.communication.communication_schema import ReadingSchema, RepeatingSentencesSchema, JumbledSentenceSchema, \
    OpenQuestionsSchema, StoryReTellingSchema, QuestionAnswerSchema
from src.app.communication.communication_service import CommunicationService
from src.app.shared.response import Response

communicationRouter = APIRouter(prefix="/communication", tags=["Communication"])

CommunicationServiceIns = Annotated[ICommunicationService, Depends(CommunicationService)]


@communicationRouter.get("/reading", response_model=Response[list[ReadingSchema]], name="reading question from mongodb")
async def get_reading(service: CommunicationServiceIns) -> Response[list[ReadingSchema]] | None:
    return Response[list[ReadingSchema]](body=await service.reading())


@communicationRouter.get("/repeating/sentences", response_model=Response[list[RepeatingSentencesSchema]],
                         name="repeating question from mongodb")
async def get_repeating_sentences(service: CommunicationServiceIns) -> Response[list[RepeatingSentencesSchema]] | None:
    return Response[list[RepeatingSentencesSchema]](body=await service.repeating_sentences())


@communicationRouter.get("/jumbled/sentence", response_model=Response[list[JumbledSentenceSchema]],
                         name="jumbled question from mongodb")
async def get_jumbled_sentences(service: CommunicationServiceIns) -> Response[list[JumbledSentenceSchema]] | None:
    return Response[list[JumbledSentenceSchema]](body=await service.jumbled_sentences())


@communicationRouter.get("/open/questions", response_model=Response[list[OpenQuestionsSchema]],
                         name="open sentence from mongodb")
async def get_open_questions(service: CommunicationServiceIns) -> Response[list[OpenQuestionsSchema]] | None:
    return Response[list[OpenQuestionsSchema]](body=await service.open_questions())


@communicationRouter.get("/story/re/telling", response_model=Response[list[StoryReTellingSchema]],
                         name="story re telling from mongodb")
async def get_reading(service: CommunicationServiceIns) -> Response[list[StoryReTellingSchema]] | None:
    return Response[list[StoryReTellingSchema]](body=await service.story_re_telling())


@communicationRouter.get("/question/and/answer", response_model=Response[list[QuestionAnswerSchema]],
                         name="question and answer from mongodb")
async def get_question_and_answer(service: CommunicationServiceIns) -> Response[list[QuestionAnswerSchema]] | None:
    return Response[list[QuestionAnswerSchema]](body=await service.question_and_answer())


    """