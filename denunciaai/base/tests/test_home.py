from django.urls import reverse
import pytest

from denunciaai.django_assertions import dj_assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_form_consulta(resp):
    dj_assert_contains(resp, '<form')


def test_form_input_chave(resp):
    dj_assert_contains(resp, '<input type="text" name="chave_acesso"')


def test_link_abrir_denuncia(resp):
    dj_assert_contains(resp, '<a href="%s' % reverse('denuncias:nova'))


def test_link_restrito(resp):
    dj_assert_contains(resp, '<a href="/restrito"')
