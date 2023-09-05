from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.crud_base import CRUDBase
from app.models.book import Book


class CRUDBook(CRUDBase):
    @staticmethod
    async def get_book_id_by_description(
        book_description: str, session: AsyncSession
    ) -> Optional[int]:
        db_book_id = await session.execute(
            select(Book.id).where(Book.description == book_description)
        )
        return db_book_id.scalars().first()

    async def search_books_by_title(
        self, title: str, session: AsyncSession
    ) -> Book:
        part = await session.execute(
            select(self.model).where(Book.title.like(f"%{title}%"))
        )
        part = part.scalars().first()
        return part


book_crud = CRUDBook(Book)
