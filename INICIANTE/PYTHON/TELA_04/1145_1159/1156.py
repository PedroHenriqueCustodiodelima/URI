numero = 1
x = 1.0
soma = 0.0
while numero <= 39:
    soma = soma + numero / x
    x = x * 2.0
    numero += 2
print(f'{soma:.2f}')
