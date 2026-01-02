from app.database import Base, engine
import asyncio

async def create_db_and_tables():
    async with engine.begin() as conn:
        # Import all models here to ensure they are registered before creating tables
        from app.models.user import User
        from app.models.transaction import Transaction
        from app.models.products import Product
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()

asyncio.run(create_db_and_tables())