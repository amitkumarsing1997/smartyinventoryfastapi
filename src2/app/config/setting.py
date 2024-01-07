import os
from functools import lru_cache

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='src/resource/env/.env',extra='ignore')
    # PROFILE: str
    # APP_NAME: str = "Winterview GPT API"
    LOG_LEVEL: str
    # API_KEY: str

    # db
    # MONGO_CONN_URI: str
    # MONGO_DB: str
    # MONGO_DB_SKILL_COLL: str
    # MONGO_DB_SKILL_LANG_COLL: str
    # MONGO_DB_MCQ_COLL: str
    # MONGO_DB_MCQ_ERR_COLL: str
    # MONGO_DB_CODING_COLL: str
    # MONGO_DB_CODING_ERR_COLL: str
    # MONGO_DB_READING: str
    # MONGO_DB_REPEATING_SENTENCES: str
    # MONGO_DB_JUMBLED_SENTENCE: str
    # MONGO_DB_OPEN_QUESTIONS: str
    # MONGO_DB_STORY_RE_TELLING: str
    # MONGO_DB_QUESTION_AND_ANSWER: str
    #
    #
    #
    # # open ai
    # OPEN_AI_API_KEY: str
    # TEXT_COMPLETION_MODEL: str
    # CHAT_MODEL: str
    # CHAT_MODEL_V2: str  # v2 is 16k Turbo
    # TRANSCRIBE_MODEL: str
    # CHAT_MODEL_GPT_4: str  # 8k token
    # CHAT_MODEL_GPT_4_32K: str  # 32k token
    # CHAT_MODEL_GPT_4_1106: str  # 128k token
    #
    # # gcp
    # GCP_PROJECT_ID: str
    #
    # # mathpix
    # MATH_PIX_IMG_TEXT: HttpUrl
    # MATH_PIX_APP_ID: str
    # MATH_PIX_API_KEY: str
    #
    # # azure
    # AZURE_SPEECH_KEY: str
    # AZURE_SPEECH_END_POINT: str
    # AZURE_SPEECH_REGION: str
    # AZURE_FACE_API_KEY: str
    # AZURE_FACE_API_END_POINT: str
    #
    # # loc
    # TEMP_AUDIO_LOC: str


# make an entry here if you are creating new env
# config = dict(
#     dev='src/resource/env/dev.env',
#     test='src/resource/env/test.env',
#     uat='src/resource/env/uat.env',
#     prod='src/resource/env/prod.env'
# )


# settings: Union[Dev, Test] = config[os.environ.get('ENV', 'dev').lower()]()



# @lru_cache
# def get_setting() -> Settings:
#     return Settings(_env_file=("src/resource/env/.env", config[os.environ.get('ENV', 'dev').lower()]))



# @lru_cache
# def get_setting() -> Settings:
#     return Settings(_env_file="src/resource/env/.env",_env_file_encoding='utf-8')


@lru_cache
def get_setting() -> Settings:
    return Settings()
