from typing import List, Optional
from pydantic import BaseModel

from models import Role
#this model is basically used to update a user entry in the database 

class UserUpdateRequest(BaseModel):
    first_name: Optional[str] = None 
    last_name: Optional[str] = None
    middle_name: Optional[str] = None 
    roles: Optional[List[Role]] = None 