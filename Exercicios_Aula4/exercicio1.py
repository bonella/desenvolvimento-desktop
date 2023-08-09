def verifica_numero_par_impar(numero):
    if numero % 2 == 0:
        return 'número par'
    else:
        return 'número impar'

while True:
    try:
        numero = int(input(('Informe o número inteiro: ')))
        break
    except ValueError:
        print("Entrada inválida, insira um número inteiro. \n")

print(f'O número {numero} é {verifica_numero_par_impar(numero)}.')
