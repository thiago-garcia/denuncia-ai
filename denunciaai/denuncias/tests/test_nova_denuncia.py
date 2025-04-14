from django.urls import reverse
import pytest

from denunciaai.django_assertions import dj_assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('denuncias:nova'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_form_denuncia(resp):
    dj_assert_contains(resp, '<form method="post"')


def test_form_input_assunto(resp):
    dj_assert_contains(resp, '<input type="text" name="assunto"')


def test_form_input_mensagem(resp):
    dj_assert_contains(resp, '<textarea name="mensagem"')
