from django.contrib import admin
from django.urls import path,include
from escola.views import AlunosViewSet, ProfessorViewSet, CursoViewSet, MatriculaViewSet
from rest_framework import routers
from django.conf.urls import url
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#Swagger
schema_view = get_schema_view(  # Cria uma instância do SchemaView a partir da biblioteca drf-yasg
   openapi.Info(
      title="Projeto escola - API",  # Título da documentação
      default_version='v1',             # Versão da documentação
      description="Endpoints do projeto",    # Descrição da documentação
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter() # Instância do DefaultRouter, ajuda na configuração de rotas da API
router.register('alunos', AlunosViewSet, basename='Alunos') # Cria automaticamente as rotas para as operações CRUD.
router.register('professores', ProfessorViewSet, basename='Professores') 
router.register('cursos', CursoViewSet, basename='Cursos') 
router.register('matriculas', MatriculaViewSet, basename='Matriculas') 

urlpatterns = [                      # Lista que define as URLs do aplicativo
    path('admin/', admin.site.urls), # Rota para o painel de administração 
    path('', include(router.urls)),   # Inclui rotas do router.As rotas definidas para as operações CRUD sejam acessíveis pela URLs
    path('token/',TokenObtainPairView.as_view()),   
    path('token/refresh/',TokenRefreshView.as_view())
]

#Swagger (documentação)
urlpatterns += [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'), # Rota para o esquema JSON da API
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # # Rota para a interface Swagger UI da documentação
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # Rota para a interface Redoc da documentação
]