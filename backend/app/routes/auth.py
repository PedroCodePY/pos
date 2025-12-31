#imports
from fastapi import APIRouter, Path
from models.user import UserLogin, UserRegister

router = APIRouter()

#Login route
@router.post("/login")
def login(user: UserLogin = Path(description="User login")):
    return user, {"message": "Login successful"}

#Registration route
@router.post("/register")
def register(user: UserRegister = Path(description="User registration")):
    return user, {"message": "Registration successful"}