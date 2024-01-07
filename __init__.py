import logging

# from src.app.config.setting import get_setting
from src2.app.config.setting import get_setting

setting = get_setting()


# logging.config.fileConfig('src/resource/logging.conf', disable_existing_loggers=False)
logging.config.fileConfig('src2/app/resource/logging.conf', disable_existing_loggers=False)
logging.getLogger().setLevel(setting.LOG_LEVEL)

