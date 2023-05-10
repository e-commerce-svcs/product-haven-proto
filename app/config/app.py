import logging

from litestar import openapi

from app.config import base


class AppSettings(base.BaseAppSettings):
    """The application configuration settings.

    The `pydantic.BaseSettings` will look for environment variables that match the
    attribute names of this class. If it finds a match, it will use the value of the
    environment variable as the value of the attribute.

    The `app.py` module initializes attributes to provide default values that can be
    overridden in the child classes. This makes it easier to customize the configuration
    settings for different environments without having to redefine all the attributes.
    """

    debug = False
    title = "Product Haven"
    version = "0.1.0"
    openapi_config = openapi.OpenAPIConfig(title=title, version=version)
    allow_origins = ["*"]
    logging_level = logging.INFO
    db_url: str = "ws://localhost:8000/rpc"

    class Config(base.BaseAppSettings.Config):
        validate_assignment = True
