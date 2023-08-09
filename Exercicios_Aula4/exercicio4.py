while True:
    try:
        area = float(input(('Informe a área em m² a ser pintada: ')))
        break
    except ValueError:
        print("Entrada inválida, insira um número válido. \n")

litros = area / 3

if area % 54 == 0:
	latas = area / 54
else:
	latas = int(area / 54) + 1

preco = latas * 80
print(f'Você vai precisar de {latas} latas e gastará R$ {preco:.2f}')

