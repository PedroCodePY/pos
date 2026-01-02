#imports
from fastapi import APIRouter, Path
from app.schemas.user import UserLogin, UserRegister, UserUpdate, CashierLogin, CashierRegister, CashierUpdate
from app.models.user import User
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select

router = APIRouter()

class crud():
    async def get_user(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            statement = select(User).group_by(User.id)
            result = await session.execute(statement)
            return result.scalars()
        
    async def add_user(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

#admin routes
#Login route
@router.post("/login")
def login(user: UserLogin = Path(description="User login")):
    return user, {"message": "Login successful"}

#Registration route
@router.post("/register")
def register(user: UserRegister = Path(description="User registration")):
    return user, {"message": "Registration successful"}

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