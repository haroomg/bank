from pydantic import BaseModel
from pydantic.types import datetime

class CreateUserSchema (BaseModel):

    user_name: str
    first_name: str
    last_name: str
    email: str
    phone: str
    ci: str
    address: str
    password: str
    birthdate: datetime
