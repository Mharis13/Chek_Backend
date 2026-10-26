from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.sql.engine import session_factory

app = FastAPI(
    title="Chek",
    version="0.1.0",
)


async def get_db() -> AsyncSession:
    return session_factory()


async def check_db(db_session: AsyncSession) -> bool:
    try:
        await db_session.execute(text("SELECT 1"))
        return True
    except:  # noqa: E722
        return False


@app.get("/health", tags=["health"])
async def health_check(
    db_session: Annotated[AsyncSession, Depends(get_db)],
) -> dict[str, str]:

    db_status = "ok" if await check_db(db_session=db_session) else "ko"

    return {"api": "ok", "database": db_status}
