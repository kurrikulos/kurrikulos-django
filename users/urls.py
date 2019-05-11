from django.conf.urls import url
from django.urls import path
from . import views

# Configuração de rotas

urlpatterns = [
    path('', views.initalPage)
]