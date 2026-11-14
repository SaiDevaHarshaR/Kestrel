from sqlalchemy.ext.asyncio import create_async_engine
async def test() -> None:
    eng =  create_async_engine("sqlite+aiosqlite://", echo=True)