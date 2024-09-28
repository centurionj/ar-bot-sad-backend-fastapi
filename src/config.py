import os

from pydantic import BaseSettings, root_validator


class Settings(BaseSettings):
    DEBUG: bool = True
    ALLOWED_ORIGINS: str = 'http://localhost, http://localhost:8000, http://localhost:3000, http://localhost:5137'
    API_V1_STR: str = "/api/v1"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    HASH_KEY: str
    HASH_ALGORITHM: str

    FRONT_DOMAIN: str

    BASE_DIR: str = os.path.abspath('./src')
    STATIC_DIR: str = os.path.join(BASE_DIR, 'static')
    MEDIA_DIR: str = os.path.join(BASE_DIR, 'media')

    @root_validator
    def get_database_dsn(cls, value):
        value['DATABASE_DSN'] = (
            f'postgresql+asyncpg://{value["POSTGRES_USER"]}:'
            f'{value["POSTGRES_PASSWORD"]}@{value["POSTGRES_HOST"]}:'
            f'{value["POSTGRES_PORT"]}/{value["POSTGRES_DB"]}'
        )
        return value

    class Config:
        env_file = '.env'


settings = Settings()
