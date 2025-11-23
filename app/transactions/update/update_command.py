from pydantic import BaseModel
from datetime import date

class UpdateTransactionCommand(BaseModel):
    name: str
    phone_number: str
    currency: str
    type:str
    description: str | None
    category: str
    amount: float
    date: date
    