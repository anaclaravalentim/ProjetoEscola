from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from ..views import AlunosViewSet
from ..models import Aluno
from django.contrib.auth.models import User

class AlunosViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory() # Instância da classe usada para criar instâncias de Request para teste
        cls.view = AlunosViewSet.as_view({'get': 'list', 'post': 'create'}) # Instância da view para 'GET' e 'POST'
        cls.url = reverse('Alunos-list') # Gera a URL reversa
        cls.user = User.objects.create_user(username='testuser', password='testpass') # Usuário de teste

    def test_list_alunos(self): # Verifica se a listagem de alunos (operação GET) retorna um status 200 (OK)
        request = self.factory.get(self.url) # Cria uma solicitação GET usando a URL gerada
        force_authenticate(request, user=self.user) # Autentica usuário 
        response = self.view(request) #Chama a view com a solicitação criada
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Verifica se o status da resposta é HTTP 200 (OK)

    def test_create_aluno(self): # Testa a criação de um novo aluno (operação POST) e verifica se o status é 201 (Criado)
        data = {'nome': 'Novo Aluno', 'rg': '123456', 'cpf': '78901234567', 'data_nascimento': '2000-01-01'} # Dicionário de dados para novo aluno
        request = self.factory.post(self.url, data, format='json') # Cria uma solicitação POST
        force_authenticate(request, user=self.user) # Autentica o usuário 
        response = self.view(request) # Chama a view com a solicitação criada
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # Verifica se o status da resposta é HTTP 201 (Criado)
        self.assertEqual(Aluno.objects.count(), 1) # Verifica se um aluno foi criado no banco 
        self.assertEqual(Aluno.objects.get().nome, 'Novo Aluno') # Verifica se o nome do aluno criado é 'Novo Aluno'.