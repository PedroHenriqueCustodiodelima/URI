c = int(input())
t = input()
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        x = float(input())
        linha.append(x)
    matriz.append(linha)
media = 0
soma = 0
for i in range(12):
    if t == 'S':
        soma += matriz[i][c]
    elif t == 'M':
        soma += matriz[i][c]
media = soma / 12 if t == 'M' else soma
print('{:.1f}'.format(media))
