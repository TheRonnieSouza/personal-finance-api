from fastapi import APIRouter, Path, Query, HTTPException, Depends, status
from app.transactions.transaction import Transaction
from app.transactions.i_transaction_repository import ITransactionRepository
from app.transactions.create.create_transaction_command import  CreateTransactionCommand
from app.transactions.create.create_transaction_command_handler import  CreateTransactionCommandHandler
from app.transactions.update.update_command import UpdateTransactionCommand
from app.transactions.update.update_command_handler import UpdateTransactionCommandHandler
from app.infra.dependencies import get_transaction_repository
from app.api.models.transaction_response import TransactionResponse
import logging

logger = logging.getLogger(__name__)

router = APIRouter()
tags= ["Transactions"]                   
                              
@router.post("/v2/transaction", response_model= TransactionResponse, status_code=status.HTTP_201_CREATED, tags=tags)
def create_transaction(payload: CreateTransactionCommand, repository: ITransactionRepository = Depends(get_transaction_repository)):
    print("request post v2/transaction realizada!")
    try:
       logger.info(f"Received PUT request for transaction {id}")
       handler = CreateTransactionCommandHandler(repository)    
       result = handler.handle(payload)
       
       logger.info(f"Updated successful, returning response")
       return TransactionResponse.model_validate(result)
    
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        logger.exception(f"Unexpected error updating transaction id={id}: {str(e)} ")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while updating the transaction: {str(e)}"
        )

@router.put("/v2/transaction/{id}", response_model= TransactionResponse, status_code=status.HTTP_200_OK, tags=tags)
def update_transaction(id: int, payload: UpdateTransactionCommand, repository: ITransactionRepository = Depends(get_transaction_repository)):
    try:
        handler = UpdateTransactionCommandHandler(repository)
        
        result = handler.handle(id, payload)
        return TransactionResponse.model_validate(result)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    