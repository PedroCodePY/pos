from pydantic import BaseModel
from typing import Optional
from ..database import Base
from sqlalchemy import Column, String, Boolean, Integer

#database table for users
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=True, unique=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), default="user")

# User models for authentication
#Admin Models
#Login Models
class UserLogin(BaseModel):
    username: str
    password: str

#Registration Models
class UserRegister(BaseModel):
    username: str
    email: str
    password: str

#Update Models
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

#Cashier Models
#Login Models
class CashierLogin(BaseModel):
    username: str
    password: str
    shop_code: str

#Registration Models
class CashierRegister(BaseModel):
    username: str
    email: str
    password: str
    shop_code: str

#Update Models
class CashierUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    shop_code: Optional[str] = None