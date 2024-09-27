import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from src.config import settings
from src.database import engine
from src.auth.admin import UserAdmin
from src.auth.utils import authentication_backend
from src.api.v1.api import api_router
from src.signboard.admin import SignboardAdmin, SignboardItemAdmin

app = FastAPI(
    title="Бот Сад",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    debug=settings.DEBUG
)

app.mount("/media", StaticFiles(directory=settings.MEDIA_DIR), name="media")

app.include_router(api_router, prefix=settings.API_V1_STR)

admin = Admin(app, engine, authentication_backend=authentication_backend, title='Бот Сад AR/VR')
admin.add_view(SignboardAdmin)
admin.add_view(SignboardItemAdmin)
admin.add_view(UserAdmin)
