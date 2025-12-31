from pydantic import BaseModel

# Model representing a product in the system
class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    in_stock: bool