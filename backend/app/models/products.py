from pydantic import BaseModel
from typing import Optional
from app.database import Base

# Model representing a product in the system
class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    in_stock: bool

# Model for updating product details
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None