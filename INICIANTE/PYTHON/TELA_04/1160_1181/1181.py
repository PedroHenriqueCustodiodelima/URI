a = int(input())
t = input()
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        x = float(input())
        linha.append(x)
    matriz.append(linha)

media = 0
soma = 0.0
for i in range(12):
    if t == 'S':
        soma += matriz[a][i]
    elif t == 'M':
        soma += matriz[a][i]

if t == 'S':
    print("{:.1f}".format(soma))
else:
    media = soma / 12.0
    print("{:.1f}".format(media))
