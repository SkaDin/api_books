import re
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class BookBase(BaseModel):
    title: str = Field(..., max_length=128, title="Название книги")
    image: Optional[str] = None
    description: str
    genre: str
    author: str = Field(..., max_length=128, title="Автор книги")
    date_publication: date = None
    url_download: Optional[str] = None

    class Config:
        str_min_length = 2
        from_attributes = True

    @classmethod
    @field_validator("title", "description", "author")
    def non_numeric_mixed_alphabet(cls, value: str) -> str:
        if re.search("[а-я]", value, re.IGNORECASE) and re.search(
            "[a-z]", value, re.IGNORECASE
        ):
            raise ValueError("Нельзя смешивать кириллицу и латиницу")
        return value


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    @classmethod
    @field_validator("title", "description", "author")
    def check_name_is_not_empty(cls, value: str) -> str:
        if value is None:
            raise ValueError(
                "Название, описание или автор не должны быть пустыми"
            )
        return value


class BookDB(BookBase):
    id: int
