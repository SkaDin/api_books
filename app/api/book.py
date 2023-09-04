from http import HTTPStatus
from typing import Sequence

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.book import book_crud
from app.models.book import Book
from app.schemas.book import BookBase, BookCreate, BookDB, BookUpdate

router = APIRouter(tags=["Books"], prefix="/books")


@router.post("/", response_model=BookBase, response_model_exclude_none=True)
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


async def check_duplicate(
    book_description: str, session: AsyncSession
) -> None:
    book_id = await book_crud.get_book_id_by_description(
        book_description, session
    )
    if book_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail="Такое описание книги уже есть!",
        )


async def check_book_exists(book_id: int, session: AsyncSession) -> Book:
    book = await book_crud.get(
        book_id,
        session,
    )
    if book is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Книга не найдена!"
        )
    return book


@router.get(
    "/get_by_name", response_model=BookBase, response_model_exclude_none=True
)
async def get_book_by_title(
    book_title: str, session: AsyncSession = Depends(get_async_session)
) -> Book:
    book = await book_crud.search_books_by_title(book_title, session)
    if book is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Такой книги нет"
        )
    return book
