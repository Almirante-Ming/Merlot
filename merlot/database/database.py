import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, DateTime, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv('.env')

database_url = os.getenv("DATABASE_URL")
if not database_url:
	raise ValueError("DATABASE_URL environment variable is not set")
engine = create_engine(database_url)  # type: ignore
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()