from fastapi import APIRouter

from app.api.endpoints import book_router, user_router


main_router = APIRouter()
main_router.include_router(book_router, tags=["Books"], prefix="/books")
main_router.include_router(user_router)
