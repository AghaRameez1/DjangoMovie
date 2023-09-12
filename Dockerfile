FROM ubuntu:latest
RUN apt update
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update \
    && apt -y upgrade \
    && apt install -y python3 \
    && apt install -y python3-pip \
    && apt install -y poppler-utils \
    && apt install -y libsm6 libxext6 libxrender-dev libpq-dev python3-dev gcc musl-dev libpq-dev software-properties-common
RUN apt install -y postgresql
USER postgres
RUN    /etc/init.d/postgresql start &&\
    psql --command "ALTER USER postgres WITH SUPERUSER PASSWORD '1234';"
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/14/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/14/main/postgresql.conf
USER root
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache --upgrade pip setuptools
RUN pip install psycopg2
WORKDIR /project


COPY . /project/


RUN pip install -r requirements.txt
RUN python3 manage.py migrate

ENV DJANGO_SUPERUSER_EMAIL=agharameez1990@gmail.com
ENV DJANGO_SUPERUSER_USERNAME=agharameez
ENV DJANGO_SUPERUSER_PASSWORD=1234

RUN python3 manage.py createsuperuser --noinput
EXPOSE 8000
CMD [ "python3", "manage.py" ,"runserver","0.0.0.0:8000" ]