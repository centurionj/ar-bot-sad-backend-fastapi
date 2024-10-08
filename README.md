# Серверная часть AR приложения для компании “Бот Сад”

## Стэк

- Python 3.10
- FastAPI
- PostgreSQL
- Docker
- Docker-compose
- nginx
- Uvicorn
- bash

## Описание проекта

Программное обеспечение с элементами виртуальной реальности (VR), позволяющее клиентам
визуализировать вывеску на своем объекте.
Пользователь получает макет вывески и может с помощью мобильного устройства
навести камеру на объект, чтобы перенести макет вывески на него,
выбрав подходящий масштаб и место.

## Инструкция по развертыванию

Создать .env из .env.example

#### Параметры приложения

| Ключ                | Значение                     | Примечания                                                      |
|---------------------|------------------------------|-----------------------------------------------------------------|
| `DEBUG`             | Режим запуска                | *                                                               |
| `ALLOWED_ORIGINS`   | Настройка для CORS           | *                                                               |
| `POSTGRES_DB`       | Имя базы данных              | Должен быть отличный от postgres                                |
| `POSTGRES_USER`     | Имя пользователя базы данных | Должен быть отличный от postgres                                |
| `POSTGRES_PASSWORD` | Пароль к базе данных         | Должен быть отличный от postgres                                |
| `POSTGRES_HOST`     | Хост базы данных             | Если запуск через докер то ставим postgres, ручками - localhost |
| `POSTGRES_PORT`     | Порт базы данных             | По умолчанию 5432                                               |
| `HASH_KEY`          | Ключ для хеширования         | *                                                               |
| `HASH_ALGORITHM`    | Алгоритм хеширования         | По умолчанию HS256                                              |
| `BACK_DOMAIN`       | Домен серверной части        | *                                                               |
| `FRONT_DOMAIN`      | Домен фронта                 | *                                                               |
| `KINZA_SITE`        | Сайт kinza                   | Указывается в футере админке                                    |

### Запуск через докер

1. В корне проекта

```shell
docker-compose up --build
```

### Запуск для разработки

1. В корне проекта

```shell
docker-compose up db
```

2. Выполнить миграции

```shell
alembic upgrade head
```

4. Запустить проект

```shell
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload
```

### Документация к api (SWAGGER)

http://localhost:8000/api/v1/docs/ или http://localhost/api/v1/docs/