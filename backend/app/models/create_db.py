from app.database import Base, engine
import asyncio

async def create_db_and_tables():
    async with engine.begin() as conn:
        # Import all models here to ensure they are registered before creating tables
        from app.models.store import Store
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()

asyncio.run(create_db_and_tables())