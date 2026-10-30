from typing import Annotated

from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from api.health._dto import HealthOutput
from api.health.router import health_router
from infrastructure.sql.engine import session_factory


async def get_db() -> AsyncSession:
    return session_factory()


async def check_db(db_session: AsyncSession) -> bool:
    try:
        await db_session.execute(text("SELECT 1"))
        return True
    except:  # noqa: E722
        return False


@health_router.get("/health")
async def health(
    db_session: Annotated[AsyncSession, Depends(get_db)],
) -> HealthOutput:
    db_status = "ok" if await check_db(db_session=db_session) else "ko"
    return HealthOutput(api="ok", database=db_status)
