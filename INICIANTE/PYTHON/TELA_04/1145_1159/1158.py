n = int(input())

for i in range(n):
    valores = input().split()
    x = int(valores[0])
    y = int(valores[1])
    soma = 0
    cont = 0
    j = x
    while cont < y:
        if j % 2 != 0:
            soma += j
            cont += 1
        j += 1
    print(soma)
