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
        
    