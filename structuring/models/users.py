from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "kazi@gmail.com",
                "password": "strong!!!",
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
