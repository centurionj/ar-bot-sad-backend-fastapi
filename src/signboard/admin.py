from sqladmin import ModelView
from markupsafe import Markup

from src.signboard.models import Signboard, SignboardItem


class SignboardItemAdmin(ModelView, model=SignboardItem):
    column_list = [c for c in SignboardItem.__table__.columns.keys()]
    name = 'Файл вывески'
    name_plural = 'Файлы вывесок'
    icon = "fa-solid fa-user"


class SignboardAdmin(ModelView, model=Signboard):
    column_list = [c for c in Signboard.__table__.columns.keys()] + ['unique_link', Signboard.items]
    name = 'Вывеска'
    name_plural = 'Вывески'
    icon = "fa-solid fa-sign"

    @staticmethod
    def __unique_link_formatter(signboard_instance: Signboard, _) -> Markup:
        return Markup(
            f'<a href="{signboard_instance.unique_link}" target="_blank">{signboard_instance.unique_link}</a>')

    column_formatters = {
        'unique_link': __unique_link_formatter,
    }

    form_widget_args = {
        'unique_link': {'readonly': True},
    }
