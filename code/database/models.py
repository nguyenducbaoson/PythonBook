from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4


class Book(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    author: str
    description: Optional[str] = None
    year: Optional[int] = None