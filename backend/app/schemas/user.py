#Import necessary libraries
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

# User models for authentication
#Admin Models
class User(BaseModel):
    id: str
    username: str
    name: str
    email: str
    hashed_password: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

#Login Models
class UserLogin(BaseModel):
    username: str
    password: str

    model_config = ConfigDict(from_attributes=True)

#Registration Models
class UserRegister(BaseModel):
    username: str
    name: str
    email: str
    hashed_password: str

    model_config = ConfigDict(from_attributes=True)

#Update Models
class UserUpdate(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    

#Cashier Models
#Login Models
class CashierLogin(BaseModel):
    username: str
    hashed_password: str
    code_shop: str

    model_config = ConfigDict(from_attributes=True)

#Registration Models
class CashierRegister(BaseModel):
    username: str
    name: str
    email: str
    hashed_password: str
    code_shop: str

    model_config = ConfigDict(from_attributes=True)

#Update Models
class CashierUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None