import functools
import typing

from app.config import app, base, dev, prod

environments: dict[base.AppEnv, typing.Type[app.AppSettings]] = {
    base.AppEnv.DEV: dev.DevAppSettings,
    base.AppEnv.PROD: prod.ProdAppSettings,
}


@functools.lru_cache
def get_app_settings() -> app.AppSettings:
    app_env = base.BaseAppSettings().app_env
    config = environments[app_env]

    return config()


app_settings = get_app_settings()
