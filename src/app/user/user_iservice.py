from abc import ABC,abstractmethod
# from src.app.user.user_schema import CreateUserRequest
from src.app.user.user_schema import CreateUserRequest
from src.app.user.user_repo import UserRepo
# from src2.app.models.models import Users

class IUserService(ABC):

    @abstractmethod
    async def reg_user(self,create_user_request:CreateUserRequest):
        pass









# from abc import ABC, abstractmethod

# from src.app.communication.communication_schema import ReadingSchema, RepeatingSentencesSchema, JumbledSentenceSchema, \
#     OpenQuestionsSchema, StoryReTellingSchema, QuestionAnswerSchema


# class ICommunicationService(ABC):

#     @abstractmethod
#     async def reading(self) -> list[ReadingSchema] | None:
#         pass

#     @abstractmethod
#     async def repeating_sentences(self) -> list[RepeatingSentencesSchema] | None:
#         pass

#     @abstractmethod
#     async def jumbled_sentences(self) -> list[JumbledSentenceSchema] | None:
#         pass

#     @abstractmethod
#     async def open_questions(self) -> list[OpenQuestionsSchema] | None:
#         pass

#     @abstractmethod
#     async def story_re_telling(self) -> list[StoryReTellingSchema] | None:
#         pass

#     @abstractmethod
#     async def question_and_answer(self) -> list[QuestionAnswerSchema] | None:
#         pass
