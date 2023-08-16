"""Exercício 2: Cadastro de Alunos
Crie uma classe chamada "Aluno" que represente um aluno em um sistema de cadastro.
O aluno deve ter os seguintes atributos: nome (string), idade (inteiro) e uma lista de disciplinas cursadas (lista de strings).
Implemente um método para adicionar disciplinas ao aluno e um método para mostrar todas as disciplinas cursadas."""
class Aluno:

    def __init__(self, nome:str, idade:int, disciplinas_cursadas:list):
        self.nome = nome
        self.idade = idade
        self.disciplinas_cursadas = disciplinas_cursadas

    def adicionar_disciplina_aluno(self, disciplinas:list):
        self.disciplinas_cursadas += disciplinas
        print(f'Disciplinas adicionadas com sucesso.')

    def mostrar_disciplinas(self):
        return self.disciplinas_cursadas

aluno1 = Aluno('Vitoria', 24, ['POO', 'Arquitetura de rede', 'Desenvolvimento Desktop'])
print(f'Disciplinas atuais do aluno "{aluno1.nome}": {aluno1.mostrar_disciplinas()}')
nova_disciplina = [input('Informe a nova disciplina: ')]
aluno1.adicionar_disciplina_aluno(nova_disciplina)
print(f'Disciplinas atuais do aluno "{aluno1.nome}": {aluno1.mostrar_disciplinas()}')
