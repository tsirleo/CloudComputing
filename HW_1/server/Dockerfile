FROM python:3.10-slim
LABEL authors="tsirleo"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install poetry

RUN python -m venv /venv

COPY server/pyproject.toml server/poetry.lock /app/

RUN . /venv/bin/activate && poetry install --no-root --no-directory

COPY server/ /app/server/

EXPOSE 12345

WORKDIR /app/server

CMD ["./docker-entrypoint.sh"]
