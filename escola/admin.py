from django.contrib import admin
from escola.models import Aluno, Curso, Matricula, Professor

# Personalizar a exibição e comportamento dos modelos no painel de administração do Django

class Alunos(admin.ModelAdmin):
    list_display = ('id','nome', 'rg', 'cpf', 'data_nascimento') # Campos do modelo serão exibidos no painel de administração
    list_display_links = ('id', 'nome') # Campos na lista de registros serão transformados em links para editar o registro
    search_fields = ('nome',) # Campos que podem ser usados na barra de pesquisa no painel de administração
    list_per_page = 20 # Quantos registros serão exibidos por página

admin.site.register(Aluno, Alunos) # Registra o modelo Aluno no painel de administração


class Professores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'grau_instrucao')
    list_display_links = ('id', 'nome')
    search_fields = ('codigo_nomecurso',)

admin.site.register(Professor, Professores)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'professor')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', 'aluno')

admin.site.register(Matricula, Matriculas)