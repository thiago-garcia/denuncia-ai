import pytest
from model_bakery import baker


@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = baker.make(django_user_model, first_name='Fulano')
    return usuario_modelo


@pytest.fixture
def client_com_usuario_logado(usuario, client):
    client.force_login(usuario)
    return client
