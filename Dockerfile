FROM python:latest

WORKDIR /TTSLABFORMS
ENV PYTHONDONTWRITENBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry
RUN poetry config virtualenvs.create false
ADD pyproject.toml .
RUN poetry install --no-root --no-interaction --no-ansi
EXPOSE 8000
COPY . /TTSLABFORMS
