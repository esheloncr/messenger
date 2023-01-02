Messenger implementation based on django, django-channels, vue js.

Requirements:
Python >= 3.9\
Redis server

How to use:
1. Create Python virtual environment and activate it: `python -m venv venv`, windows: `venv\Scripts\activate`, linux: `source venv/bin/activate`
2. Install redis server and redis-cli, then run it.
3. Install all requirements by `pip install -r requirements.txt`
4. Apply migrations: python manage.py migrate
5. Run debug server `python manage.py runserver`