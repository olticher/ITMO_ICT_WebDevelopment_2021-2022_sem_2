FROM python:3.8.12

RUN apt-get update && apt-get upgrade -y && apt-get autoclean

RUN mkdir /project
COPY . /project/
WORKDIR /project

RUN pip install -r requirements.txt

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000