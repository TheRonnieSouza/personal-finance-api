from app.transactions.i_transaction_repository import ITransactionRepository
from .delete_transaction_command import DeleteTransactionCommand
import logging 

logger = logging.getLogger(__name__)

class DeleteTransactionCommandHandler:
    
    def __init__(self, repository: ITransactionRepository):
        self.repository = repository
    
    def handle(self, id: int, command: DeleteTransactionCommand) -> bool:
        
        logger.info(f"geting transaction with id: {id}")
        transaction = self.repository.get_by_id(id)
        
        logger.info(f"Deleting transaction with id: {id}")
        if not transaction.phone_number == command.phone_number:
            logger.info(f"error phone number diferent")
            return False
        
        logger.info(f"Deleting transaction with id: {id}")
        self.repository.delete(transaction=transaction)
        return True