FROM python:3.11-slim

WORKDIR /app

COPY app.py test_app.py ./

RUN pip install psycopg2-binary pytest allure-pytest

CMD ["pytest", "--alluredir=allure-results", "test_app.py"]
