import json
import pathlib
from fastapi import APIRouter, FastAPI, Request

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@auth_router.get('/')
async def test_view(request: Request):
   return { "data": "auth", "status": "200" }