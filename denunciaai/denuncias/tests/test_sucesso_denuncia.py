from django.urls import reverse
import pytest

from denunciaai.django_assertions import dj_assert_contains


@pytest.fixture
def resp(client, db):
    dados = {'assunto': 'Exemplo', 'mensagem': 'Exemplo'}
    resp = client.post(reverse('denuncias:nova'), dados)
    return resp


@pytest.fixture
def resp_acesso_sucesso(client):
    resp_acesso_sucesso = client.get(reverse('denuncias:sucesso'))
    return resp_acesso_sucesso


@pytest.fixture
def resp_follow(client, db):
    dados = {'assunto': 'Exemplo', 'mensagem': 'Exemplo'}
    resp_follow = client.post(reverse('denuncias:nova'), dados, follow=True)
    return resp_follow


def test_sucesso_redirect_code(resp):
    assert resp.status_code == 302


def test_sucesso_redirect_url(resp):
    assert resp.url == reverse('denuncias:sucesso')


def test_sucesso_direto_code(resp_acesso_sucesso):
    assert resp_acesso_sucesso.status_code == 302


def test_sucesso_direto_redirect_url(resp_acesso_sucesso):
    assert resp_acesso_sucesso.url == reverse('denuncias:nova')


def test_sucesso_chave(resp_follow):
    dj_assert_contains(resp_follow, 'ABCDE12345')
