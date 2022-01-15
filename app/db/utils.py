from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import async_session


async def get_db_session() -> AsyncSession:
    async with async_session() as session:
        yield session
        await session.commit()
