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
class Estoque:
    def __init__(self):
        self.produtos = []
    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)
    def remover_produto(self, produto: Produto):
        self.produtos.remove(produto)
    def calcular_valor_estoque(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco * produto.quantidade_estoque
        return total

nome_produto = input('Informe o nome do produto: ')
valor_produto = float(input(f'Informe o valor do produto: '))
quantidade_produto = int(input(f'Informe a quantidade do produto": '))
produto = Produto(nome_produto, valor_produto, quantidade_produto)
produto2 = Produto('Camisa', 45.25, 5)
estoque = Estoque()
estoque.adicionar_produto(produto)
estoque.adicionar_produto(produto2)

produto.remover_produto_estoque(2)
print(f'Total do estoque {estoque.calcular_valor_estoque()}')

