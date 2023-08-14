from django.test import TestCase
from ..models import Professor

class ProfessorTestCase(TestCase):
    @classmethod # Método de classe, ou seja, será executado uma vez antes de executar qualquer teste na classe
    def setUpTestData(self): 
        Professor.objects.create(nome='Professor 1', grau_instrucao='M') #Cria objeto professor

    def test_nome_max_length(self): # Verifica se o campo nome tem o comprimento máximo correto
        professor = Professor.objects.get(id=1)
        max_length = professor._meta.get_field('nome').max_length
        self.assertEquals(max_length, 30)

    def test_grau_instrucao_choices(self): # Verifica se as opções de escolha para o campo grau_instrucao estão corretas
        professor = Professor.objects.get(id=1)
        choices = professor._meta.get_field('grau_instrucao').choices
        self.assertEquals(choices, (('S', 'Superior Completo'), ('M', 'Mestrado'), ('D', 'Doutorado')))

    def test_str_method(self): # Verifica se o método __str__ retorna o nome do professor corretamente
        professor = Professor.objects.get(id=1)
        expected_name = professor.nome
        self.assertEquals(str(professor), expected_name)