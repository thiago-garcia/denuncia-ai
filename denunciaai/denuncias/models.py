from django.db import models


class Denuncia(models.Model):
    assunto = models.CharField(max_length=150)
    mensagem = models.TextField(max_length=1500)
    chave_acesso = models.CharField(max_length=10, unique=True, editable=False)
    encerrada = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.assunto
