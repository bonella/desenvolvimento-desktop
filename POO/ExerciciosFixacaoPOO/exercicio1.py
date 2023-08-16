class Produto:

    def __init__(self, nome:str, preco:float, quantidade_estoque:int):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def adicionar_produto_estoque(self, quantidade:int):
        self.quantidade_estoque += quantidade
        print(f'Quantidade alterada para o produto {self.nome} adicionado.')

    def remover_produto_estoque(self, quantidade:int):
        if self.quantidade_estoque >= quantidade:
            self.quantidade_estoque -= quantidade
            print(f'Removido {quantidade} do produto {self.nome} no estoque')
        else:
            print('Verifique a quantidade informada')

    def calcular_valor_estoque(self):
        return self.quantidade_estoque * self.preco

estoque = []

nome_produto = input('Informe o nome do produto: ')
valor_produto = float(input(f'Informe o valor do produto: '))
quantidade_produto = int(input(f'Informe a quantidade do produto": '))
produto = Produto(nome_produto, valor_produto, quantidade_produto)
estoque.append(produto)

for produto in estoque:
    print(f'ID: {estoque.index(produto)}')
    print(f'Nome: {produto.nome}')
    print(f'Preço: {produto.preco}')
    print(f'Quantidade no estoque: {produto.quantidade_estoque}')
produto.remover_produto_estoque(2)
print(f'Total do estoque {produto.calcular_valor_estoque()}')
estoque.clear()
