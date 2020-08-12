import pytest
from asgiref.sync import sync_to_async
from app.django_models.person.models import Person


@sync_to_async
def create_person() -> Person:
    return Person.objects.create(name="hello world")


@sync_to_async
def count_persons() -> int:
    return Person.objects.count()


@pytest.mark.asyncio
@pytest.mark.django_db()
async def test_db() -> None:
    await create_person()
    assert await count_persons() == 1


@pytest.mark.asyncio
@pytest.mark.django_db()
async def test_db_again() -> None:
    await create_person()
    assert await count_persons() == 1
