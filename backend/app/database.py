from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

URL_DATABASE = os.getenv("DATABASE_URL")

engine = create_engine(URL_DATABASE)
con = engine.connect()

con.execute(text("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE NOT NULL, password VARCHAR(100) NOT NULL);"))

con.commit()