import json
import pathlib
from typing import Union
from fastapi import FastAPI
from functools import lru_cache
from .auth_routes import auth_router
from .admin_routes import admin_router
from .quiz_routes import quiz_router
from .default_routes import default_router
#from .config import Settings

app = FastAPI()

""" @lru_cache()
def get_settings():
    return Settings() """

app.include_router(default_router)
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(quiz_router)