from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional, Literal
import os
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import create_engine, Numeric, String, Date, Column, Integer

# ---- DB ---- #
DB_URL = os.getenv("STRING_CONNECTION", "")
engine = create_engine(DB_URL, future=True)

Base = declarative_base()

def get_db():
    with Session(engine) as s:
        yield s

# ---- DATABASE MODEL ---- #
class Transaction(Base):
    __tablename__ = "app_transactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String(20))
    name = Column(String(30))
    date = Column(Date, index=True)
    amount = Column(Numeric(12, 2))
    currency = Column(String(3), default="BRL")
    type = Column(String(10))  # "debito" | "credito"
    description = Column(String(255), default=None)
    category = Column(String(50))  # Increased size for categories

# Create tables
Base.metadata.create_all(engine)

# ---- SCHEMAS ----
class TransactionOut(BaseModel):
    id: int
    phone_number: int
    name: str
    date: date
    amount: float
    currency: str
    type: str
    description: Optional[str]
    category: str
    model_config = ConfigDict(from_attributes=True)
    
class TransactionIn(BaseModel):
    phone_number : int
    name: str
    date: date
    amount: float = Field(gt=0)
    currency: str = Field(default="BRL")  # Fixed to 3 characters
    type: Literal["debito", "credito"]
    category: str
    description: Optional[str] = None


class AgentTransactionIn(BaseModel):
    transaction: TransactionIn


app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/v1/transactions")
def get_transactions(phone_number: Optional[str] = None, db: Session = Depends(get_db)):
    if phone_number:
        transactions = db.query(Transaction).filter(Transaction.phone_number ==  phone_number).all()
    elif not phone_number:
        transactions = db.query(Transaction).all()
    return {"transactions": transactions}

@app.post("/v1/transactions", response_model=TransactionOut, status_code=201)
def create_transaction(payload: TransactionIn, db: Session = Depends(get_db)):
    print("request realizada")
    transaction = Transaction(
        phone_number=payload.phone_number,
        name=payload.name,
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


@app.post("/v1/transactions/agent", response_model=TransactionOut, status_code=201)
def create_agent_transaction(payload: AgentTransactionIn, db: Session = Depends(get_db)):
    print("Agent request realizada")
    transaction = Transaction(        
        name=payload.transaction.name,
        phone_number=payload.transaction.phone_number,
        date=payload.transaction.date,
        amount=payload.transaction.amount,
        currency= payload.transaction.currency,
        type=payload.transaction.type,
        description=payload.transaction.description,
        category=payload.transaction.category
    )
    
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    
    return transaction
    

# Simple runner without uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

