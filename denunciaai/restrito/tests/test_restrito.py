from django.urls import reverse
import pytest

from denunciaai.django_assertions import dj_assert_contains


@pytest.fixture
def resp_nao_logada(client):
    return client.get(reverse('restrito:home'))


def test_restrito_home_sem_login(resp_nao_logada):
    assert resp_nao_logada.status_code == 302
    assert resp_nao_logada.url.startswith(reverse('login'))


@pytest.fixture
def resp(client_com_usuario_logado):
    return client_com_usuario_logado.get(reverse('restrito:home'))


def test_logout(resp):
    dj_assert_contains(resp, 'action="%s"' % reverse('logout'))
    dj_assert_contains(resp, 'Sair')
