#imports
from fastapi import APIRouter, Body, Path, HTTPException
from app.schemas.user import UserLogin, UserRegister, UserUpdate, CashierLogin, CashierRegister, CashierUpdate
from app.models.user import User
from app.models.store import Store
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from app.database import engine
from http import HTTPStatus
from passlib.context import CryptContext
import uuid

#API router for authentication
router = APIRouter()
session = async_sessionmaker(bind=engine, expire_on_commit=False)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Authentication system class
class system():
    #store
    async def check_store_code(self, async_session: async_sessionmaker[AsyncSession], store: Store):
        async with async_session() as session:
            statement = select(Store).where(Store.store_code == store.store_code)
            result = await session.execute(statement)
            return result

    #User
    async def register(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def login(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            statement = select(User).where(
                (User.username == user.username) & 
                (User.hashed_password == user.hashed_password)
            )
            result = await session.execute(statement)
            return result.scalars().first()
    
    #Cashier
    async def cashier_register(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def cashier_login(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            statement = select(User).where(
                (User.username == user.username) & 
                (User.hashed_password == user.hashed_password) &
                (User.role == "cashier") &
                (User.store_code == user.store_code)
            )
            result = await session.execute(statement)
            return result.scalars().first()
    
        
db = system()

#admin routes
#Login route
@router.post("/login", status_code=HTTPStatus.OK)
async def login(login_data: UserLogin = Body(...)):
    async with session() as db_session:
        # Ambil user berdasarkan username
        result = await db_session.execute(select(User).where(User.username == login_data.username))
        user = result.scalars().first()

        if not user:
            raise HTTPException(status_code=401, detail="Invalid username or password")

        # Verifikasi password
        if not pwd_context.verify(login_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid username or password")

        # Kalau sukses, return user tanpa password
        return {
            "id": str(user.id),
            "username": user.username,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "message": "Login successful"
        }

#Registration route
@router.post("/register", status_code=HTTPStatus.CREATED)
async def register(register_data: UserRegister = Body(description="User registration")):
    new_user = User(
        id=str(uuid.uuid4()),
        name=register_data.name,
        username=register_data.username,
        email=register_data.email,
        hashed_password=pwd_context.hash(register_data.hashed_password),
        role="user"
    )

    user = await db.register(session, new_user)
    return user

#Update route
@router.put("/update/user")
def update_user(user: UserUpdate = Path(description="User update")):
    return user, {"message": "User updated successfully"}

@router.delete("/delete/{user_id}")
def delete_user(user_id: str = Path(description="User ID to delete")):
    return {"user_id": user_id, "message": "User deleted successfully"}

#cashier routes
#Login route
@router.post("/login/cashiers")
def login_cashiers(user: CashierLogin = Path(description="Cashier login")):
    return user, {"message": "Cashiers login successfully"}

#Registration route
@router.post("/register/cashiers")
def register_cashiers(user: CashierRegister = Path(description="Cashier registration")):
    return user, {"message": "Cashiers register successfully"}

#Update route
@router.put("/update/cashiers")
def update_cashiers(user: CashierUpdate = Path(description="Cashier update")):
    return user, {"message": "Cashiers updated successfully"}

@router.delete("/delete/cashiers/{user_id}")
def delete_cashiers(user_id: str = Path(description="Cashier ID to delete")):
    return {"user_id": user_id, "message": "Cashiers deleted successfully"}