from exercicio4 import gera_numeros_aleatorios as numeros_aleatorios

lista = numeros_aleatorios(10)

nomes = ['Roberto', 'Josefa', 'Anastácio', 'Ana', 'Oswald', 'Rogério', 'Biro Biro']
lista.append(nomes)

lista_inteiros = [numero for numero in lista if isinstance(numero,int)]

print(f'A lista contendo apenas número é: \n {lista_inteiros}.')
