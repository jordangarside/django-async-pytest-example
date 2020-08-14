import pytest
from asyncio import create_task
from asgiref.sync import sync_to_async, async_to_sync
from app.django_models.person.models import Person
import decorator


def async_db_test(func):
    def inner(func, *args, **kwargs):
        return async_to_sync(func)(*args, **kwargs)

    return decorator.decorator(inner, func)


@pytest.fixture
def person() -> Person:
    return Person.objects.create(name="hello world")


@pytest.mark.django_db
@async_db_test
async def test_same_thread_refresh(person) -> None:
    refresh_person = sync_to_async(person.refresh_from_db, thread_sensitive=True)
    # this works fine
    await refresh_person()


@pytest.mark.django_db
@async_db_test
async def test_tasked_refresh(person) -> None:
    refresh_person = sync_to_async(person.refresh_from_db, thread_sensitive=True)
    # app.django_models.person.models.Person.DoesNotExist: Person matching query does not exist.
    await create_task(refresh_person())
