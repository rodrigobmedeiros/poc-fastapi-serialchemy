from pydantic import BaseModel

from models import User
from models import Item 

from typing import List

class ItemSchema(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int
class UserSchema(BaseModel):
    id: int 
    email: str
    hashed_password: str
    is_active: bool

