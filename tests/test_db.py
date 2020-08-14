import pytest
from django.db import transaction
from asgiref.sync import sync_to_async, async_to_sync
from app.django_models.person.models import Person
import decorator


def async_db_test(func):
    def inner(func, *args, **kwargs):
        return async_to_sync(func)(*args, **kwargs)

    return decorator.decorator(inner, func)


@pytest.fixture
async def create_person() -> Person:
    def inner():
        return Person.objects.create(name="hello world")

    return sync_to_async(inner, thread_sensitive=True)


@pytest.fixture
def count_persons() -> int:
    def inner():
        return Person.objects.count()

    return sync_to_async(inner, thread_sensitive=True)


@pytest.mark.django_db
@async_db_test
async def test_db(create_person, count_persons) -> None:
    await create_person()
    await Person.objects.async_create(name="hello there")
    assert await count_persons() == 2


@pytest.mark.django_db
@async_db_test
async def test_db_again(create_person, count_persons) -> None:
    await create_person()
    await Person.objects.async_create(name="hello there")
    assert await count_persons() == 2
