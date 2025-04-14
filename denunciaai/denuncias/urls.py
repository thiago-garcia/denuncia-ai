from django.urls import path
from .views import nova, sucesso, consulta


app_name = 'denuncias'
urlpatterns = [
    path('nova/', nova, name='nova'),
    path('nova/sucesso/', sucesso, name='sucesso'),
    path('consulta/', consulta, name='consulta'),
]
