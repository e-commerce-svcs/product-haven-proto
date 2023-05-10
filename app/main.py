from litestar import Litestar

from app.events import db


def create_app() -> Litestar:
    app = Litestar(
        on_shutdown=[
            db.close_db_client,
        ],
        on_startup=[
            db.create_db_client,
        ],
    )

    return app
