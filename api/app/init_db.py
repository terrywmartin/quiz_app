from .database import engine, Base
from .models import Question, Quiz, User, Country, Settings, HighScores

def init_db():
    Base.metadata.create_all(bind=engine)