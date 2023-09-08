import csv

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.models import Book


def load_test_data(session: AsyncSession = Depends(get_async_session)):
    with open("my_book_database.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data = Book(**row)
            session.add(data)
            session.commit()
