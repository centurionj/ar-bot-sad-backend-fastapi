from sqlalchemy import select, insert, delete, update

from src.database import async_session_maker


class BaseService:
    """Базовый сервис для CRUD"""

    _MODEL = None

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls._MODEL.__table__.columns).order_by(cls._MODEL.id)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def get_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(cls._MODEL.__table__.columns).filter_by(id=id)
            result = await session.execute(query)
            return result.mappings().first()

    @classmethod
    async def get_by_filter(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls._MODEL.__table__.columns).filter_by(**filter)
            result = await session.execute(query)
            return result.mappings().first()

    @classmethod
    async def delete_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(cls._MODEL).filter_by(id=id)
            result = await session.execute(query)
            obj_to_delete = result.scalar_one_or_none()
            if obj_to_delete is not None:
                await session.delete(obj_to_delete)
                await session.commit()
            return id

    @classmethod
    async def create(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls._MODEL).values(**data)
            await session.execute(query)
            await session.commit()
            return data

    @classmethod
    async def update_by_id(cls, id: int, **data):
        async with async_session_maker() as session:
            query = update(cls._MODEL.__table__.columns).where(cls._MODEL.id == id).values(**data)
            await session.execute(query)
            await session.commit()
            return {
                'id': id,
                **data,
            }
