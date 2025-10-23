FROM python:3.11-slim

WORKDIR /app

COPY app.py test_app.py ./

RUN pip install psycopg2-binary pytest

CMD ["pytest", "test_app.py"]
