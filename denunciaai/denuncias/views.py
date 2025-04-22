from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import DenunciaForm
from .models import Denuncia


def nova(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)

        if form.is_valid():
            denuncia = form.save()
            request.session['chave_acesso'] = denuncia.chave_acesso
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
        try:
            denuncia = Denuncia.objects.get(chave_acesso=chave_acesso.upper())
            comentarios = denuncia.comentario_set.order_by('criado_em').all()
        except Denuncia.DoesNotExist:
            denuncia = None
            comentarios = None

        return render(request, 'denuncias/consulta_denuncia.html', {'denuncia': denuncia, 'comentarios': comentarios})
    else:
        return redirect(reverse('base:home'))
