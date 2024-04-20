import os
from django.conf import settings
from django.test import SimpleTestCase


def test_database_name_in_settings():
    assert settings.DATABASES['default']['NAME'] == BASE_DIR / 'db.sqlite3'

def test_allowed_hosts():
    assert '*' in settings.ALLOWED_HOSTS

def test_language_code():
    assert settings.LANGUAGE_CODE == 'en-us'

def test_debug_mode():
    assert settings.DEBUG == 'False'
