#!/bin/bash
cd "$(dirname "$0")"
[ -d venv ] || python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
(sleep 3; open http://127.0.0.1:8000/profile/) &
python manage.py runserver
