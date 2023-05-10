import litestar

from app.config import settings
from app.events import db
from app.utils import cache, cors


def create_app() -> litestar.Litestar:
    app = litestar.Litestar(
        debug=settings.app_settings.debug,
        on_shutdown=[
            db.close_db_client,
        ],
        on_startup=[
            db.create_db_client,
        ],
        cache_control=cache.create_cache_control_header(),
        cors_config=cors.create_cors_config(
            allow_origins=settings.app_settings.allow_origins
        ),
        openapi_config=settings.app_settings.openapi_config,
    )

    return app
