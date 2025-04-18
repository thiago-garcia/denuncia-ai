import secrets
import string
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import DenunciaForm
from .models import Denuncia


def nova(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)

        if form.is_valid():

            caracteres = string.ascii_uppercase + string.digits
            chave = ''.join(secrets.choice(caracteres) for _ in range(10))
            while Denuncia.objects.filter(chave_acesso=chave).exists():
                chave = ''.join(secrets.choice(caracteres) for _ in range(10))

            denuncia = form.save(commit=False)
            denuncia.chave_acesso = chave
            denuncia.save()

            request.session['chave_acesso'] = chave
            return redirect(reverse('denuncias:sucesso'))
    else:
        form = DenunciaForm()

    return render(request, 'denuncias/form_denuncia.html', {'form': form})


def sucesso(request):
    chave_acesso = request.session.pop('chave_acesso', None)
    if not chave_acesso:
        return redirect(reverse('denuncias:nova'))

    return render(request, 'denuncias/sucesso_denuncia.html', {'chave_acesso': chave_acesso})


def consulta(request):
    if request.method == 'POST':
        chave_acesso = request.POST['chave_acesso']
        denuncia = None
        try:
            denuncia = Denuncia.objects.get(chave_acesso=chave_acesso.upper())
        except Denuncia.DoesNotExist:
            pass

        return render(request, 'denuncias/consulta_denuncia.html', {'denuncia': denuncia})
    else:
        return redirect(reverse('base:home'))
