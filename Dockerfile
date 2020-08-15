FROM python:3.6-slim

WORKDIR /app
COPY requirements.txt .
COPY device_bind.sh .
RUN chmod +x device_bind.sh
RUN pip install -r requirements.txt