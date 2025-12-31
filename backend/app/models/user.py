from pydantic import BaseModel

# User models for authentication
#Login Models
class UserLogin(BaseModel):
    username: str
    password: str

#Registration Models
class UserRegister(BaseModel):
    username: str
    email: str
    password: str