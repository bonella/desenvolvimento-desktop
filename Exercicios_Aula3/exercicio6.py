from exercicio4 import gera_numeros_aleatorios as numeros_aleatorios

numeros = numeros_aleatorios(10)
print(f'A lista de números é: {numeros}')

for i in range(1, len(numeros), 2):
    print(f'Numero {numeros[1]} no índice {i}')
