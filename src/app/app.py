
from fastapi import FastAPI,Depends
from src.app.user import user_router
from src.app.models import model
from src.app.config.db_config import engine

app=FastAPI()

# model.Base.metadata.create_all(bind=engine)

app.include_router(user_router.userRouter)

# 

# import logging
# from os import makedirs

# from fastapi import FastAPI, Security, HTTPException, Depends
# from fastapi.security import APIKeyHeader
# from starlette import status
# from starlette.middleware.cors import CORSMiddleware

# from src.app.coding_qna.coding_qna_router import codingQnaRouter
# from src.app.config.lib_config import LibConfig
# from src.app.config.setting import get_setting
# from src.app.exception.handler import exception_handlers
# from src.app.grammar.grammar_router import grammarRouter
# from src.app.mcq_generator.mcq_gen_router import mcqGenRouter
# from src.app.resume.resume_router import resumeRouter
# from src.app.skill.skill_router import skillRouter
# from src.app.speech.speech_router import speechRouter
# from src.app.winbot.winbot_router import winbotRouter
# from src.app.communication.communication_router import communicationRouter

# log = logging.getLogger()
# setting = get_setting()

# api_key_auth = APIKeyHeader(name='access_token', auto_error=False)


# def is_authorized(api_key: str = Security(api_key_auth)):
#     if api_key != setting.API_KEY:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='forbidden')


# app = FastAPI()

# exception_handlers(app)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(skillRouter, dependencies=[Depends(is_authorized)])
# app.include_router(mcqGenRouter, dependencies=[Depends(is_authorized)])
# app.include_router(codingQnaRouter, dependencies=[Depends(is_authorized)])
# app.include_router(winbotRouter, dependencies=[Depends(is_authorized)])
# app.include_router(speechRouter, dependencies=[Depends(is_authorized)])
# app.include_router(grammarRouter, dependencies=[Depends(is_authorized)])
# app.include_router(resumeRouter, dependencies=[Depends(is_authorized)])
# app.include_router(communicationRouter, dependencies=[Depends(is_authorized)])



# # @app.on_event("startup")
# # def initialize():
# #     log.info(f"ACTIVE PROFILE :: {setting.PROFILE}")
# #     LibConfig.init_open_ai()
# #     makedirs(setting.TEMP_AUDIO_LOC, exist_ok=True)


# # @app.get("/health")
# # def health():
# #     log.debug("Health")
# #     return "UP and RUNNING :)"
