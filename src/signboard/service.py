from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.signboard.models import Signboard
from src.base.base_service import BaseService
from src.database import async_session_maker
from src.signboard.schemas import SSignboard


class SignboardService(BaseService):
    _MODEL = Signboard

    @classmethod
    async def get_signboard_with_item(cls, access_token: str):
        """
        SELECT * FROM signboard
        JOIN signboard_item ON signboard_item.signboard_id = signboard.id
        WHERE signboard.access_token = 'access_token'
        ORDER BY signboard_item.id

        :param access_token:
        :return:
        """
        async with async_session_maker() as session:
            query = (
                select(cls._MODEL)
                .options(selectinload(cls._MODEL.items))
                .where(cls._MODEL.access_token == access_token)
            )
            result = await session.execute(query)
            signboard = result.scalars().first()

            if not signboard:
                return None

            return SSignboard.from_orm(signboard)
