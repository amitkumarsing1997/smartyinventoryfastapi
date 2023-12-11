from src.app.user.user_iservice import IUserService
from src.app.user.user_schema import CreateUserRequest
from src.app.user.user_repo import UserRepo
from fastapi import Depends
from typing import Annotated



# open_ai: OpenAI = Depends() 

userrepo : UserRepo = Depends()

# userrepo =Annotated[UserRepo,Depends()]

class UserService(IUserService):
    def __init__(self) -> None:
        super().__init__()

    
    async def reg_user(self,create_user_request:CreateUserRequest):
         await userrepo.create_user(create_user_request)

    # 
    
"""
from src.app.communication.communication_iservice import ICommunicationService
from src.app.communication.communication_schema import ReadingSchema, RepeatingSentencesSchema, JumbledSentenceSchema, \
    OpenQuestionsSchema, StoryReTellingSchema, QuestionAnswerSchema

from src.app.repo.communication_mongo_repo import CommunicationMongoRepo


comm_mongo_repo = CommunicationMongoRepo()


class CommunicationService(ICommunicationService):
    def __init__(self) -> None:
        super().__init__()

    async def reading(self) -> list[ReadingSchema] | None:
        return await comm_mongo_repo.get_all_content()

    async def repeating_sentences(self) -> list[RepeatingSentencesSchema] | None:
        return await comm_mongo_repo.get_all_content_repeating_sentences()

    async def jumbled_sentences(self) -> list[JumbledSentenceSchema] | None:
        return await comm_mongo_repo.get_all_content_jumbled_sentences()

    async def open_questions(self) -> list[OpenQuestionsSchema] | None:
        return await comm_mongo_repo.get_all_open_questions()

    async def story_re_telling(self) -> list[StoryReTellingSchema] | None:
        return await comm_mongo_repo.get_all_story_re_telling()

    async def question_and_answer(self) -> list[QuestionAnswerSchema] | None:
        return await comm_mongo_repo.get_all_question_answer()


"""