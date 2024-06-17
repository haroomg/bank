from pydantic import BaseModel

class CreateStaffSchema (BaseModel):
    
    username: str
    first_name: str
    last_name: str
    email: str
    password: str