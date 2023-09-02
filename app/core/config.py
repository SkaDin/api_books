import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    app_title: str = os.getenv('APP_TITLE')
    db_url: str = os.getenv('DATABASE_URL')


settings = Settings()
