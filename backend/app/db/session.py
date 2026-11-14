
from ..core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator
eng =  create_async_engine(settings.database_url, echo=True)
async_session = async_sessionmaker(eng, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session 
        except Exception:
            await session.rollback()  
            raise