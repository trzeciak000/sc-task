FROM python:3.8-slim-buster

COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app/ /app
WORKDIR /app

ENTRYPOINT ["python", "-m", "app.py"]
