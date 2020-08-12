import pytest
from asgiref.sync import sync_to_async
from app.django_models.person.models import Person


@sync_to_async
def create_person() -> None:
    Person.objects.create(name="hello world")


@pytest.mark.asyncio
@pytest.mark.django_db()
async def test_db() -> None:
    await create_person()
