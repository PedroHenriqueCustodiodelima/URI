n = int(input())
for i in range(n):
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])
    if x > y:
        maior = x
        menor = y
    else:
        maior = y
        menor = x
    soma = 0
    for p in range(menor+1, maior):
        if p % 2 != 0:
            soma += p
    print(soma)
