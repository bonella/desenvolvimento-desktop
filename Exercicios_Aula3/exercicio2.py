frase = ('Paulo é d4veloper e um b0m musico').split()

for n in frase:
    if any(c.isdigit() for c in n) != False:
        print(f'A palavra {n} contém letras e números')

