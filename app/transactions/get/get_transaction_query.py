from pydantic import BaseModel

class GetTransactionQuery(BaseModel):
    
    id: int 
    phone_number: str
    '''
    def __init__(self, id: int, phone_number:str):
        self.id = id
        self.phone_number = phone_number
        
        '''