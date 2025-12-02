from .get_transactions_query import GetTransactionsQuery
from app.transactions.i_transaction_repository import ITransactionRepository
from app.transactions.transaction import Transaction
import logging
from typing import List

logger = logging.getLogger(__name__)

class GetTransactionsQueryHandler:
    
    def __init__(self, repository: ITransactionRepository):
        self.repository = repository
        pass
    
    def handle(self, query: GetTransactionsQuery) -> List[Transaction]:
        
        transactions = self.repository.get(query.phone_number)
        
        if not transactions:
            logger.warning("No transactions found")
            raise ValueError("Transactions not found.")
       
        return transactions 
       
        
        