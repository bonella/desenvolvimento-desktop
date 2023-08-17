"""Exercício 2: Cadastro de Alunos
Crie uma classe chamada "Aluno" que represente um aluno em um sistema de cadastro.
O aluno deve ter os seguintes atributos: nome (string), idade (inteiro) e uma lista de disciplinas cursadas (lista de strings).
Implemente um método para adicionar disciplinas ao aluno e um método para mostrar todas as disciplinas cursadas."""
class Aluno:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade
        self.__disciplinas = []

    def adicionar_disciplina_aluno(self, disciplina):
        self.__disciplinas.append(disciplina)
        print(f'Disciplina adicionada com sucesso.')

    def mostrar_disciplinas(self):
        return self.__disciplinas

aluno1 = Aluno('Vitoria', 24)
aluno1.adicionar_disciplina_aluno('Desenvolvimento Web')
aluno1.adicionar_disciplina_aluno('LPA')

print(f'Disciplinas atuais do aluno "{aluno1.nome}": {", ".join(aluno1.mostrar_disciplinas())}')

