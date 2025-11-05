#import fastapi 
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import Gender, Role, User 



#create an instance of the fastapi application
app = FastAPI() 

#let us create the database 
#for now this will have a type of List 
#in this case a list of users 
#we need to have the [ on the same line as the = or it breaks 
db: List[User] = [
    #let us create some dummy users 
    #we can hardcode the id btw 
    User(id = UUID("6499b344-c368-46ec-b165-6f2c71b7b4cd"), first_name="Jane", last_name = "Doe", gender = Gender.female, roles = [Role.student]),
    User(id = UUID("c0a6f24d-a6ba-48cb-9619-f89b62babf40"), first_name="Alex", last_name = "Jones", gender = Gender.male, roles = [Role.admin, Role.user] )
]



#create a route for a get request 
#we need to specify the path/endpoint for the route
@app.get("/")
#create a function that will be called when we access this route 
#the async function tells us that we might need to wait for some tasks midway 
async def root():
    #the await keyword is used to actually make us wait for a certain task to be done 

    #await some tadsk

    #at this point, we don't really need to worry about await 
    return {"Hello": "Jai"}

'''
Remember the HTTP codes:
GET - gets the resource 
POST - creates the resource
PUT - updates the resource 
DELETE - deletes the resource 
'''

#now let us create a route to expose all the users in the list to the client 
@app.get("/api/v1/users")
async def fetch_users():
    return db

