FROM python:3.12

RUN pip install poetry

RUN pip install fastapi[standard]

COPY . .

RUN poetry install 

CMD ["fastapi", "run", "src/api.py", "--port", "80"]