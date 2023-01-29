from pydantic import BaseModel
from typing import List, Optional

class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_active:bool

    class Config:
        orm_mode=True
        schema_extra={
            'example': {
                "username": "Test User",
                "email": "testuser@mail.com",
                "password": "password",
                "is_active": True
            }
        }

class QuestionModel(BaseModel):
    id:Optional[int]
    quiz_id:Optional[int]
    name:str
    abrv:str

    class Config:
        orm_mode=True
        schema_extra={
            'example': {
                "name": "United States of America",
                "abrv": "US"
            }
        }

class QuizModel(BaseModel):
    id:Optional[int]
    answer:str
    questions:List[QuestionModel]

    class Config:
        orm_mode=True
        schema_extra={
            'example': {
                "answer": "US",
                "questions": [
                    {
                        "name":  "United States of America",
                        "abrv": "US"
                    },
                    {
                        "name":  "Canada",
                        "abrv": "CA"
                    }
                ]
            }
        }
