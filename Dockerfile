FROM python:3.10.6-slim-bullseye

RUN apt-get update -y

RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r requirements.txt

WORKDIR /src

COPY . /src

EXPOSE 8000
