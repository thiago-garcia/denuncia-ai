from django.contrib import admin
from django import forms

from .models import Denuncia, Comentario


class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = '__all__'
        widgets = {
            'encerrada': forms.Select(choices=[(True, 'Sim'), (False, 'Não')])
        }


class ComentarioInline(admin.StackedInline):
    model = Comentario
    readonly_fields = ('criado_em',)
    autocomplete_fields = ('usuario',)
    ordering = ('-criado_em',)
    extra = 0


@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    form = DenunciaForm
    list_display = ('admin_assunto', 'admin_chave_acesso', 'admin_criada_em', 'admin_encerrada')
    search_fields = ('assunto', 'chave_acesso', 'criada_em', 'encerrada')
    list_filter = ('criada_em', 'encerrada')
    ordering = ('-criada_em',)
    inlines = [ComentarioInline]

    @admin.display(description='Assunto')
    def admin_assunto(self, obj):
        return obj.assunto[:50] + '...' if len(obj.assunto) > 50 else obj.assunto

    @admin.display(description='Chave de Acesso')
    def admin_chave_acesso(self, obj):
        return obj.chave_acesso

    @admin.display(description='Criada em')
    def admin_criada_em(self, obj):
        return obj.criada_em.strftime('%d/%m/%Y')

    @admin.display(boolean=False, description='Encerrada')
    def admin_encerrada(self, obj):
        return 'Sim' if obj.encerrada else 'Não'
