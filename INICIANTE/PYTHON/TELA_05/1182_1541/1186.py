operacao = input()
contDiagonal = 11
matriz = [[0 for j in range(12)] for i in range(12)]
soma = 0
media = 0

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

for k in range(1, 12):
    for p in range(11, contDiagonal-1, -1):
        soma += matriz[k][p]
        media = soma / 66
    contDiagonal -= 1

if operacao == 'S':
    print("{:.1f}".format(soma))
elif operacao == 'M':
    print("{:.1f}".format(media))