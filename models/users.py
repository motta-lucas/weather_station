from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List

from beanie import Document, Link

from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "sensors@iot.com",
                "username": "strong!!!",
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": [
                {
                    "email": "sensors@iot.com",
                    "password": "strong!!!",
                }
            ]
        }
    )


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
