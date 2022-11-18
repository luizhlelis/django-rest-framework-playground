# django-rest-framework-playground

🐍 Just playing a bit with `python` and `Django Rest Framework`.

## Pre-requisites

- [Python](https://www.python.org/downloads/)

## Running commands

To use virtual environment isolating packages dependencies locally:

```bash
python3 -m venv env
source env/bin/activate
```

To fire up the server type:

```bash
python manage.py runserver
```

To get all users:

```bash
curl -H 'Accept: application/json; indent=4' -u admin:admin123 http://127.0.0.1:8000/users/
```
