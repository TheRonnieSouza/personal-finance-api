from abc import ABC, abstractmethod
from .transaction import Transaction
from typing import List, Optional

class ITransactionRepository(ABC):
    @abstractmethod
    def save(self, transaction: Transaction) ->  Transaction:
        pass
    
    @abstractmethod
    def update(self, transaction: Transaction) -> Transaction:
        pass
    
    @abstractmethod
    def get_by_id(self, id:int) -> Transaction:
        pass
    
    @abstractmethod
    def delete(self, transaction: Transaction) -> None:
        pass
    
    @abstractmethod
    def get(self, phone_number:Optional[str]= None) -> List[Transaction]:
        pass 