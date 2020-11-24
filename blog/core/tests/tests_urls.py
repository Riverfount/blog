from django.test import Client
from django.urls import reverse

from blog.core.urls import urlpatterns


client = Client()


def tests_url_length():
    """Checks the exact number of urls in the system"""
    assert 1 <= len(urlpatterns)


def tests_homepage_status_ok():
    """
    Checks if the homepage in the root of the site responds
    with status code 200 ok
    """
    response = client.get('/')
    assert response.status_code == 200


def test_view_url_by_name():
    """Checks if the homepage responds by its name"""
    response = client.get(reverse('index'))
    assert response.status_code == 200
