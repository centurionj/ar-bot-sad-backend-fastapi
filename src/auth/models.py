from sqlalchemy import Column, Integer, String

from src.database import Base

class User(Base):
    """Модель пользователя"""

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False, comment='Email')
    password = Column(String(255), nullable=False, comment='Пароль')

    def __str__(self):
        return self.email
