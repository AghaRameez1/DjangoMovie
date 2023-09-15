#!/bin/sh

python manage.py flush --no-input
python manage.py migrate

export DJANGO_SUPERUSER_EMAIL=agharameez1990@gmail.com
export DJANGO_SUPERUSER_USERNAME=agharameez
export DJANGO_SUPERUSER_PASSWORD=1234
python manage.py createsuperuser --noinput

exec "$@"