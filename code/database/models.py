from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from bson import ObjectId
from uuid import uuid4

class Book(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid4()))
    title: str
    author: str
    description: Optional[str] = None
    year: Optional[int] = None


class User(BaseModel):
    username: str
    email: Optional[EmailStr] = None 
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None 


class UserInDB(User):
    hashed_password: str

class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    disabled: Optional[bool] = None