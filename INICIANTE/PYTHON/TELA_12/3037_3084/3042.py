def normaliza(posicao):
    if posicao == -1:
        return 2
    if posicao == 3:
        return 0
    return posicao
while (True):
    m = int(input())
    if m == 0:
        break
    caminho = []
    for i in range(m):
        caminho.append(input().split())

    atual = 1
    movs = 0
    for i in range(m):
        if caminho[i][atual] == '0':
            continue
        anterior = atual
        if caminho[i].count('0') == 1:
            atual = caminho[i].index('0')
        else:
            esquerda = normaliza(anterior - 1)
            direita = normaliza(anterior + 1)
            proxima = caminho[i + 1]
            if proxima[esquerda] == '0' and abs(anterior - esquerda) < abs(anterior - direita):
                atual = esquerda
            else:
                atual = direita
        movs += abs(atual - anterior)
    print(movs)