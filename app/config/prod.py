from app.config import app


class ProdAppSettings(app.AppSettings):
    ...

    class Config(app.AppSettings.Config):
        ...
