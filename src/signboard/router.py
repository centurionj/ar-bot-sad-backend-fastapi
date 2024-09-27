from fastapi import APIRouter, HTTPException, status

from src.signboard.service import SignboardService
from src.signboard.schemas import SSignboard

router = APIRouter()


@router.get("/{access_token}", response_model=SSignboard)
async def get_signboard(access_token: str):
    signboard_with_items = await SignboardService().get_signboard_with_item(access_token=access_token)

    if not signboard_with_items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return signboard_with_items
