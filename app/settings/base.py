import os
from typing import List


ALLOWED_HOSTS: List[str] = []
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = False
INSTALLED_APPS: List[str] = [
    "django.contrib",
    "app.django_models.person",
]
SECRET_KEY = "aaa"
TIME_ZONE = "US/Pacific"
TRACING = None
USE_TZ = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "NAME": "postgres",
        "PASSWORD": "password",
        "PORT": 5432,
        "USER": "postgres",
        "CONN_MAX_AGE": 0,
    },
}
