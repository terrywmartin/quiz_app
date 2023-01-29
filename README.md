# quiz_app

I wanted to learn FastAPI and got this idea while searching for tutorials on YouTube.

This uses FastAPI, Redis, Celery, Flower, Postgreslq and Docker.


A .env file is used for the environmental variables.  The file should look something like this.

`
DB_HOST=db
DB_NAME=quiz_app
DB_PASSWORD=1234567
DB_PORT=5432
DB_USER=postgres

PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

COUNTRYAPI=https://restcountries.com/v3.1/all
FIELDS=name,cca2,ccn3
FLAGAPI=https://countryflagsapi.com/
FILETYPE=png

APP_NAME=Quiz App
`

To start the app, you'll need docker installed.  Then run `docker compose build`.  If this is successful, run `docker compose up` to start everything and run the app. Make sure you're in the API folder.

I haven't automated creating the database tables because I'm learning how to use Celery so I decided to write a couple of functions to create the tables and load the country data.  Use the following urls to initialize and populate the tables.

`http://127.0.0.1:8000/admin/initialize-database`
`http://127.0.0.1:8000/admin/update-country`

This is very much a work in progress as I'm learning FastAPI, Docker and Celery.
