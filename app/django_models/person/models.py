from django.db import models
from asgiref.sync import sync_to_async
from typing import TypeVar

TModel = TypeVar("TModel", bound=models.Model)


class BonfireAsyncManager(models.Manager):  # type: ignore # excuse: typed in a stub
    """This class is typed via a typestub in async_manager.pyi. Make sure to add new manager commands in the file
       to pass the typecheck.
    """

    async def async_create(self, **kwargs: object) -> TModel:
        obj: TModel = await sync_to_async(super().create, thread_sensitive=True)(
            **kwargs
        )
        return obj


class BonfireBaseModel(models.Model):  # type: ignore
    """Abstract base model class to provide commonly used fields uuid, created_at and updated_at."""

    objects = BonfireAsyncManager()

    class Meta:
        abstract = True


class Person(BonfireBaseModel):
    name = models.CharField(max_length=100)
