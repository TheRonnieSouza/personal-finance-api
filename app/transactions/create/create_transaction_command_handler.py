from .create_transaction_command import CreateTransactionCommand
from app.transactions.i_transaction_repository import ITransactionRepository
from app.transactions.transaction import Transaction

class CreateTransactionCommandHandler:
    
    def __init__(self, repository: ITransactionRepository):
        self.repository = repository
            
    def handle(self, command: CreateTransactionCommand) -> Transaction:
        print("Handle was called!")
        
        transaction = Transaction(
            name=command.name,
            phone_number=command.phone_number,
            currency=command.currency,
            date=command.date,
            amount=command.amount,
            category=command.category,
            description=command.description,
            type=command.type
        )
        
        return self.repository.save(transaction=transaction)
        