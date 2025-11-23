from sqlalchemy import Column, Integer, String, Date, Numeric
from app.infra.database import Base

class TransactionModel(Base):
    __tablename__ = "app_transactions"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String(20))
    name = Column(String(30))
    date = Column(Date, index=True)
    amount = Column(Numeric(12,2))
    currency = Column(String(3), default="BRL")
    type = Column(String(10))
    description = Column(String(255), default=None)
    category = Column(String(50))