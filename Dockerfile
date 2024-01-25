FROM python:3.10.6-slim-bullseye

RUN apt-get update -y \
    && apt-get install -y libpq-dev build-essential \
    && apt-get install -y --no-install-recommends gunicorn \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /src

COPY . /src

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]
