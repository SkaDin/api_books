from fastapi import FastAPI

from app.api.endpoints import router as router_endpoints
from app.core.config import settings


app = FastAPI(title=settings.app_title, docs_url='/swagger')

app.include_router(router_endpoints)
