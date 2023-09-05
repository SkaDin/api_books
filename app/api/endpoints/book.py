from typing import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_duplicate,
    check_book_exists,
    obj_is_empty,
)
from app.core.db import get_async_session
from app.crud.book import book_crud
from app.models.book import Book
from app.schemas.book import BookCreate, BookDB, BookUpdate

router = APIRouter()


@router.post("/", response_model=BookDB, response_model_exclude_none=True)
async def create_books(
    book: BookCreate, session: AsyncSession = Depends(get_async_session)
) -> Book:
    await check_duplicate(book.description, session)
    new_book = await book_crud.create(book, session)
    return new_book


@router.patch(
    "/{book_id}",
    response_model=BookUpdate,
    response_model_exclude_none=True,
)
async def partially_update_book(
    book_id: int,
    obj_in: BookUpdate,
    session: AsyncSession = Depends(get_async_session),
) -> Book:
    book = await check_book_exists(book_id, session)
    book = await book_crud.update(book, obj_in, session)
    return book


@router.delete(
    "/{book_id}",
    response_model=BookDB,
    response_model_exclude_none=True,
)
async def remove_book(
    book_id: int, session: AsyncSession = Depends(get_async_session)
) -> Book:
    book = await check_book_exists(book_id, session)
    book = await book_crud.remove(book, session)
    return book


@router.get(
    "/",
    response_model=list[BookDB],
    response_model_exclude_none=True,
)
async def get_all_books(
    session: AsyncSession = Depends(get_async_session),
) -> Sequence[Book]:
    book_all = await book_crud.get_multi(session)
    return book_all


@router.get(
    "/get_by_title", response_model=BookDB, response_model_exclude_none=True
)
async def get_book_by_title(
    book_title: str, session: AsyncSession = Depends(get_async_session)
) -> Book:
    book = await book_crud.search_books_by_title(book_title, session)
    await obj_is_empty(book)
    return book
