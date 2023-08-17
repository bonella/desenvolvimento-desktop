"""
Exercício 9: Catálogo de Livros
Crie uma classe chamada "Livro" que represente um livro em um catálogo.
O livro deve ter os seguintes atributos: título (string), autor (string), ano de publicação (inteiro) e gênero (string).
Implemente métodos para atualizar o ano de publicação e para exibir os detalhes do livro.
"""

class Livro:

    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero

    def atualizar_ano_publicao(self, ano):
        self.ano = ano

    def exibir_detalhes(self):
        print(f'Livro: {self.titulo}, autor {self.autor} \n'
              f'Ano de publicação {self.ano} e gênero {self.genero}')

livro = Livro('Lord of the rings', 'J.R.R Tolkien', '1954', 'Fantasia')
livro.exibir_detalhes()
livro.atualizar_ano_publicao('2021')
livro.exibir_detalhes()
