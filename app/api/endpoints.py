from http import HTTPStatus
from fastapi import APIRouter, HTTPException

from app.crud.book import create_book, get_book_id_by_description
from app.schemas.book import BookCreate, BookDB

router = APIRouter()


@router.post(
    "/book_create/",
    response_model=BookDB,
)
async def create_books(
    book: BookCreate,
):
    book_id = await get_book_id_by_description(book.description)
    if book_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail='Такое описание книги уже есть!'
        )
    new_book = await create_book(book)
    return new_book
