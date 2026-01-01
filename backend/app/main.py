#imports
from fastapi import FastAPI
from routes import auth, product

# Initialize FastAPI app
app = FastAPI()

#test api
@app.get("/")
def read_root():
    return {"message": "Welcome to the POS system API"}

# Include authentication routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(product.router, prefix="/product", tags=["product"])