from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ContentCreate(BaseModel):
    title: str
    body: str
    tags: List[str] = []
    author: str
    date: Optional[datetime]
    template: str = "content.html"

class ContentOut(ContentCreate):
    id: str  # MongoDB ObjectId as string
