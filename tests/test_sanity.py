from django.conf import settings


def test_sanity():
    assert 1 + 1 == 2



def test_settings_loaded():
    assert settings.SECRET_KEY
