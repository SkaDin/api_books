import re

from typing import Union, Optional

from pydantic import BaseModel, Field, field_validator


class Person(BaseModel):
    """Схема пользователя."""
    name: str = Field(
        ..., max_length=20,
        title='Полное имя', description='Можно вводить в любом регистре'
    )
    surname: Union[str, list[str]] = Field(..., max_length=50)
    email: str = Field(..., max_length=64)
    age: Optional[int] = Field(None)
    is_staff: bool = Field(False, alias='is-staff')

    class Config:
        title = 'Класс для приветствия'
        str_min_length = 2
        json_schema_extra = {
            'example': {
                'name': 'Denisa',
                'surname': 'Gopher',
                'email' :'gas.killa@example.com',
                'age': 26,
            }
        }

    @field_validator('name', 'surname')
    @classmethod
    def check_name_surname(cls, value: str) -> str:
        if value.isnumeric():
            raise ValueError('Имя или фамилия не может быть числом')
        if (re.search('[а-я]', value, re.IGNORECASE)
                and re.search('[a-z]', value, re.IGNORECASE)):
            raise ValueError(
                'Нельзя смешивать кириллицу и латиницу'
            )
        return value

    @field_validator('email')
    @classmethod
    def check_email(cls, value: str) -> str:
        regular_email: str = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(regular_email, value):
            raise ValueError('Email not valid')
        return value
