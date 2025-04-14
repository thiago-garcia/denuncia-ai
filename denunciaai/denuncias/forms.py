from django import forms


class DenunciaForm(forms.Form):
    assunto = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o assunto',
        })
    )

    mensagem = forms.CharField(
        max_length=1500,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua mensagem',
            'rows': 5,
        })
    )
