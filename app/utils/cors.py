from litestar.config import cors


def create_cors_config(allow_origins: list[str]) -> cors.CORSConfig:
    return cors.CORSConfig(
        allow_origins=allow_origins,
    )
