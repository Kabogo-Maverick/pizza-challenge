# Pizza Restaurant API — Phase 4 Code Challenge

## Learning Goals

- Build a RESTful Flask API with models, validations, and routes
- Structure a backend application using the MVC pattern
- Seed and query a PostgreSQL database
- Test endpoints using Postman

---

## Introduction

It’s pizza time! In this challenge, you'll implement a fully-functional REST API for a pizza restaurant using Flask and PostgreSQL.

You’ll define models and relationships, apply validations, build route controllers, seed the database, and test it all using Postman.

---

## Setup

This challenge is organized with a standard MVC folder structure inside the `server` directory.

Begin by installing dependencies and activating your virtual environment:

```console
$ pipenv install
$ pipenv shell
```


## Migrate


```console
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
 


