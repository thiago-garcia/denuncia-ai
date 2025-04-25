from django.urls import reverse
import pytest


@pytest.fixture
def resp(client):
    return client.get(reverse('restrito:home'))


def test_status_code(resp):
    assert resp.status_code == 200
