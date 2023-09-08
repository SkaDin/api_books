from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate


class UserRead(BaseUser[int]):
    """Схема просмотра юзера."""

    pass


class UserCreate(BaseUserCreate):
    """Схема создания юзера."""

    pass


class UserUpdate(BaseUserUpdate):
    """Схема редактирования юзера."""

    pass
