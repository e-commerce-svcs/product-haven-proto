import surrealdb
from litestar import datastructures

from app.config import settings


async def create_db_client(state: datastructures.State) -> None:
    """Create an instance of the SurrealDB client and store it in the app state.

    Returns:
        None
    """
    state.db = surrealdb.Surreal(url=settings.app_settings.db_url)


async def close_db_client(state: datastructures.State) -> None:
    """Close the the app state's SurrealDB client.

    Returns:
        None
    """
    db: surrealdb.Surreal = state.db

    await db.close()
