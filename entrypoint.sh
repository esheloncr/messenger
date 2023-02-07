#!/bin/bash

python manage.py migrate
python manage.py compilemessages --ignore=venv
python manage.py runserver $HOST:$PORT