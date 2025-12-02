from pydantic import BaseModel

class GetTransactionsQuery(BaseModel):
    phone_number: str