while True:
    try:
        numero = int(input(('Informe o número inteiro: ')))
        break
    except ValueError:
        print("Entrada inválida, insira um número inteiro. \n")

print(f'O número "{numero}" com duas casas decimais é igual {numero:.2f}')
