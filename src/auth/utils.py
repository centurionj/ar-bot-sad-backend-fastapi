from datetime import datetime, timedelta

from passlib.context import CryptContext
from pydantic import EmailStr
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from jose import jwt

from src.config import settings
from src.auth.service import AuthService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(email: EmailStr, password: str):
    existing_user = await AuthService.get_by_filter(email=email)
    if not (existing_user and verify_password(password, existing_user.password)):
        return None
    return existing_user


async def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.HASH_KEY, settings.HASH_ALGORITHM,
    )
    return encoded_jwt


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]

        user = await authenticate_user(email, password)

        if user:
            access_token = await create_access_token({'sub': str(user.id)})

            request.session.update({"access_token": access_token})

            return True

        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("access_token")

        if not token:
            return False

        return True


authentication_backend = AdminAuth(secret_key="...")
