from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "kazi@gmail.com",
                "password": "strong!!!",
                "events": []
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "kazi@gmail.com",
                "password": "strong!!!",
            }
        }
