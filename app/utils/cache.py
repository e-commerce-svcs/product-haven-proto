from litestar import datastructures


def create_cache_control_header() -> datastructures.CacheControlHeader:
    return datastructures.CacheControlHeader(
        max_age=300,
        must_revalidate=True,
        stale_while_revalidate=60,
    )
