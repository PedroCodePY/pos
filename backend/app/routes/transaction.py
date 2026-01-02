from fastapi import APIRouter
from app.schemas.transaction import Transaction
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.models.transaction import Transaction
from sqlalchemy import select
from app.database import engine

router = APIRouter()
session = async_sessionmaker(bind=engine, expire_on_commit=False)

class system():
    pass

#create transactions
@router.post("/create-transaction")
async def create_transaction():
    pass

#get all transaction by user ID
@router.get("/get-all-transactions/{user_name}")
async def get_all_transactions():
    pass

#get transaction by transaction code
@router.get("/get-transaction-by-code/{transaction_code}")
async def get_transaction_by_code():
    pass