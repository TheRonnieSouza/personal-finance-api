from .update_command import UpdateTransactionCommand
from app.transactions.i_transaction_repository import ITransactionRepository
from app.transactions.transaction import Transaction
import logging

logger = logging.getLogger(__name__)

class UpdateTransactionCommandHandler():
    
    def __init__(self, repository: ITransactionRepository):
        self._repository = repository
            
    def handle(self, id:int, command:UpdateTransactionCommand) -> Transaction:
        
        logger.info(f"Executing handle()")
        transaction = self._repository.get_by_id(id)
        
        logger.info(f"get_by_id executed transaction= {str(transaction)}")
        if not transaction:
            logger.error(f"Transaction not founded!")
            raise  ValueError(f"Transaction with id {id} not found")
        
        transaction.name = command.name
        transaction.phone_number = command.phone_number
        transaction.amount = command.amount
        transaction.type = command.type
        transaction.date = command.date
        transaction.description = command.description
        transaction.category = command.category
        transaction.currency = command.currency
        
        return self._repository.update(transaction)    
        