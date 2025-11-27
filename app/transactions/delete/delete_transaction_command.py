from pydantic import BaseModel

class DeleteTransactionCommand(BaseModel):
    phone_number: str