frutas = {
    'banana' : 54,
    'melancia' : 1,
    'kiwi' : 32,
    'pitaya' : 10,
    'uva' : 9
}
# Imprimindo as frutas e quantidade
for frutas, quantidade in frutas.items():
    print(frutas.ljust(10), quantidade)
