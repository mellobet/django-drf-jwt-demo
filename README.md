# Django DRF JWT Demo

Basic and minimal example to start working with JWT in Django Rest Framework.

## Installation

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser --username <a_django_user>
./manage.py runserver
```

## Views:

- POST - <your_django_host>[\:<port>]/api/token/ | To obtain the initial tokens, both access and refresh. (Needs the username and password in the request form)

```bash
curl -XPOST localhost:8000/api/token/ -F 'username=<a_django_username>' -F 'password=<a_django_pass>'
```

- POST - <your_django_host>[\:<port>]/api/token/refresh/ | To refresh your token. (Needs the previously obtained refresh token)

```bash
curl -XPOST localhost:8000/api/token/refresh/ -F 'refresh=<obtained_refresh_token>'
```

- GET - <your_django_host>[\:<port>]/demo | For testing the JWT demo. (Needs the obtained token string in bearer auth)

```bash
curl localhost:8000/demo/ -H 'Authorization: Bearer <obtained_access_token>'
```


**Don't forget to change the SECRET_KEY value in django settings file if are planning to use this code as the boilerplate in some project. This key is used for sign the JWTs by default.**

https://www.buymeacoffee.com/awantagrde
