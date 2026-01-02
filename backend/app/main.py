#imports
from fastapi import FastAPI
from app.routes import auth, product, transaction

# Initialize FastAPI app
app = FastAPI()

#test api
@app.get("/")
def read_root():
    return {"message": "Welcome to the POS system API"}

# Include authentication routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(product.router, prefix="/product", tags=["product"])
app.include_router(transaction.router, prefix="/transaction", tags=["transaction"])