## Basic and minimal example to start working with JWT in Django Rest Framework.


Views:

- POST - <your_django_host>/api/token/ | To obtain the initial demo (needs the username and password in form)
- POST - <your_django_host>/api/token/refresh/ | To refresh your token (needs your obtained refresh token)
- GET - <your_django_host>/demo | For testing the demo JWT Experiment. (need the obtained token in bearer auth)


https://www.buymeacoffee.com/awantagrde