#imports
from fastapi import APIRouter, Body, Path, HTTPException, status
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
            return result.scalar.first()

    #User
    async def register(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def login_user(self, async_session, username: str, password: str):
        async with async_session() as session:
            result = await session.execute(
                select(User).where(User.username == username)
            )
            user = result.scalars().first()

            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )

            if user.code_shop:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Unauthorized access for cashiers",
                )

            if not pwd_context.verify(password, user.hashed_password):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect password or username  ",
                )

            return {
                "id": user.id,
                "username": user.username,
                "role": user.role
            }
    
    #Cashier
    async def cashier_register(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def cashier_login(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            store_code = self.check_store_code(session, user.store_code)
            if not store_code:
                raise HTTPException(status_code=401, detail="Invalid store code")
            else:
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
async def login(data: UserLogin = Body(description="User login")):
    user = await db.login_user(session, data.username, data.password)
    return user

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
async def login_cashiers(login_data: CashierLogin = Body(description="Cashier login")):
    async with session() as db_session:
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