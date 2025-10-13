from dotenv import load_dotenv
load_dotenv()  


from fastapi import FastAPI, Depends, Header
from pydantic import BaseModel, ConfigDict, Field
from datetime import date
from typing import Optional, Literal
import os
from sqlalchemy.orm import Session, declarative_base, Mapped
from sqlalchemy import create_engine , Numeric, String, Date, Column, Integer


# ---- DB ---- #
DB_URL = os.getenv("STRING_CONNECTION", "")
engine = create_engine(DB_URL, future=True)

Base = declarative_base()

def get_db():
    with Session(engine) as s:
        yield s



class Transaction(Base):
    __tablename__ = "app_transactions"
    id: Mapped[int] = Column(Integer,primary_key=True,autoincrement=True)
    date: Mapped[date] = Column(Date, index=True)
    amount: Mapped[float] = Column(Numeric(12, 2))
    currency: Mapped[str] = Column(String(3), default="BRL")
    type: Mapped[str] = Column(String(10))  # "debit" | "credit"
    description: Mapped[Optional[str]] = Column(String(255), default=None)
    category: Mapped[str] = Column(String(10)) 

# cria as tabelas
Base.metadata.create_all(engine)


# ---- SCHEMAS ----
class TransactionOut(BaseModel):
    id: int
    date : date
    amount: float
    currency: str
    type: str
    description : Optional[str]
    model_config = ConfigDict(from_attributes=True)
    
class TransactionIn(BaseModel):
    date: date
    amount: float = Field(gt=0) #se receber valor <= 0 o pydantic lanca um 422
    currency: str = Field(default="Real")
    type: Literal["debito", "credito"]
    category: str
    description: Optional[str] = None

app = FastAPI()

transations = []

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/v1/transactions", response_model=TransactionOut,status_code=201)
def create_transation(
    payload: TransactionIn, 
    db: Session = Depends(get_db)):
    print("request realizada")
    transaction = Transaction(
        date=payload.date,
        amount=payload.amount,
        currency=payload.currency,
        type=payload.type,
        description=payload.description,
        category=payload.category
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)   
    
    return transaction

