from django.urls import reverse
import pytest

from denunciaai.django_assertions import dj_assert_contains


@pytest.fixture
def resp(client):
    dados = {'chave_acesso': 'ABCDE12345'}
    resp = client.post(reverse('denuncias:consulta'), dados)
    return resp


@pytest.fixture
def resp_inexistente(client):
    dados = {'chave_acesso': 'TESTE12345'}
    resp_inexistente = client.post(reverse('denuncias:consulta'), dados)
    return resp_inexistente


@pytest.fixture
def resp_get(client):
    resp_get = client.get(reverse('denuncias:consulta'))
    return resp_get


def test_status_code(resp):
    assert resp.status_code == 200


def test_denuncia_nao_encontrada(resp_inexistente):
    dj_assert_contains(resp_inexistente, 'Denúncia não encontrada')


def test_denuncia_assunto(resp):
    dj_assert_contains(resp, 'Teste assunto')


def test_denuncia_mensagem(resp):
    dj_assert_contains(resp, 'Teste mensagem')


def test_acesso_redirect(resp_get):
    assert resp_get.status_code == 302


def test_acesso_url(resp_get):
    assert resp_get.url == reverse('base:home')
