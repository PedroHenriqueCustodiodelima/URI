operacao = input()
contDiagonal = 0
matriz = [[0] * 12 for _ in range(12)]
soma = 0
media = 0

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

for k in range(1, 12):
    for p in range(contDiagonal + 1):
        soma += matriz[k][p]
        media = soma / 66
    contDiagonal += 1

if operacao == 'S':
    print("{0:0.1f}".format(soma))
elif operacao == 'M':
    print("{0:0.1f}".format(media))
