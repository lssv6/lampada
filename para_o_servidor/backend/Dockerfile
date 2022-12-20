FROM python:3-alpine AS base

WORKDIR /opt/websocket

COPY servidor.py .

RUN pip install websockets

ENTRYPOINT ["python", "servidor.py"]
