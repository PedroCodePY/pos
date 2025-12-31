#imports
from fastapi import APIRouter, Path
from pydantic import BaseModel
from models.user import UserLogin, UserRegister

router = APIRouter()

#Login route
@router.post("/login")
def login(user: UserLogin):
    return user, {"message": "Login successful"}

#Registration route
@router.post("/register")
def register(user: UserRegister):
    return user, {"message": "Registration successful"}