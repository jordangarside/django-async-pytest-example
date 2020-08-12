import pytest
from asgiref.sync import sync_to_async
from app.django_models.person.models import Person


def create_person() -> Person:
    return Person.objects.create(name="hello world")


def count_persons() -> int:
    return Person.objects.count()


@pytest.mark.django_db()
def test_db() -> None:
    create_person()
    assert count_persons() == 1


@pytest.mark.django_db()
def test_db_again() -> None:
    create_person()
    assert count_persons() == 1
