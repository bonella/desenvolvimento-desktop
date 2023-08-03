from exercicio11 import gera_numeros_aleatorios

lista = gera_numeros_aleatorios(10)

nomes = ['Roberto', 'Josefa', 'Anastácio', 'Ana', 'Oswald', 'Rogério', 'BiroBiro']

[lista.append(nome) for nome in nomes]

dados_agrupados = ''.join([str(item) for item in lista])
print(f'Os números da lista agrupados sem espaço geram a seguinte string: \n'
      f'{dados_agrupados} ')
