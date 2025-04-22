from django.urls import reverse
import pytest
from django.utils.timezone import localtime
from model_bakery import baker

from denunciaai.django_assertions import dj_assert_contains
from denunciaai.denuncias.models import Denuncia, Comentario


@pytest.fixture
def denuncia(db):
    return baker.make(Denuncia, chave_acesso='ABCDE12345')


@pytest.fixture
def usuario(db, django_user_model):
    return baker.make(django_user_model, first_name='Fulano')


@pytest.fixture
def comentarios(denuncia, usuario):
    return baker.make(Comentario, 3, denuncia=denuncia, usuario=usuario)


@pytest.fixture
def resp(client, denuncia, comentarios):
    resp = client.post(reverse('denuncias:consulta'), {'chave_acesso': denuncia.chave_acesso})
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_denuncia_assunto(resp, denuncia):
    dj_assert_contains(resp, denuncia.assunto)


def test_denuncia_mensagem(resp, denuncia):
    dj_assert_contains(resp, denuncia.mensagem)


def test_denuncia_criada_em(resp, denuncia):
    data = localtime(denuncia.criada_em).strftime('%d/%m/%Y')
    dj_assert_contains(resp, f'Criado em: {data}')


def test_denuncia_status(resp, denuncia):
    status = 'Encerrada' if denuncia.encerrada else 'Aberta'
    dj_assert_contains(resp, f'Status: {status}')


def test_comentarios_usuario(resp, comentarios):
    for comentario in comentarios:
        dj_assert_contains(resp, comentario.usuario.first_name)


def test_comentarios_criada_em(resp, comentarios):
    for comentario in comentarios:
        criado_em = localtime(comentario.criado_em).strftime('%d/%m/%Y, %H:%M')
        dj_assert_contains(resp, criado_em)


def test_comentarios_mensagem(resp, comentarios):
    for comentario in comentarios:
        dj_assert_contains(resp, comentario.mensagem)


@pytest.fixture
def resp_inexistente(client, db):
    dados = {'chave_acesso': 'TESTE12345'}
    resp_inexistente = client.post(reverse('denuncias:consulta'), dados)
    return resp_inexistente


def test_denuncia_nao_encontrada(resp_inexistente):
    dj_assert_contains(resp_inexistente, 'Denúncia não encontrada')


@pytest.fixture
def resp_get(client):
    resp_get = client.get(reverse('denuncias:consulta'))
    return resp_get


def test_acesso_redirect(resp_get):
    assert resp_get.status_code == 302


def test_acesso_url(resp_get):
    assert resp_get.url == reverse('base:home')
