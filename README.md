# Pizza Restaurant API — Phase 4 Code Challenge

## Learning Goals

- Build a RESTful Flask API with models, validations, and routes
- Structure a backend application using the MVC pattern
- Seed and query a PostgreSQL database
- Test endpoints using Postman

---

## Setup

This challenge is organized with a standard MVC folder structure inside the `server` directory.

## Clone the repo
```console
https://github.com/Kabogo-Maverick/pizza-challenge.git 
```

## Installing dependencies and activating your virtual environment:

```console
$ pipenv install
$ pipenv shell
```


## Migrate


```console
$export FLASK_APP=server/app.py
$ flask db init
$ flask db migrate -m "Initial migration"
$ flask db upgrade
```

## run seed
from the root directory:

```console
python -m server.seed
````

## run the flask
from the root directory:

```console
export FLASK_APP=server.app
flask run
````
 
## viewing the postgresql table

```console
psql -U maverick -d pizza_db
```
view tables;

```console
\dt
