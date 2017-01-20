import os
import django
import pytest


# We manually designate which settings we will be using in
# an environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feiraslivresapi.settings")

# `pytest` automatically calls this function once when tests are run.


def pytest_configure():
    # If you have any test specific settings, you can declare them here,
    # e.g.
    # settings.DEBUG = False
    # settings.PASSWORD_HASHERS = (
    #     'django.contrib.auth.hashers.MD5PasswordHasher',
    # )
    django.setup()


@pytest.fixture
def feira():
    from feiraslivres.models import Feira
    return Feira.objects.get(pk=3)
