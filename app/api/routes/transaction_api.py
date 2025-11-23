from fastapi import APIRouter, Path, Query, HTTPException, Depends
from app.transactions.transaction import Transaction
from app.transactions.i_transaction_repository import ITransactionRepository
from app.transactions.create.create_transaction_command import  CreateTransactionCommand
from app.transactions.create.create_transaction_command_handler import  CreateTransactionCommandHandler
from app.infra.transaction_repository import TransactionRepository
from app.infra.dependencies import get_transaction_repository


router = APIRouter()
'''
@router.get("/v2/transaction/{id}")
def get_transaction(id: int = Path(description="Transaction id"),
                    phone_number: str = Query(None, default="phone number")               
                    )
                    '''
#TODO create view model                    
@router.post("/v2/transaction", response_model= None, status_code=201, tags=["Transactions"])
def create_transaction(payload: CreateTransactionCommand, repository: ITransactionRepository = Depends(get_transaction_repository)):
    print("request post v2/transaction realizada!")
    
    handler = CreateTransactionCommandHandler(repository)
    
    result = handler.handle(payload)
    
    if result:
        return
    else:
        return HTTPException(400)
    