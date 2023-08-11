from rest_framework import serializers
from escola.models import Aluno, Professor, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer): #simplifica a criação de serializadores 
    class Meta:                 # Define classe interna usada para configurar metadados do serializador
        model = Aluno           # Modelo que o serializador está associado
        fields = '__all__'      # Define quais campos do modelo Aluno serão incluídos no serializador (todos)


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:                
        model = Professor         
        fields = '__all__'    


class CursoSerializer(serializers.ModelSerializer):
    class Meta:                
        model = Curso         
        fields = '__all__'    


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:                
        model = Matricula         
        fields = '__all__'    
