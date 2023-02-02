FROM python:3.10

WORKDIR /app

ADD requirements.txt requirements.txt 

RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

ADD . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]