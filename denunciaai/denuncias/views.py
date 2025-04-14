from django.shortcuts import render

from .forms import DenunciaForm


def nova(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)

        if form.is_valid():
            pass
    else:
        form = DenunciaForm()

    return render(request, 'denuncias/form_denuncia.html', {'form': form})
