from django.forms import ModelForm, TextInput, Textarea
from .models import Denuncia


class DenunciaForm(ModelForm):
    class Meta:
        model = Denuncia
        fields = ('assunto', 'mensagem')
        widgets = {
            'assunto': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o assunto',
            }),
            'mensagem': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua mensagem',
                'rows': 5,
            })
        }
