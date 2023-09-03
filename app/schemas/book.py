import datetime
import re
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, field_validator, PastDate


class BookCreate(BaseModel):
    """Schemas fro Book."""

    title: str = Field(..., max_length=30, title="Название книги")
    image: Optional[str] = None
    description: str
    author: str = Field(..., max_length=64, title="Автор книги")
    date_publication: date = None
    price: Optional[int] = None

    class Config:
        str_min_length = 2

    @field_validator("title", "description", "author")
    @classmethod
    def non_numeric_mixed_alphabet(cls, value: str) -> str:
        if re.search("[а-я]", value, re.IGNORECASE) and re.search(
            "[a-z]", value, re.IGNORECASE
        ):
            raise ValueError("Нельзя смешивать кириллицу и латиницу")
        return value
