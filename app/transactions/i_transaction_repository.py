from abc import ABC, abstractmethod
from .transaction import Transaction

class ITransactionRepository(ABC):
    @abstractmethod
    def save(self, transaction: Transaction) ->  Transaction:
        pass