#imports
from fastapi import FastAPI
from routes import auth

# Initialize FastAPI app
app = FastAPI()

# Include authentication routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])