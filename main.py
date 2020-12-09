from db.user_db import UserInDB
from db.user_db import update_user, get_user

from models.user_models import UserIn, UserOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()
