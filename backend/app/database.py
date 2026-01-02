from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
import os

#URL for the database connection
URL_DATABASE = "{}://{}:{}@{}:{}/{}".format(
    os.getenv("DB_ENGINE"),
    os.getenv("DB_USER"),
    os.getenv("DB_PASSWORD"),
    os.getenv("DB_HOST"),
    os.getenv("DB_PORT"),
    os.getenv("DB_NAME"),
)

#Create the database engine and session
engine = create_async_engine(URL_DATABASE, echo=True)

class Base(DeclarativeBase):
    pass
