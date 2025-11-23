#Container DI

from fastapi import Depends
from sqlalchemy.orm import Session
from app.infra.database import get_db
from app.infra.transaction_repository import TransactionRepository
from app.transactions.i_transaction_repository import ITransactionRepository

def get_transaction_repository(db: Session = Depends(get_db)) -> ITransactionRepository:
    return TransactionRepository(db)