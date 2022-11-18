# django-rest-framework-playground

🐍 Just playing a bit with `python` and `Django Rest Framework`.

## Pre-requisites

- [Python](https://www.python.org/downloads/)

## Running commands

To install dependencies, run:

```bash
pipenv install
```

To activate this project's virtualenv:

```bash
pipenv shell
```

To fire up the `API` type:

```bash
python3 manage.py runserver --noreload
```

To get all users type the following in your terminal:

```bash
curl -H 'Accept: application/json; indent=4' -u admin:admin123 http://127.0.0.1:8000/users/
```

To leave your virtual environment:

```bash
exit
```
