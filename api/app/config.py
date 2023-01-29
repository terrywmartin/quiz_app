from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DB_HOST: str
    DB_NAME: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_USER: str

    COUNTRYAPI: str
    FIELDS: str
    FLAGAPI: str
    FILETYPE: str
    
    APP_NAME: str

    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    class Config:
        env_file = "../.env"

@lru_cache()
def get_settings():
    return Settings()