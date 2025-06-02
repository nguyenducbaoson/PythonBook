from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
import uuid

class Book(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    year: Optional[int] = None