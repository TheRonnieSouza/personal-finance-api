from app.common.base_entity import BaseEntity
from datetime import date 

class Transaction():
    
    def __init__(self, phone_number: str, name: str, date: date, amount: float, currency: str, type: str, description: str, category: str):
        self.phone_number = phone_number
        self.name = name
        self.date = date
        self.amount = amount 
        self.currency = currency
        self.type = type
        self.description = description
        self.category = category
        
    def add(self, phone_number:str, name:str , date: date, amount: float, currency: str, type: str, description: str, category:str):
        self.phone_number = phone_number
        self.name = name
        self.date = date
        self.amount = amount 
        self.currency = currency 
        self.type = type
        self.description = description
        self.category = category
        
    def __str__(self):
        return (f"Transaction(id={getattr(self, 'id', None)},"
                f"name='{self.name}', "
                f"phone_number='{self.phone_number}',"
                f"amount={self.amount},"
                f"currency='{self.currency}',"
                f"type='{self.type}', "
                f"category='{self.category}')")
    
    def __repr__(self):
        return self.__str__()