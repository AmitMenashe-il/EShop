from django.conf import settings

def test_database_name():
    assert settings.DATABASES['default']['NAME'] == str(settings.BASE_DIR / 'db.sqlite3')

def test_allowed_hosts():
    assert settings.ALLOWED_HOSTS == ['*']

def test_language_code():
    assert settings.LANGUAGE_CODE == 'en-us'
