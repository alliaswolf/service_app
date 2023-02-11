FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt

WORKDIR /service
EXPOSE 8000

RUN pip3 install -U pip
RUN pip3 install -r /temp/requirements.txt

COPY service /service

RUN adduser --disabled-password service-user

USER service-user
