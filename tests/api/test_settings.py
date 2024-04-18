import os
from django.conf import settings
from django.test import SimpleTestCase


def test_database_name_in_settings():
    settings_file_path = os.path.join(settings.BASE_DIR, 'backend', 'settings.py')
    with open(settings_file_path, 'r') as f:
        settings_contents = f.read()
    assert "BASE_DIR / 'db.sqlite3'" in settings_contents

def test_allowed_hosts():
    assert '*' in settings.ALLOWED_HOSTS

def test_language_code():
    assert settings.LANGUAGE_CODE == 'en-us'
