import logging

from app.config import app


class DevAppSettings(app.AppSettings):
    debug = True
    title = "Product Haven Dev"
    logging_level = logging.DEBUG

    class Config(app.AppSettings.Config):
        env_file = ".env"
        env_file_encoding = "utf-8"
