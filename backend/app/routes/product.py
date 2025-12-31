from fastapi import APIRouter
from models.products import Product

router = APIRouter()

@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: str):
    for product in Product:
        if product_id == product.id:
            return product
    return {"error": "Product not found"}

@router.post("/add", response_model=Product)
async def add_product(product: Product):
    pass

