from fastapi import APIRouter, HTTPException

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserRead, UserCreate, UserUpdate
from constants import METHOD_NOT_ALLOWED

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@router.delete("/users/{id}", tags=["user"], deprecated=True)
def delete_user(user_id: str) -> None:
    """Нельзя удалять юзеров."""
    raise HTTPException(
        status_code=METHOD_NOT_ALLOWED, detail="Нельзя удалять пользователей!"
    )
