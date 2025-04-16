from django.urls import reverse
import pytest

from denunciaai.denuncias.models import Denuncia
from denunciaai.django_assertions import dj_assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('denuncias:nova'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_form_denuncia(resp):
    dj_assert_contains(resp, '<form method="post" action=""')


def test_form_input_assunto(resp):
    dj_assert_contains(resp, '<input type="text" name="assunto"')


def test_form_input_mensagem(resp):
    dj_assert_contains(resp, '<textarea name="mensagem"')


@pytest.fixture
def resp_acesso_sucesso(client):
    resp_acesso_sucesso = client.get(reverse('denuncias:sucesso'))
    return resp_acesso_sucesso


def test_sucesso_direto_code(resp_acesso_sucesso):
    assert resp_acesso_sucesso.status_code == 302
    assert resp_acesso_sucesso.url == reverse('denuncias:nova')


@pytest.fixture
def resp_post(client, db):
    dados = {'assunto': 'Chave', 'mensagem': 'Teste'}
    resp_post = client.post(reverse('denuncias:nova'), dados, follow=True)
    denuncia = Denuncia.objects.get(assunto='Chave', mensagem='Teste')
    return resp_post, denuncia


def test_sucesso_chave(resp_post):
    response, denuncia = resp_post
    dj_assert_contains(response, denuncia.chave_acesso)
