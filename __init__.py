import logging

from src.app.config.setting import get_setting

setting = get_setting()


logging.config.fileConfig('src/resource/logging.conf', disable_existing_loggers=False)
logging.getLogger().setLevel(setting.LOG_LEVEL)

