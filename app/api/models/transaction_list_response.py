from typing import List
from pydantic import BaseModel
from .transaction_response import TransactionResponse

class TransactionListResponse(BaseModel):
    total: int
    transactions: List[TransactionResponse]
        
    class Config:
        from_attributes = True