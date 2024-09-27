from src.base.base_service import BaseService
from src.auth.models import User


class AuthService(BaseService):
    _MODEL = User
