import os
import pathlib
import requests

from celery import Celery
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .models import Country
from .database import Session,engine
from .config import get_settings

from .init_db import init_db

#load_dotenv(".env")
settings = get_settings()
session = Session(bind=engine)

celery = Celery(__name__)
celery.conf.broker= settings.CELERY_BROKER_URL
celery.conf.backend = settings.CELERY_RESULT_BACKEND

@celery.task(name="initialize_database")
def init_database():
    init_db()
    
    context = {
        "msg": "Tables have been created.",
        "status_code": 201
    }
    return context

@celery.task(name="update_country_table")
def update_country_table():
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
        "msg": msg,
        "status_code": status_code
    }
    return context
