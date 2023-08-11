from django.contrib import admin
from django.urls import path,include
from escola.views import AlunosViewSet
from rest_framework import routers

router = routers.DefaultRouter() # Instância do DefaultRouter, ajuda na configuração de rotas da API
router.register('alunos', AlunosViewSet, basename='Alunos') # Cria automaticamente as rotas para as operações CRUD.

urlpatterns = [                      # Lista que define as URLs do aplicativo
    path('admin/', admin.site.urls), # Rota para o painel de administração 
    path('', include(router.urls))   # Inclui rotas do router.As rotas definidas para as operações CRUD sejam acessíveis pela URLs 
]
