from fastapi import APIRouter

from src.auth.router import router as auth_router
from src.signboard.router import router as signboard_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(signboard_router, prefix="/signboard", tags=["signboard"])
