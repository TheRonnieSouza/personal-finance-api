from fastapi import APIRouter, Path, Query, HTTPException, Depends, status
from app.transactions.transaction import Transaction
from app.transactions.get.get_transaction_query import GetTransactionQuery
from app.transactions.get.get_transaction_query_handler import GetTransactionQueryHandler 
from app.transactions.i_transaction_repository import ITransactionRepository
from app.transactions.create.create_transaction_command import  CreateTransactionCommand
from app.transactions.create.create_transaction_command_handler import  CreateTransactionCommandHandler
from app.transactions.update.update_command import UpdateTransactionCommand
from app.transactions.update.update_command_handler import UpdateTransactionCommandHandler
from app.infra.dependencies import get_transaction_repository
from app.api.models.transaction_response import TransactionResponse
from typing import Optional
from app.transactions.delete.delete_transaction_command import DeleteTransactionCommand
from app.transactions.delete.delete_transaction_command_handler import DeleteTransactionCommandHandler

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
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.exception(f"Unexpected error updating transaction id={id}: {str(e)} ")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while updating the transaction: {str(e)}"
        )

@router.put("/v2/transaction/{id}", response_model= TransactionResponse, status_code=status.HTTP_200_OK, tags=tags)
def update_transaction(id: int, payload: UpdateTransactionCommand,
                       repository: ITransactionRepository = Depends(get_transaction_repository)):
    try:
        handler = UpdateTransactionCommandHandler(repository)
        
        result = handler.handle(id, payload)
        return TransactionResponse.model_validate(result)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.delete("/v2/transaction/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=tags)
def delete_transaction(id: int = Path(description="Transaction id", gh=0),
                       phone_number: str = Query(None, description="Phone number"),
                       repository: ITransactionRepository = Depends(get_transaction_repository)):
    
    try: 
        command = DeleteTransactionCommand(phone_number=phone_number)
        handler = DeleteTransactionCommandHandler(repository)
        
        result = handler.handle(id, command,)
        if result:
            return status.HTTP_204_NO_CONTENT
        
        return status.HTTP_404_NOT_FOUND
            
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.get("/v2/transaction/{id}", status_code=status.HTTP_200_OK, tags=tags)
def get_transaction_by_id(id: int, 
                          phone_number:str = Query(None,description="Phone number"), 
                          repository:ITransactionRepository = Depends(get_transaction_repository)):      
    
    try: 
        Querytransaction = GetTransactionQuery(id=id, phone_number=phone_number)
        handler = GetTransactionQueryHandler(repository=repository)
        transaction = handler.handle(Querytransaction)
        
        if transaction:
            return TransactionResponse.model_validate(transaction)
            
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaction with id {id} not found.")
        
    except ValueError as e:
        error_msg = str(e).lower()
        
        if "not found" in error_msg:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))
        if "permission" in error_msg:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred while fetching the transaction {str(e)}") 
    
        