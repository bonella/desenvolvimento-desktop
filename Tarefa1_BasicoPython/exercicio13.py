a, b = 0, 1
print(f'Inicial {a}')

for _ in range(14):
    a, b = b, a + b
    print(a)
