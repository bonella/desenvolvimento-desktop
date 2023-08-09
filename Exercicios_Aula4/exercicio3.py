def caucular_peso_ideal(altura):
    peso_ideal = (72.7 * altura) - 58
    print(f'O peso ideal para a sua altura de "{altura}m" é {"{:.2f}".format(peso_ideal)} kg.')

while True:
    try:
        numero = float(input(('Informe a sua altura: ')))
        break
    except ValueError:
        print("Entrada inválida, insira um número válido. \n")

caucular_peso_ideal(numero)
