from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
#from sqlalchemy_utils import database_exists, create_database
import os

URL_DATABASE = "{}://{}:{}@{}:{}/{}".format(
    os.getenv("DB_ENGINE"),
    os.getenv("DB_USER"),
    os.getenv("DB_PASSWORD"),
    os.getenv("DB_HOST"),
    os.getenv("DB_PORT"),
    os.getenv("DB_NAME"),
)
engine = create_engine(URL_DATABASE, echo=True)
session = sessionmaker(bind=engine)
Base = declarative_base()
print(engine.url)
