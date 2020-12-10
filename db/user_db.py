from typing import Dict
from pydantic import BaseModel

# Definition UserInDB

class UserInDB(BaseModel):
    username: str
    password: str
    files: int


# Definition untrue DB 

database_users = Dict[str, UserInDB]

database_users = {
    "camilo24@mail.com": UserInDB(**{"username":"camilo24@mail.com",
                                    "password":"root",
                                    "files":1}),
    "andres18@mail.com": UserInDB(**{"username":"andres18@mail.com",
                                    "password":"hola",
                                    "files":0}),
    "Mayra14@mail.com": UserInDB(**{"username":"Mayra14@mail.com",
                                    "password":"hello",
                                    "files":0}),
    "kuga23@mail.com": UserInDB(**{"username":"kuga23@mail.com",
                                    "password":"1234",
                                    "files":2}),
}


# Defining functions on untrue DB


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def save_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db

