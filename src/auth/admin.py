from sqladmin import ModelView

from src.auth.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]
    column_details_exclude_list = [User.password]
    name = 'Пользователь'
    name_plural = 'Пользователи'
    icon = "fa-solid fa-user"
