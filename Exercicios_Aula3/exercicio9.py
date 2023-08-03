from exercicio4 import gera_numeros_aleatorios as numeros_aleatorios

lista = numeros_aleatorios(10)

nomes = ['Roberto', 'Josefa', 'Anastácio', 'Ana', 'Oswald', 'Rogério', 'Biro Biro']
lista.append(nomes)

print(f'A lista ficou com os seguintes dados: \n{lista}')
