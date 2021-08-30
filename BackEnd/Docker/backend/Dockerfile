FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /backend-code

COPY requirements.txt /backend-code/

RUN pip install -r requirements.txt

COPY . /backend-code/