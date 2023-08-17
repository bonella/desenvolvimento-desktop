"""Exercício 4: Carrinho de Compras
Crie uma classe chamada "carrinho_de_compras" que represente um carrinho de compras em um sistema de e-commerce.
O carrinho deve ter os seguintes atributos: produtos selecionados (lista de strings) e preços correspondentes (lista de floats).
Implemente métodos para adicionar produtos ao carrinho, calcular o total da compra e mostrar os itens no carrinho."""

#Refatorar utilizando a class Produto do exercicio1
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos_selecionados = []
        self.precos_correspondentes = []
    def adicionar_produto(self, novo_produto:str, preco_produto:float):
        self.produtos_selecionados.append(novo_produto)
        self.produtos_selecionados.append(preco_produto)
        print(f'Produto {novo_produto} adicionado no carrinho.')
    def calcular_total_compra(self):
        return sum(self.precos_correspondentes)
    def mostrar_carrinho_compras(self):
        for i in Carrinho.precos_correspondentes:
            print(self.produtos_selecionados)
            for self.precos_correspondentes in carrinho_de_compras:
                print(self.precos_correspondentes)

Carrinho = CarrinhoDeCompras()
Carrinho.mostrar_carrinho_compras()
