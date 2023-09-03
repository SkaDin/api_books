from typing import Optional

from sqlalchemy import select

from app.core.db import AsyncSessionLocal
from app.models.book import Book
from app.schemas.book import BookCreate


async def create_book(new_book: BookCreate) -> Book:
    new_book_data = new_book.model_dump()
    db_obj = Book(**new_book_data)
    async with AsyncSessionLocal() as session:
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
    return db_obj


async def get_book_id_by_description(book_description: str) -> Optional[int]:
    async with AsyncSessionLocal() as session:
        db_book_id = await session.execute(
            select(Book.id).where(Book.description == book_description)
        )
        return db_book_id.scalars().first()
