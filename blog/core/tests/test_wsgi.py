import os

from django.core.handlers.wsgi import WSGIHandler

from blog.wsgi import application


def test_wsgi_default_settings():
    assert 'blog.settings' == os.environ["DJANGO_SETTINGS_MODULE"]


def test_application_instace():
    assert isinstance(application, WSGIHandler)
