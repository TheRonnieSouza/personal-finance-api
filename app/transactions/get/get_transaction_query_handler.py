from .get_transaction_query import GetTransactionQuery
from app.transactions.i_transaction_repository import ITransactionRepository
from app.transactions.transaction import Transaction
import logging

logger = logging.getLogger(__name__)

class GetTransactionQueryHandler():
    
    def __init__(self,repository:ITransactionRepository):
        self.repository = repository
        
    def handle(self, query:GetTransactionQuery) -> Transaction: 
        
        transaction = self.repository.get_by_id(query.id)
        
        if not transaction:
            logger.warning(f"Transaction with id {query.id} not found")
            raise ValueError(f"Transaction with id {query.id} not found")
        
        if transaction.phone_number != query.phone_number:
            logger.warning(f"Phone number mismatch for transaction {query.id}")
            raise ValueError("You don't have permission to access this transaction")
        
        logger.info(f"Transaction {query.id} found and validated")

        return transaction        

