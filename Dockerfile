FROM python:3.7.6-stretch

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
