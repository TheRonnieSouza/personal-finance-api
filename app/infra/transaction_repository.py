from app.transactions.i_transaction_repository import ITransactionRepository
from app.transactions.transaction import Transaction
from app.infra.models.transaction_model import TransactionModel
from sqlalchemy.orm import Session, declarative_base

class TransactionRepository(ITransactionRepository):
    def __init__(self, session: Session):
        self._session = session
       
    def save(self, transaction: Transaction) -> Transaction:
        
        model = self.to_model(transaction)
        
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return self.to_entity(model)
    
    def to_model(self, transaction: Transaction) -> TransactionModel:
        
        return TransactionModel(
            id=transaction.id if hasattr(transaction, 'id') else None,
            phone_number=transaction.phone_number,
            name=transaction.name,
            date=transaction.date,
            amount=transaction.amount,
            currency=transaction.currency,
            type=transaction.type,
            description=transaction.description,
            category=transaction.category
        )
        
    def to_entity(self, model: TransactionModel) -> Transaction:
        transaction = Transaction(
            phone_number=model.phone_number,
            name=model.name,
            date=model.date,
            amount=float(model.amount),
            currency=model.currency,
            type=model.type,
            description=model.description,
            category=model.category
        )
        transaction.id = model.id  
        return transaction