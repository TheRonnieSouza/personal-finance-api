#Configuração centralizada do banco
import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

DB_URL = os.getenv("STRING_CONNECTION", "")
engine = create_engine(DB_URL, future=True)

Base = declarative_base()

def get_db():
    with Session(engine) as s:
        yield s