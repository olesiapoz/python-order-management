FROM python:3-alpine

MAINTAINER olesiapoz

COPY app /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]