# pull the official base image
FROM python:3.9

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
# COPY ./unixcmdb /usr/src/app

EXPOSE 8000
WORKDIR /usr/src/app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]