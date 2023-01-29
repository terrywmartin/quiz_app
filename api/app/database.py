from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#from .init_db import init_db
from app.config import get_settings
#from .config import get_settings

settings = get_settings()

db_string = 'postgresql://' + settings.DB_USER + ':' + settings.DB_PASSWORD + '@' + settings.DB_HOST + ':' + str(settings.DB_PORT) + '/' + settings.DB_NAME
engine = create_engine(db_string,  #'postgresql://postgres:1234567@10.0.0.144:5434/quiz_app',
    echo = True
)

# Create database if it does not exist.
#if not database_exists(engine.url):
#    create_database(engine.url)
    

Base = declarative_base()

Base.metadata.create_all(engine)

Session = sessionmaker()
