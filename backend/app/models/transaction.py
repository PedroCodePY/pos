from pydantic import BaseModel

class Transaction(BaseModel):
    id: str
    product_id: str
    quantity: int
    total_price: float
    timestamp: str