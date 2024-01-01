FROM python:3.10-alpine

WORKDIR /usr/src/app

EXPOSE 8000

COPY requirements.txt ./

COPY . .

RUN pip install --no-cache-dir -r requirements.txt