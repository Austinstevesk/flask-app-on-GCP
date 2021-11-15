FROM python:3.8-alpine

MAINTAINER Stephen Karanja

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python", "wsgi.py"]