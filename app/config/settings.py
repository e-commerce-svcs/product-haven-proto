from functools import lru_cache
from typing import Type

from app.config.app import AppSettings
from app.config.base import AppEnv, BaseAppSettings
from app.config.dev import DevAppSettings
from app.config.prod import ProdAppSettings

environments: dict[AppEnv, Type[AppSettings]] = {
    AppEnv.DEV: DevAppSettings,
    AppEnv.PROD: ProdAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()


settings = get_app_settings()
