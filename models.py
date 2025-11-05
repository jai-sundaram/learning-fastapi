#we are using pydantic 
#pydantic is used for data validation
#data validation basically means checking that the data that comes into your program is correct, complete and in the correct format 
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import List, Optional
from enum import Enum 
#an enum is a special class that is used to define a set of fixed values 
#used to restrict a variable so it can only take predefined values 
class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
class User(BaseModel):
    # now let us define the attributes 
    #the data type for id is UUID, which is a universally unique identifier
    #uui4 basically generated a random unique id automatically if one isnt provided 
    id: Optional[UUID] = uuid4()
    first_name: str 
    last_name: str 
    middle_name: Optional[str] = None 
    gender: Gender 
    roles: List[Role]
    