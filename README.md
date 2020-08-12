## Django Async Pytest Teardown Problem Example

Start Postgres if you don't have it running locally:

```sh
docker run --rm --name django-postgres -p 5432:5432 -e POSTGRES_PASSWORD=password postgres
```

Setup and run the test:

```sh
$ pyenv local 3.8.2
$ pip install virtualenv virtualenvwrapper

$ mkvirtualenv test-app
$ poetry install

$ DJANGO_SETTINGS_MODULE=app.settings.base pytest tests/test_db.py
```

Result:

```
Error when trying to teardown test databases: OperationalError('database "test_postgres" is being accessed by other users\nDETAIL:  There is 1 other session using the database.\n')
```
