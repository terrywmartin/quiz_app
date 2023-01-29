import json
import pathlib
import requests
from fastapi import APIRouter, FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .database import Session,engine
from .models import Country
from .config import get_settings, Settings


default_router = APIRouter(
    tags=["default"]
)
BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

session = Session(bind=engine)

@default_router.get("/", response_class=HTMLResponse)
async def get_homes(request: Request, settings: Settings = Depends(get_settings)):
    context = {
        "request": request,
        "app_name": settings.APP_NAME
    }
    return templates.TemplateResponse("index.html", context)
