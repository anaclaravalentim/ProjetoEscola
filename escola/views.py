from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Professor, Curso, Matricula
from escola.serializer import AlunoSerializer, ProfessorSerializer, CursoSerializer, MatriculaSerializer



class AlunosViewSet(viewsets.ModelViewSet): # ViewSet já possui as operações CRUD configuradas automaticamente
    queryset = Aluno.objects.all()          # Consulta que o ViewSet usará para recuperar os objetos Aluno do banco de dados (todos os alunos)
    serializer_class = AlunoSerializer      # Classe de serializador que será usada para converter os objetos Aluno. O AlunoSerializer é quem controla a serialização e desserialização dos objetos
    permission_classes = (IsAuthenticated,) # Verifica se o usuário está autenticado, ou seja, se possui um token de autenticação válido


class ProfessorViewSet(viewsets.ModelViewSet): 
    queryset = Professor.objects.all()          
    serializer_class = ProfessorSerializer      
    permission_classes = (IsAuthenticated,)


class CursoViewSet(viewsets.ModelViewSet): 
    queryset = Curso.objects.all()          
    serializer_class = CursoSerializer      
    permission_classes = (IsAuthenticated,)


class MatriculaViewSet(viewsets.ModelViewSet): 
    queryset = Matricula.objects.all()          
    serializer_class = MatriculaSerializer      
    permission_classes = (IsAuthenticated,)
