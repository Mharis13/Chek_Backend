from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
)

engine: AsyncEngine = create_async_engine("sqlite+aiosqlite:///:memory", 
                                          connect_args={"timeout": 30}
                                          )
session_factory = async_sessionmaker(engine, expire_on_commit=False)


def get_db_engine(url: str | None) -> AsyncEngine:
    if url is None:
        return engine

    return create_async_engine(url)
