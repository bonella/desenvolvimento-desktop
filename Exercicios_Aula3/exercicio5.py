from exercicio4 import gera_numeros_aleatorios as numeros_aleatorios

numeros = numeros_aleatorios(10)
print(f'Lista de números aleatórios \n {numeros}.')

for numero in numeros:
    if numero % 5 == 0:
        print(f'Número múltiplo por 5: {numero}.')
        if numero > 95 and numero < 150:
            #print(f'Número {numero} é menor que 95 e maior que 150.')
            pass
        elif numero > 1500:
            break
        else:
            print(f'O número {numero} não se encaixa em nenhuma condicional.')
            continue


