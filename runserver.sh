#!/bin/sh
clear;

find . -name "*.pyc" | xargs rm && \

rm -rf db.sqlite3 && \

python manage.py makemigrations && \
python manage.py migrate && \

DJANGO_ADMIN="admin"
DJANGO_USER="user"
DJANGO_MAIL="test@test.com"
DJANGO_PASSWORD="testpassword123"

echo "from django.contrib.auth.models import User; \
      User.objects.create_superuser('$DJANGO_ADMIN', '$DJANGO_MAIL', '$DJANGO_PASSWORD'); \
      User.objects.create_user('$DJANGO_USER', '$DJANGO_MAIL', '$DJANGO_PASSWORD')" \
      | python manage.py shell

echo "Adding initial data"
python manage.py initial_data

python manage.py runserver
