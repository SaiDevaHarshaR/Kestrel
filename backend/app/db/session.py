
from core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

eng =  create_async_engine(settings.database_url, echo=True)
async_session = async_sessionmaker(eng, expire_on_commit=False)


async def main() -> Depends():
    async with () as session:
        try:
            yield session
            await session.commit()  
        except Exception:
            await session.rollback()  
            raise