from django.db import models

class Aluno(models.Model):                                  # Criação da tabela/classe de aluno (django cria ID sozinho)
    nome = models.CharField(max_length=30)                  # campo nome varchar 
    rg = models.CharField(max_length=9)                     # campo rg varchar 
    cpf = models.CharField(max_length=11)                   # campo cpf varchar 
    data_nascimento = models.DateField()                    # campo data_nascimento date 
    celular = models.CharField(max_length=11, default='')   # campo celular varchar 

    def __str__(self):
        return self.nome   # Representação em string de um objeto aluno, retorna o nome do aluno
    

class Professor(models.Model):
    GRAU = (                       #tupla de escolhas
        ('S', 'Superior Completo'),
        ('M', 'Mestrado'),
        ('D', 'Doutorado')
    )
    grau_instrucao = models.CharField(max_length=1, choices=GRAU, blank=False, null=False,default='S')  # campo grau de instrução varchar
    nome = models.CharField(max_length=30)                                                              # campo nome varchar
    
    def __str__(self):      # Representação em string de um objeto Professor, retorna o nome do Professor
        return self.nome


class Curso(models.Model):
    NIVEL = (                       #tupla de escolhas
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)      #campo chave vinda da tabela Professor
    codigo_curso = models.CharField(max_length=10)                          #campo codigo varchar
    descricao = models.CharField(max_length=100)                            #campo descricao varchar
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False,default='B') #campo nivel varchar
    
    def __str__(self):
        return self.descricao


class Matricula(models.Model):       
    PERIODO = (                     #tupla de escolhas
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)       #campo chave vinda da tabela Aluno
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)       #campo chave vinda da tabela Curso
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False,default='M') #campo periodo varchar
