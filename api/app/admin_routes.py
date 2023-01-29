import json
import pathlib
import requests
from fastapi import APIRouter, FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .database import Session,engine
from .models import Country
from .config import get_settings, Settings
from .celery_worker import update_country_table, init_database



admin_router = APIRouter(
     prefix="/admin",
    tags=["admin"]
)
BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

session = Session(bind=engine)

@admin_router.get("/status", response_class=HTMLResponse)
async def get_status(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("status.html", context)

@admin_router.get("/update-country", response_class=HTMLResponse)
async def update_countries(request: Request):
    status_code = ""
    msg = ""
    context = {
        "request": request,
        "msg": msg,
        "status_code": status_code
    }
    return templates.TemplateResponse("update-country.html", context)

@admin_router.get("/update", response_class=HTMLResponse)
async def update(request: Request, settings: Settings = Depends(get_settings)):
   task = update_country_table.delay()
   
   resp = task.get()
  
   status_code = resp["status_code"]
   msg = resp["msg"]
   context = {
        "request": request,
        "msg": msg,
        "status_code": status_code
    }
   return templates.TemplateResponse("partials/update-country-list.html", context)

@admin_router.get("/initialize-database", response_class=HTMLResponse)
async def initialize_database(request: Request):
    status_code = ""
    msg = ""
    context = {
        "request": request,
        "msg": msg,
        "status_code": status_code
    }
    return templates.TemplateResponse("init-db.html", context)

@admin_router.get("/init-db", response_class=HTMLResponse)
async def initialize_db(request: Request, settings: Settings = Depends(get_settings)):
   task = init_database.delay()
   
   resp = task.get()
  
   status_code = resp["status_code"]
   msg = resp["msg"]
   context = {
        "request": request,
        "msg": msg,
        "status_code": status_code
    }
   return templates.TemplateResponse("partials/init-db-status.html", context)

# Below is no longer used - Changed to a celery task
@admin_router.get("/update2", response_class=HTMLResponse)
async def update(request: Request, settings: Settings = Depends(get_settings)):
    url = settings.COUNTRYAPI + '?fields=' + settings.FIELDS
    
    #"https://restcountries.com/v3.1/all?fields=name,cca2,ccn3"

    resp = requests.get(url)
    changed = False

    if resp.status_code != 200:
        msg = "Error updating countries.  Cannot contact API"
    else:
        for country in resp.json():
            # See if the country is in the database
            db_country = session.query(Country).filter(Country.name==country['name']['official']).first()
            if db_country is None:
                changed = True
                # not in the database, add it
                ccn3 = 0 if country['ccn3'] == '' else country['ccn3']
                new_country = Country(name=country['name']['official'], cca2=country['cca2'],ccn3=ccn3)
                session.add(new_country)

        if changed:
            session.commit()
            msg = "Country database has been updated successfully."
        else:
            msg = "No updates were made."
        

    status_code = resp.status_code
    context = {
        "request": request,
        "msg": msg,
        "status_code": status_code
    }
    return templates.TemplateResponse("partials/update-country-list.html", context)

@admin_router.get("/", response_class=HTMLResponse)
async def default_view(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("status.html", context)

