Messenger implementation based on django, django-channels, vue js.

Requirements:
Python >= 3.9\
Redis server\
Docker >= 20.10.17

How to use (without docker):
1. Create Python virtual environment and activate it: `python -m venv venv`, windows: `venv\Scripts\activate`, linux: `source venv/bin/activate`
2. Install redis server and redis-cli, then run it.
3. Install all requirements by `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Run debug server `python manage.py runserver`
6. Change directory to frontend/
7. Run `npm install`
8. After dependencies installation run `npm run serve`

Docker usage:
1. Create .env file based on .env_example.
2. Use command `docker-compose -f docker-compose-dev.yaml up` to up docker-containers.
If you want to up docker in daemon use:
3. `docker-compose -f docker-compose-dev.yaml up -d` and `docker logs -f messenger_backend` or `docker logs -f messenger_frontend` to access logs.
