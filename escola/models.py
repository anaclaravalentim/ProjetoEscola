from django.db import models

class Aluno(models.Model):                                  # Criação da tabela/classe de aluno (django cria ID sozinho)
    nome = models.CharField(max_length=30)                  # campo nome varchar 
    rg = models.CharField(max_length=9)                     # campo rg varchar 
    cpf = models.CharField(max_length=11)                   # campo cpf varchar 
    data_nascimento = models.DateField()                    # campo data_nascimento date 
    celular = models.CharField(max_length=11, default='')   # campo celular varchar 

    def __str__(self):
        return self.nome   # Representação em string de um objeto aluno, retorna o nome do aluno