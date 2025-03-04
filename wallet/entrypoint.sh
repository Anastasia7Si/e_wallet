#!/bin/sh

sleep 10

python manage.py makemigrations

python manage.py migrate --no-input

python manage.py collectstatic --no-input

cp -r /app/collected_static/. /backend_static/static/

python /app/create_wallet.py

pytest

exec gunicorn wallet.wsgi:application --bind 0.0.0.0:8000

