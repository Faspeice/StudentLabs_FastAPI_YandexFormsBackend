FROM python:latest

WORKDIR /TTSLABFORMS

ENV PYTHONDOMTWRITENBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN  pip install --no-cache-dir --upgrade -r requirements.txt

COPY ../ app