from django.test import Client
from django.urls import reverse


client = Client()


def test_view_use_his_tamplate():
    """Checks if the homepage use hist tamplate"""
    response = client.get(reverse('index'))
    assert response.templates[0].name == 'index.html'
