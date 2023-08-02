numeros = input('Insira uma lista de números separados por espaço: ').split()
numeros = [int(numero) for numero in numeros] # list comprehension
pares = [num for num in numeros if num % 2 == 0]
print(f'Os números pares são {pares}')
