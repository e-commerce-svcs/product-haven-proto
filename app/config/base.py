import enum

import pydantic


class AppEnv(enum.Enum):
    PROD = "prod"
    DEV = "dev"


class BaseAppSettings(pydantic.BaseSettings):
    """The base application configuration settings.

    Use this to set the application configuration settings for different environments.
    See `app.config.settings` or the `settings.py` module.
    """

    app_env: AppEnv = pydantic.Field(
        default=AppEnv.PROD,
        env="APP_ENV",
    )

    class Config(pydantic.BaseSettings.Config):
        env_file = ".env"
