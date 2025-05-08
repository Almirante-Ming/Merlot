import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, DateTime, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("Erro na variavel DATABASE_URL!")

engine = create_engine(DATABASE_URL)  #é uma função que cria uma instância do "engine" para gerenciar a conexão com o banco de dados
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()