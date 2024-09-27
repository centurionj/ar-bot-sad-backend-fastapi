import uuid
import os
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base
from src.config import settings

storage_path = os.path.join(settings.MEDIA_DIR, 'signboard')
os.makedirs(storage_path, exist_ok=True)


class Signboard(Base):
    """Модель Вывески"""

    __tablename__ = 'signboard'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=True)
    access_token = Column(String, default=lambda: uuid.uuid4().hex[:20], nullable=False, comment='Уникальный номер')

    items = relationship("SignboardItem", back_populates="signboard", cascade='save-update, merge, delete',
                         passive_deletes=True, )

    @property
    def unique_link(self) -> str:
        return f"{settings.FRONT_DOMAIN}/{self.access_token}"

    def __str__(self):
        return f'{self.title}'


class SignboardItem(Base):
    """Модель элемента вывески"""

    __tablename__ = 'signboard_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=True)
    signboard_id = Column(ForeignKey('signboard.id', ondelete='CASCADE'), nullable=False)
    file = Column(FileType(storage=FileSystemStorage(path=storage_path)), comment='Файл вывески')
    height = Column(Integer, nullable=False, comment='Высота в мм')
    width = Column(Integer, nullable=False, comment='Ширина в мм')

    signboard = relationship("Signboard", back_populates="items")

    def __str__(self):
        return f'{self.title}'
