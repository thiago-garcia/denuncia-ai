from django.urls import path
from .views import home


app_name = 'restrito'
urlpatterns = [
    path('', home, name='home'),
]
