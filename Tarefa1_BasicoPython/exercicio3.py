numeros = []
valida = True

numeros.append(input("Digite o primeiro número: "))
numeros.append(input("Digite o segundo número: "))

def verifica_inteiros(numero) -> bool:
    while True:
        try:
            int(numero)
            return True
        except ValueError as e:
            print(f'O valor {numero} não é numérico.')
            print(f'Erro: {e}')
            return False

for n in numeros:
    if verifica_inteiros(n) is False:
        valida = False

if valida:
    print(f'O valor da soma do números {numeros[0]} e {numeros[1]} é: {int(numeros[0]) + int(numeros[1])}')
