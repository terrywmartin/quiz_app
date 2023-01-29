from .database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__='user'
    id=Column(Integer, primary_key=True)
    username=Column(String(25),unique = True)
    email=Column(String(100),unique = True)
    password=Column(Text,nullable=True)
    is_active=Column(Boolean,default=True)

    def __repr__(self):
        return f"<User {self.username}>"

class Quiz(Base):
    __tablename__='quiz'

    id=Column(Integer, primary_key=True)
    answer=Column(Text)
    questions=relationship('Question', back_populates='quiz')

class Question(Base):
    __tablename__='question'

    id=Column(Integer, primary_key=True)
    quiz_id=Column(Integer,ForeignKey('quiz.id'))
    name=Column(String(255))
    abrv=Column(String[2])
    quiz=relationship('Quiz',back_populates='questions')
    

class Settings(Base):
    __tablename__='settings'

    id=Column(Integer,primary_key=True)
    number_of_questions=Column(Integer,default=10)
    number_of_choices=Column(Integer,default=5)

class HighScores(Base):
    __tablename__='high_scores'

    id=Column(Integer, primary_key=True)
    name=Column(String(255))
    score=Column(Integer)
    num_of_games=Column(Integer)

class Country(Base):
    __tablename__='countries'

    id=Column(Integer, primary_key=True)
    name=Column(String(255),unique=True)
    cca2=Column(String(2),unique = True)
    ccn3=Column(Integer,unique=True)

