from rest_framework import viewsets
from escola.models import Aluno
from escola.serializer import AlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet): # ViewSet já possui as operações CRUD configuradas automaticamente
    queryset = Aluno.objects.all()          # Consulta que o ViewSet usará para recuperar os objetos Aluno do banco de dados (todos os alunos)
    serializer_class = AlunoSerializer      # Classe de serializador que será usada para converter os objetos Aluno. O AlunoSerializer é quem controla a serialização e desserialização dos objetos

