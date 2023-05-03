MAXSIZE = 101
matriz = [[0 for i in range(MAXSIZE)] for j in range(MAXSIZE)]
memoria = [[-1 for i in range(MAXSIZE)] for j in range(MAXSIZE)]
def calcula(linha, coluna):
    soma = 0
    if (memoria[linha][coluna] != -1):
        return memoria[linha][coluna]
    if (linha == 1):
        return matriz[linha][coluna]
    for i in range(linha):
        soma += matriz[linha][coluna + i]
    memoria[linha][coluna] = soma + mim(calcula(linha - 1, coluna), calcula(linha - 1, coluna + 1))
    return memoria[linha][coluna]
def mim(a, b):
    if (a < b):
        return a
    else:
        return b
tamMatriz = int(input())
for i in range(1, tamMatriz+1):
    linha = list(map(int, input().split()))
    for j in range(1, tamMatriz+1):
        matriz[i][j] = linha[j-1]
print(calcula(tamMatriz, 1))
