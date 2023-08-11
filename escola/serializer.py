from rest_framework import serializers
from escola.models import Aluno

class AlunoSerializer(serializers.ModelSerializer): #simplifica a criação de serializadores 
    class Meta:                 # Define classe interna usada para configurar metadados do serializador
        model = Aluno           # Modelo que o serializador está associado
        fields = '__all__'      # Define quais campos do modelo Aluno serão incluídos no serializador (todos)
