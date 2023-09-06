from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.book import book_crud
from app.models.book import Book
from constants import NOT_FOUND, UNPROCESSABLE_ENTITY


async def check_book_exists(book_id: int, session: AsyncSession) -> Book:
    book = await book_crud.get(
        book_id,
        session,
    )
    await obj_is_empty(book)
    return book


async def obj_is_empty(obj):
    if obj is None:
        raise HTTPException(status_code=NOT_FOUND, detail="Такой книги нет")


async def check_duplicate(
    book_description: str, session: AsyncSession
) -> None:
    book_id = await book_crud.get_book_id_by_description(
        book_description, session
    )
    if book_id is not None:
        raise HTTPException(
            status_code=UNPROCESSABLE_ENTITY,
            detail="Такое описание книги уже есть!",
        )
