# IMPORTS
import datetime

# DateTime

# Dummy database
from db.user_db import UserInDB
from db.user_db import save_user, get_user, eliminate_user

# Models
from models.user_models import UserIn, UserOut

# FastAPI and HTTPException
from fastapi import FastAPI, HTTPException

# CORS Policy

from fastapi.middleware.cors import CORSMiddleware

doku = FastAPI()

# List of permited origins

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://doku-api.herokuapp.com"
]

# Adding CORS policy execution

doku.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

#MAIN PAGE FOR THE DOKU WEB APPLICATION
@doku.get("/")
async def doku_main():
    pass

# ADMINISTRATION MODULES HTTP METHODS
# POST HTTP method to create a new user
@doku.post("/user/admon/create/")
async def create_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)

    if user_in_db != None:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    user_creation = UserInDB(**user_in.dict(), files = 0)

    user_creation = save_user(user_creation)
    return {"Creación": True}

# GET HTTP method to consult an existing user
@doku.get("/user/admon/search/")
async def search_user(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

# PUT HTTP method to update an existing user
@doku.put("/user/admon/update/")
async def update_user():
    pass

# DELETE HTTP method to delete an existing user
@doku.delete('/user/admon/delete/')
async def delete_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=400, detail="Password incorrecto")
    user_deleted = eliminate_user(user_in_db.username)
    user_out = UserOut(**user_deleted.dict())
    return {"Eliminado": user_out}

# AUTHENTICATION MODULE HTTP METHODS
# GET HTTP method to obtain login information
@doku.get("/user/auth/login/")
async def auth_user():
    pass

# PUT HTTP method to update password
@doku.put("/user/auth/password-reset/")
async def reset_user_password():
    pass

# ARCHIVE MODULE HTTP METHODS
# POST HTTP method for documents uploading
@doku.post("/storage/archive/upload/")
async def upload_file():
    pass

# GET HTTP method for documents downloading
@doku.post("/storage/archive/download/")
async def download_file():
    pass

# DELETE HTTP method for documents removal
@doku.delete("/storage/archive/delete/")
async def delete_file():
    pass

# PUT HTTP method for documents data update
@doku.put("/storage/archive/update/")
async def update_file():
    pass

# NOTIFICATIONS MODULE HTTP METHODS
# POST HTTP method to create notifications
@doku.post("/storage/notifications/create/")
async def create_notification():
    pass

# DELETE HTTP method for notifications removal
@doku.delete("/storage/notifications/delete/")
async def delete_notification():
    pass

# GET HTTP method to show a notification
@doku.get("/storage/notifications/show/")
async def show_notification():
    pass
