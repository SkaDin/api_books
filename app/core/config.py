import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv
from pydantic import EmailStr

load_dotenv()


@dataclass
class Settings:
    app_title: str = os.getenv("APP_TITLE")
    db_url: str = os.getenv("DATABASE_URL")
    secret: str = os.getenv("SECRET")
    first_superuser_email: Optional[EmailStr] = os.getenv(
        "FIRST_SUPERUSER_EMAIL"
    )
    first_superuser_password: Optional[str] = os.getenv(
        "FIRST_SUPERUSER_PASSWORD"
    )


settings = Settings()
