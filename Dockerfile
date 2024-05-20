FROM python:latest

WORKDIR /src
ENV PYTHONDONTWRITENBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry
RUN poetry config virtualenvs.create false
ADD pyproject.toml .
RUN poetry install
COPY . .
