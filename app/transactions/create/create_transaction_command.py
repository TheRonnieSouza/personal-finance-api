from datetime import date
from pydantic import BaseModel

#TODO Abstrair depencia de pydantic
class CreateTransactionCommand(BaseModel):
    phone_number: str
    name: str
    date: date
    amount: float
    currency: str
    type: str
    description: str
    category: str