from pydantic import BaseModel
from ..database import Base

class Transaction(BaseModel):
    id: str
    product_id: str
    quantity: int
    total_price: float
    timestamp: str