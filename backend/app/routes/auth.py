#imports
from fastapi import APIRouter, Path
from app.schemas.user import UserLogin, UserRegister, UserUpdate, CashierLogin, CashierRegister, CashierUpdate
from app.models.user import User
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from app.database import engine
from http import HTTPStatus

#API router for authentication
router = APIRouter()
session = async_sessionmaker(bind=engine, expire_on_commit=False)

#Authentication system class
class system():
    async def register(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def login(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            statement = select(User).where(User.username == user.username, User.password == user.password)
            result = await session.execute(statement)
            return result.scalars()
        
db = system()

#admin routes
#Login route
@router.post("/login", status_code=HTTPStatus.OK)
def login(login_data: UserLogin = Path(description="User login")):
    pass

#Registration route
@router.post("/register", status_code=HTTPStatus.CREATED)
def register(register_data: UserRegister = Path(description="User registration")):
    new_user = User(
        name=register_data.name,
        username=register_data.username,
        email=register_data.email,
        hashed_password=register_data.hashed_password
    )

    user = db.register(session, new_user)
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