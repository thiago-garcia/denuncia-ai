from django.urls import path
from .views import nova


app_name = 'denuncias'
urlpatterns = [
    path('nova/', nova, name='nova'),
]
