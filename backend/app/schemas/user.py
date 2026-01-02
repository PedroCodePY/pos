#Import necessary libraries
from pydantic import BaseModel
from typing import Optional

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