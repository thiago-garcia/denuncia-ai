from django.db import models
from django.utils.crypto import get_random_string


class Denuncia(models.Model):
    assunto = models.CharField(max_length=150)
    mensagem = models.TextField(max_length=1500)
    chave_acesso = models.CharField(max_length=10, unique=True, editable=False)
    encerrada = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.assunto

    def _gerar_chave_acesso(self):
        chave = get_random_string(10).upper()
        while Denuncia.objects.filter(chave_acesso=chave).exists():
            chave = get_random_string(10).upper()
        return chave

    def save(self, *args, **kwargs):
        if not self.chave_acesso:
            self.chave_acesso = self._gerar_chave_acesso()
        super().save(*args, **kwargs)
