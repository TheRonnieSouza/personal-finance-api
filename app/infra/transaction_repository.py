from app.transactions.i_transaction_repository import ITransactionRepository
from app.transactions.transaction import Transaction
from app.infra.models.transaction_model import TransactionModel
from sqlalchemy.orm import Session, declarative_base
import logging

logger = logging.getLogger(__name__)

class TransactionRepository(ITransactionRepository):
    def __init__(self, session: Session):
        self._session = session
       
    def save(self, transaction: Transaction) -> Transaction:
        
        model = self.to_model(transaction)
        
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return self.to_entity(model)
    
    def update(self, transaction:Transaction) -> Transaction:
        try:
            
           model = self._session.get(TransactionModel, transaction.id)
           
           if not model:
            raise ValueError(f"Transaction with id {transaction.id} not found")
        
           model.name = transaction.name
           model.phone_number = transaction.phone_number
           model.amount = transaction.amount
           model.type = transaction.type
           model.date = transaction.date
           model.description = transaction.description
           model.category = transaction.category
           model.currency = transaction.currency
           
           self._session.commit()
           self._session.refresh(model)
        
           return self.to_entity(model)
        except Exception as e:
            logger.exception(f"Error to update transaction. error:{str(e)}")
            self._session.rollback()
            raise e
    
    def get_by_id(self, id) -> Transaction:  
        try:
            model = self._session.get(TransactionModel, id)
            
            if not model:
               raise ValueError(f"Transaction with id {id} not found")
            
        except Exception as e:
            logger.exception(f"Error fetching transaction id={id}: {str(e)}")
            raise e         
              
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