from surrealdb import Surreal


async def create_db_client() -> Surreal:
    """Creates a new instance of the SurrealDB client.

    Returns:
        Surreal: Representation of a SurrealDB client/server.
    """
    return Surreal("ws://localhost:8000/rpc")
