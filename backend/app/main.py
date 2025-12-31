#imports
from fastapi import FastAPI
from routes import auth, product

# Initialize FastAPI app
app = FastAPI()

# Include authentication routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(product.router, prefix="/product", tags=["product"])