import json
import pathlib
from fastapi import APIRouter, FastAPI, Request

quiz_router = APIRouter(
     prefix="/quiz",
    tags=["quiz"]
)

@quiz_router.get('/')
async def quiz_view(request: Request):
   
   return { "data": "quiz", "status": "200" }