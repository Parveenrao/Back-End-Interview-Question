from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class Role(str, Enum):
    user = "USER"
    admin = "ADMIN"

class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=30)
    age: int = Field(ge=18, le=100)
    email: EmailStr
    phone: str = Field(pattern=r"^[0-9]{10}$")
    role: Role

@app.post("/users")
def create_user(user: UserCreate):
    return {"message": "User created", "user": user}


# custom validation


from pydantic import BaseModel, field_validator

class User(BaseModel):
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("Password too short")

        if not any(c.isupper() for c in value):
            raise ValueError("Must contain uppercase letter")

        return value