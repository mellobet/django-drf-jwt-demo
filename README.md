## Basic and minimal example to start working with JWT in Django Rest Framework.


Views:

- POST - <your_django_host>/api/token/ | To obtain the initial token. (Needs the username and password in the request form)
- POST - <your_django_host>/api/token/refresh/ | To refresh your token. (Needs the previously obtained refresh token)
- GET - <your_django_host>/demo | For testing the JWT demo. (Needs the obtained token string in bearer auth)

**Don't forget to change the SECRET_KEY value in django settings file if are planning to use this code as the boilerplate in some project. This key is used for sign the JWTs by default.**

Mario Llobet.
https://www.buymeacoffee.com/awantagrde