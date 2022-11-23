# django-rest-framework-playground

🐍 Just playing a bit with `python` and `Django Rest Framework`.

## Pre-requisites

- [Python](https://www.python.org/downloads/)

- [Poetry](https://python-poetry.org/docs/) (if you want to run the API locally)

- [Docker](https://www.docker.com/products/docker-desktop/) (if you want to run the API in containers)

## Running commands (poetry and virtual environment)

To up the containerized database:

```bash
docker-compose up db
```

To activate this project's virtualenv:

```bash
poetry shell
```

To create a new migration file:

```bash
python3 manage.py makemigrations
```

To apply the migrations:

```bash
python3 manage.py migrate
```

To create a superuser on django admin:

```bash
python3 manage.py createsuperuser
```

To fire up the `API`, type:

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

## Running commands (docker)
