#imports
from fastapi import APIRouter, Body, Path, HTTPException, status
from app.schemas.user import UserLogin, UserRegister, UserUpdate, CashierLogin, CashierRegister, CashierUpdate
from app.models.user import User
from app.models.store import Store
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.database import engine
from http import HTTPStatus
from passlib.context import CryptContext
from app.function.auth_function import system
import uuid

#API router for authentication
router = APIRouter()
session = async_sessionmaker(bind=engine, expire_on_commit=False)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
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
@router.post("/login/cashiers", status_code=HTTPStatus.OK)
async def login_cashiers(login_data: CashierLogin = Body(description="Cashier login")):
    user = await db.cashier_login(session, login_data)
    return user

#Registration route
@router.post("/register/cashiers", status_code=HTTPStatus.CREATED)
async def register_cashiers(register_data: CashierRegister = Body(description="Cashier registration")):
    new_cashier = User(
        id=str(uuid.uuid4()),
        name=register_data.name,
        username=register_data.username,
        email=register_data.email,
        hashed_password=pwd_context.hash(register_data.hashed_password),
        role="cashier",
        code_shop=register_data.code_shop
    )

    user = await db.cashier_register(session, new_cashier)
    return user

#Update route
@router.put("/update/cashiers")
def update_cashiers(user: CashierUpdate = Path(description="Cashier update")):
    return user, {"message": "Cashiers updated successfully"}

@router.delete("/delete/cashiers/{user_id}")
def delete_cashiers(user_id: str = Path(description="Cashier ID to delete")):
    return {"user_id": user_id, "message": "Cashiers deleted successfully"}