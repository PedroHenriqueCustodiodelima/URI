n = int(input())
x = list(map(int, input().split()))
posicao = 0
for j in range(1, n):
    if x[j] < x[0]:
        posicao = j
        x[0] = x[posicao]                            
print(f"Menor valor: {x[posicao]}")
print(f"Posicao: {posicao}")
