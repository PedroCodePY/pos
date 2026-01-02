#imports
from fastapi import APIRouter
from app.schemas.product import Product
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.models.products import Product
from sqlalchemy import select
from app.database import engine

#API router for product management
router = APIRouter()
session = async_sessionmaker(bind=engine, expire_on_commit=False)

#product management system class
class system():
    async def add_product(self, async_session: async_sessionmaker[AsyncSession], product: Product):
        async with async_session() as session:
            session.add(product)
            await session.commit()
            await session.refresh(product)
            return product
    
    async def get_product(self, async_session: async_sessionmaker[AsyncSession], owner_id: int):
        async with async_session() as session:
            statement = select(Product).where(Product.owner_id == owner_id)
            result = await session.execute(statement)
            return result.scalars()
        
    async def get_products_by_id(self, async_session: async_sessionmaker[AsyncSession], product_id: int):
        async with async_session() as session:
            statement = select(Product).where(Product.id == product_id)
            result = await session.execute(statement)
            return result.scalars().one()
    
    async def update_product(self, async_session: async_sessionmaker[AsyncSession], product_id: int, data: Product):
        async with async_session() as session:
            product = await self.get_products_by_id(session, product_id)
            product.name = data.name
            product.description = data.description
            product.price = data.price
            product.in_stock = data.in_stock
            product.product_image = data.product_image
            product.date_updated = data.date_updated
            await session.commit()

    async def delete_product(self, async_session: async_sessionmaker[AsyncSession], product_id: int):
        async with async_session() as session:
            product = await self.get_products_by_id(session, product_id)
            await session.delete(product)
            await session.commit()

#Get product
@router.get("/all/{owner_id}")
async def get_product():
    pass

#Get product by ID
@router.get("/by-id/{product_id}")
async def get_product_by_id():
    pass

#Add new product
@router.post("/add")
async def add_product():
    pass

#Update existing product
@router.put("/update/{product_id}")
async def update_product():
    pass

#Delete product
@router.delete("/delete/{product_id}")
async def delete_product():
    pass