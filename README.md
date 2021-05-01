## Basic and minimal example to start working with JWT in Django Rest Framework.


Views:

- POST - <your_django_host>/api/token/ | To obtain the initial demo (needs the username and password in form)
- POST - <your_django_host>/api/token/refresh/ | To refresh your token (needs your obtained refresh token)
- GET - <your_django_host>/demo | For testing the demo JWT Experiment. (need the obtained token in bearer auth)

**Don't forget to change your SECRET_KEY value in django settings file if are planning to use this code as a boilerplate in some project. It is used for sign JWTs.**

Mario Llobet.
https://www.buymeacoffee.com/awantagrde