FROM python:3.8

MAINTAINER Volodymyr Rekeda

WORKDIR /django-lab1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /django-lab1