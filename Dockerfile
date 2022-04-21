FROM python:3.8.13-alpine3.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN  pip3 install -r requirements.txt

COPY . .

EXPOSE 5000:5000

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
