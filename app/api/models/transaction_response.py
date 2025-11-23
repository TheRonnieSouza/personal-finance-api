from pydantic import BaseModel
from app.transactions.transaction import Transaction
from datetime import date

class TransactionResponse(BaseModel):
    id: int
    name: str
    date: date
    amount: float
    currency: str
    type: str
    description: str | None
    category: str
    
    class Config:
        from_attributes = True