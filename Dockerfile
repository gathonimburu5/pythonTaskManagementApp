FROM python:3.11-slim

WORKDIR /task

COPY requirements.txt  requirements.txt

RUN pip install -r requirements.txt

COPY . .