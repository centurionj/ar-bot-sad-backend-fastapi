FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ../src /app/src
COPY ../alembic /app/alembic
COPY ../alembic.ini /app/alembic.ini
COPY ../requirements.txt /app/requirements.txt
COPY ./deploy /app/deploy

EXPOSE 8000

RUN chmod +x ./deploy/run_server.sh

CMD ["./deploy/run_server.sh"]
