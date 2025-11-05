#import fastapi 
from typing import List, Optional
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from UserUpdateRequest import UserUpdateRequest
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

#creating an endpoint to create a new user 
#we can ahve the same path since this is a different HTTP method 
@app.post("/api/v1/users")
#it will take in a parameter, user 
async def create_user(user: User):
    #add the user to the database 
    db.append(user) 
    return {"id": user.id}

#deleting users 
#deleting the users base doff user id 
@app.delete("/api/v1/users/{user_id}")
#taking in the user id, of type UUID 
#if we try deleting a user that doesnt exist, we should get a 404 ('not found') error 
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id: 
            db.remove(user) 
            #coming out of the loop once we find the user 
            return 
    #if the condition isnt met, meaning we dont find a user with this id, lets raise an exception
    #we are returning the 404 error, code and providing some detail as well 
    raise HTTPException(
        status_code = 404, 
        detail =f"user with id {user_id} does not exist"
    )

#updating a user 
@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, update_user: UserUpdateRequest):
    #first finding the user with the matching id 
    for user in db:
        if user_id == user_id:
            #we are updating all the fields in the user that aren't none (meaning that we dont have to update those)
            #after updating all of we can break out of the loop 
            if update_user.first_name is not None:
                user.first_name = update_user.first_name
            if update_user.last_name is not None:
                user.last_name = update_user.last_name
            if update_user.middle_name is not None:
                user.middle_name = update_user.middle_name
            if update_user.roles is not None:
                user.roles = update_user.roles
            return
    raise HTTPException(
        status_code = 404,
        detail = f"user with id {user_id} not found"
    )
    