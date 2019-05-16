from django.contrib import admin
from django.urls import path

# views
from contas.views import home, listagem, criar_currilo, atualizar_curriculo, deletar_curriculo, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  home, name='url_home'),
    path('usuario/login', login, name='url_login'),
    path('curriculo/listagem', listagem, name='url_listagem'),
    path('curriculo/criar', criar_currilo, name='url_criar'),
    path('curriculo/atualizar/<int:pk>/', atualizar_curriculo, name='url_atualizar'),
    path('curriculo/deletar/<int:pk>/', deletar_curriculo, name='url_deletar')
]
