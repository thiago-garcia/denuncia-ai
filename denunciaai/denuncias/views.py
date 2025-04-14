from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import DenunciaForm


def nova(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)

        if form.is_valid():
            chave = 'ABCDE12345'
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
        denuncia = {}
        if chave_acesso == 'ABCDE12345':
            denuncia['assunto'] = 'Teste assunto'
            denuncia['mensagem'] = 'Teste mensagem'
        return render(request, 'denuncias/consulta_denuncia.html', {'denuncia': denuncia})
    else:
        return redirect(reverse('base:home'))
