"""Exercício 2: Agenda de Contatos
Crie uma classe chamada "Contato" que represente um contato em uma agenda.
O contato deve ter os seguintes atributos: nome (string), telefone (string) e email(string).
Implemente métodos para atualizar o telefone e o email do contato."""

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    def atualizar_telefone_contato(self, novo_telefone:str):
        self.telefone = novo_telefone
        print(f'Telefone atualizado com sucesso.')
    def atualizar_email_contato(self,novo_email:str):
        self.email = novo_email
        print(f'Email atualizado com sucesso.')
    def mostrar_contato(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'E-mail: {self.email}')

print('Cadastro de contato ')
nome = input('Informe o nome: ')
telefone = input('Telefone: ')
email = input('E-mail: ')
contato = Contato(nome, telefone, email)

contato.mostrar_contato()
contato.atualizar_telefone_contato(str(input('Novo número: ')))
contato.atualizar_email_contato(str(input('Novo e-mail: ')))
contato.mostrar_contato()
